#!/usr/bin/python3
# -*- coding: utf-8; mode: python -*-
__version__ = "1.0"
__date__ = "20170329"
__author__ = "kthoden@mpiwg-berlin.mpg.de"

import json

JSON_DATA = "../data/impactomatrix.json"

IMP_TEMPLATE = "(%s:Impact {slug: '%s', name: '%s', name_de: '%s', description: '%s'})"
FACTOR_TEMPLATE = "(%s:Factor {slug: '%s', name: '%s', name_de: '%s'})"
CRITERIA_TEMPLATE = "(%s:Criterion {slug: '%s', name: '%s', name_de: '%s'})"
AFFECT_TEMPLATE = "(%s)-[:AFFECTS]->(%s)"
RATE_TEMPLATE = "(%s)-[:RATES]->(%s)"

if __name__ == '__main__':
    with open(JSON_DATA, "r") as json_data_file:
        json_object = json.load(json_data_file)

    CIPHER_LIST = []
    RELATIONS = []

    impact_areas = json_object['impacts']
    factors = json_object['factors']
    criteria = json_object['criteria']

    for area in impact_areas:
        tmp_template = IMP_TEMPLATE % (area['slug'], area['slug'], area['name'], area['name_de'], area['description'])
        CIPHER_LIST.append(tmp_template)
        for link in area['links']:
            if link.startswith("c"):
                tmp_template = RATE_TEMPLATE % (link, area['slug'])
            elif link.startswith("f"):
                tmp_template = AFFECT_TEMPLATE % (link, area['slug'])
            RELATIONS.append(tmp_template)

    for factor in factors:
        tmp_template = FACTOR_TEMPLATE % (factor['slug'], factor['slug'], factor['name'], factor['name_de'])
        CIPHER_LIST.append(tmp_template)

    for criterion in criteria:
        tmp_template = CRITERIA_TEMPLATE % (criterion['slug'], criterion['slug'], criterion['name'], criterion['name_de'])
        CIPHER_LIST.append(tmp_template)

    QUERY_LIST = CIPHER_LIST + RELATIONS

    CIPHER_STRING = "CREATE " + ", ".join(QUERY_LIST)

    print(CIPHER_STRING)
# finis
