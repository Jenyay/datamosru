# -*- coding: UTF-8 -*-

from datamosru import DataMosRu


def test_api_version():
    dmr = DataMosRu()
    version = dmr.getAPIVersion()
    assert version == 1
