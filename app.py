from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

import json
from krs import get_krs_obj

companies = get_krs_obj()

class Company(Resource):
    def get(self, company_id):
        return {company_id: companies[company_id]}

    def put(self, company_id):
        companies[company_id] = request.form['data']
        return {company_id: companies[company_id]}

class Companies(Resource):
    def get(self):
        return json.dumps(companies)

api.add_resource(Company, '/<string:company_id>')
api.add_resource(Companies, '/companies')

if __name__ == '__main__':
    app.run(debug=False)
