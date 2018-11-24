from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

import json
from krs import get_krs_obj

companies_arr = get_krs_obj()

class Company(Resource):
    def get(self, company_id):
        print(company_id)
        for obj in companies_arr:
            if int(obj['id']) == company_id:
                return obj
        # TODO throw error

    def put(self, company_id):
        companies[company_id] = request.form['data']
        return {company_id: companies[company_id]}

class Companies(Resource):
    def get(self):
        return companies_arr

api.add_resource(Company, '/companies/<int:company_id>')
api.add_resource(Companies, '/companies')

if __name__ == '__main__':
    app.run(debug=True)
