import connexion
import six

from openapi_server.models.companies import Companies  # noqa: E501
from openapi_server.models.company import Company  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server import util

import json

with open('krs.json', 'r') as f:
    krs_json = json.loads(f.read())

krs = krs_json['Dataobject']

def companies_get():  # noqa: E501
    """Gets some companies

    Returns a list containing all companies. The list supports paging. # noqa: E501


    :rtype: Companies
    """
    return krs


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
