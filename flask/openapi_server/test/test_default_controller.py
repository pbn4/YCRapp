# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from openapi_server.models.companies import Companies  # noqa: E501
from openapi_server.models.company import Company  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_companies_get(self):
        """Test case for companies_get

        Gets some companies
        """
        response = self.client.open(
            '/api/companies',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_companies_id_get(self):
        """Test case for companies_id_get

        Gets a company
        """
        response = self.client.open(
            '/api/companies/{id}'.format(id=3.4),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_companies_post(self):
        """Test case for companies_post

        Creates a company
        """
        company = Company()
        response = self.client.open(
            '/api/companies',
            method='POST',
            data=json.dumps(company),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
