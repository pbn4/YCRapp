import connexion
import six

from openapi_server.models.companies import Companies  # noqa: E501
from openapi_server.models.company import Company  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server import util

import json

with open('krs.json', 'r') as f:
    krs_json = json.loads(f.read())

def filter_krs_obj(krs):
    out_objs = []

    krs = krs_json['Dataobject']
    for obj in krs:
        out = {}
        out['id'] = obj['id']
        out['url'] = obj['url']
        out['nazwa'] = obj['data']['krs_podmioty.nazwa']
        out['nip'] = obj['data']['krs_podmioty.nip']
        out['regon'] = obj['data']['krs_podmioty.regon']
        out['date_created'] = obj['data']['krs_podmioty.data_dokonania_wpisu']
        out_objs.append(out)

    return out_objs

def companies_get():  # noqa: E501
    """Gets some companies

    Returns a list containing all companies. The list supports paging. # noqa: E501


    :rtype: Companies
    """
    return filter_krs_obj(krs_json)


def companies_id_get(id):  # noqa: E501
    """Gets a company

    Returns a single company for its id. # noqa: E501

    :param id: The company&#39;s id
    :type id: 

    :rtype: Company
    """
    return 'do some magic!'


def companies_post(company=None):  # noqa: E501
    """Creates a company

    Adds a new person to the persons list. # noqa: E501

    :param company: The company to create.
    :type company: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        company = Company.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
