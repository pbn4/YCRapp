from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

from krs import get_krs_obj

companies_arr = get_krs_obj()

class Company(Resource):
    def get(self, company_id):
        print(company_id)
        for obj in companies_arr:
            if int(obj['id']) == company_id:
                return obj
        # TODO throw error

class Companies(Resource):
    def get(self):
        return companies_arr

api.add_resource(Company, '/companies/<int:company_id>')
api.add_resource(Companies, '/companies')

if __name__ == '__main__':
    app.run(debug=False)
