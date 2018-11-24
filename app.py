from flask import Flask, request
from flask_restful import Resource, Api
from similarity.normalized_levenshtein import NormalizedLevenshtein
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

class Search(Resource):

    def get(self, company_name):
        nl = NormalizedLevenshtein()
        allNames = [(nl.distance(company_name.upper(), a['nazwa']), a['id'], a['nazwa']) for a in companies_arr]
        best_result = sorted(allNames,reverse=True)[-1]
        if best_result[0] > 0.8: #result is bad
            return {'Error':'Company not found!'}
        else:
            return {'Closest Match':best_result}
            

api.add_resource(Company, '/companies/<int:company_id>')
api.add_resource(Companies, '/companies')
api.add_resource(Search, '/search/<string:company_name>')

if __name__ == '__main__':
    app.run(debug=True)
