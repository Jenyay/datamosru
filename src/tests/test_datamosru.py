# -*- coding: UTF-8 -*-

import sys



def test_api_version():
    print(sys.path)
    from datamosru import DataMosRu
    dmr = DataMosRu()
    version = dmr.getAPIVersion()
    assert version == 1
