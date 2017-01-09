# -*- coding: UTF-8 -*-

import requests


class DataMosRu:
    """
    Class to interact with http://data.mos.ru with API.
    """
    # Base URL for API
    site = 'http://api.data.mos.ru/'

    def __init__(self, api_key):
        self.api_key = api_key

    def request(self, resource, **kwargs):
        r = requests.get(self.site + resource, params=kwargs)

        if r.status_code != requests.codes.ok:
            raise DMRStatusError(r)

        return r

    def getAPIVersion(self):
        r = self.request('version')
        return r.json()['Version']


class DMRBaseException(Exception):
    """Base exception for datamosru module."""
    pass


class DMRStatusError(DMRBaseException):
    """For response with error codes
    """
    def __init__(self, response):
        super().__init__()
        self.response = response
