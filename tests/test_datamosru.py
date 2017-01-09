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


def test_getDatasetInfo():
    dmr = DataMosRu('')
    dataset_id = 658
    info = dmr.getDatasetInfo(dataset_id)

    assert 'Id' in info
    assert 'CategoryId' in info
    assert 'CategoryCaption' in info
    assert 'DepartmentId' in info
    assert 'DepartmentCaption' in info
    assert 'Caption' in info
    assert 'Description' in info
    assert 'ContainsGeodata' in info
    assert 'VersionNumber' in info
    assert 'VersionDate' in info
    assert 'ItemsCount' in info
    assert 'Columns' in info

    assert len(info['Columns']) > 0

    assert 'Name' in info['Columns'][0]
    assert 'Caption' in info['Columns'][0]
    assert 'Visible' in info['Columns'][0]
    assert 'Type' in info['Columns'][0]
    assert 'SubColumns' in info['Columns'][0]


def test_getDatasetLen():
    dmr = DataMosRu('')
    dataset_id = 493
    count = dmr.getDatasetLen(dataset_id)
    assert count > 160


def test_getDatasetVersion():
    dmr = DataMosRu('')
    dataset_id = 655
    version, release = dmr.getDatasetVersion(dataset_id)
    assert version >= 4
    assert release >= 110
