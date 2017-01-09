# -*- coding: UTF-8 -*-

import requests


class DataMosRu:
    """
    Class to interact with http://data.mos.ru with API.
    """
    def __init__(self, api_key):
        self.api_key = api_key
        self.site = 'http://api.data.mos.ru/'
        self.request_items_portion = 500
        self._api_version = None

    def request(self, resource, params=None, **kwargs):
        if params is None:
            params = {}

        params.update(kwargs)
        r = requests.get(self.site + resource, params=params)

        if r.status_code != requests.codes.ok:
            raise DMRStatusError(r)

        return r

    def request_with_version(self, resource, params=None, **kwargs):
        if self._api_version is None:
            self._api_version = self.getAPIVersion()

        resource_new = 'v{version}/{resource}'.format(
            version=self._api_version,
            resource=resource
        )
        return self.request(resource_new, params, **kwargs)

    def getAPIVersion(self):
        '''Get current API version.'''
        r = self.request('version')
        return r.json()['Version']

    def getDatasets(self):
        '''Get datasets list.'''
        count = None
        received = 0
        resource = 'datasets'

        while count is None or received < count:
            params = {
                '$top': self.request_items_portion,
                '$skip': received,
                '$inlinecount': 'allpages',
                'foreign': 'false',
            }
            r = self.request_with_version(resource, params)

            if r.status_code != requests.codes.ok:
                raise DMRStatusError(r)

            result_json = r.json()
            count = result_json['Count']
            items = result_json['Items']
            yield from items
            received += len(items)

    def getDatasetInfo(self, dataset_id):
        '''Return list of columns for dataset.'''
        resource = 'datasets/{id}'.format(id=dataset_id)
        r = self.request_with_version(resource)
        return r.json()

    def getDatasetLen(self, dataset_id):
        '''Return items count in dataset.'''
        resource = 'datasets/{id}/count'.format(id=dataset_id)
        r = self.request_with_version(resource)
        return r.json()

    def getDatasetVersion(self, dataset_id):
        '''Get dataset version.
        Return tuple (versionNumber, releaseNumber).'''
        resource = 'datasets/{id}/version'.format(id=dataset_id)
        r = self.request_with_version(resource)
        result_json = r.json()
        return (result_json['versionNumber'], result_json['releaseNumber'])


class DMRBaseException(Exception):
    """Base exception for datamosru module."""
    pass


class DMRStatusError(DMRBaseException):
    """For response with error codes
    """
    def __init__(self, response):
        super().__init__()
        self.response = response
