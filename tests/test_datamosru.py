# -*- coding: UTF-8 -*-

import requests

from datamosru import DataMosRu, DMRStatusError
# from secret import API_KEY


def test_api_version():
    dmr = DataMosRu()
    version = dmr.getAPIVersion()
    assert version == 1


def test_request_invalid_resource():
    dmr = DataMosRu()
    try:
        dmr.request('invalid_resource')
    except DMRStatusError as e:
        assert e.response.status_code == requests.codes.not_found
    else:
        assert False


def test_getDatasetsList_01():
    dmr = DataMosRu()
    datasets_iter = dmr.getDatasetsList()
    assert len(list(datasets_iter)) > 680


def test_getDatasetsList_02():
    dmr = DataMosRu()
    dmr.request_items_portion = 100
    datasets_iter = dmr.getDatasetsList()
    assert len(list(datasets_iter)) > 680


def test_getDatasetInfo():
    dmr = DataMosRu()
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
    dmr = DataMosRu()
    dataset_id = 493
    count = dmr.getDatasetLen(dataset_id)
    assert count > 160


def test_getDatasetVersion():
    dmr = DataMosRu()
    dataset_id = 655
    version, release = dmr.getDatasetVersion(dataset_id)
    assert version >= 4
    assert release >= 110


def test_getDataset_2039():
    dmr = DataMosRu()
    dataset_id = 2039

    dataset_len = dmr.getDatasetLen(dataset_id)
    items = list(dmr.getDataset(dataset_id))

    assert len(items) == dataset_len

    item = items[0]
    assert item['global_id'] is not None
    assert item['Kod_okato'] is not None
    assert item['Name'] is not None
    assert item['Latin_name'] is not None
    assert item['Type'] is not None
    assert item['Kod'] is not None


def test_getDataset_2044():
    dmr = DataMosRu()
    dataset_id = 2044

    dataset_len = dmr.getDatasetLen(dataset_id)
    items = list(dmr.getDataset(dataset_id))

    assert len(items) == dataset_len

    item = items[0]
    assert item['global_id'] is not None
    assert item['UM_NAMEF'] is not None
    assert item['UM_CODE'] is not None
    assert item['UM_NAMES'] is not None
    assert item['UM_TRANS'] is not None
    assert item['UM_KLADR'] is not None
