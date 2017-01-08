# -*- coding: UTF-8 -*-

import requests


class DataMosRu:
    """
    Class to interact with http://data.mos.ru with API.
    """
    # Base URL for API
    site = 'http://api.data.mos.ru'

    def getAPIVersion(self):
        r = requests.get(self.site + u'/version')
        return r.json()['Version']
