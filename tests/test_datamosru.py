# -*- coding: UTF-8 -*-

import requests

from datamosru import DataMosRu, DMRStatusError
# from secret import API_KEY


def test_api_version():
    dmr = DataMosRu('')
    version = dmr.getAPIVersion()
    assert version == 1


def test_request_invalid_resource():
    dmr = DataMosRu('')
    try:
        dmr.request('invalid_resource')
    except DMRStatusError as e:
        assert e.response.status_code == requests.codes.not_found
    else:
        assert False


def test_getDatasets_01():
    dmr = DataMosRu('')
    datasets_iter = dmr.getDatasets()
    assert len(list(datasets_iter)) > 680


def test_getDatasets_02():
    dmr = DataMosRu('')
    dmr.request_items_portion = 100
    datasets_iter = dmr.getDatasets()
    assert len(list(datasets_iter)) > 680
