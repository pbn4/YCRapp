from flask import Flask, request
from flask_restful import Resource, Api
from similarity.normalized_levenshtein import NormalizedLevenshtein
from flask_cors import CORS
from fuzzywuzzy import fuzz
from operator import itemgetter

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
        ratios = []
        for obj in companies_arr:
            ratio = fuzz.token_set_ratio(company_name, obj['nazwa'])
            ratios.append((obj, ratio))
        sorted_ratios = sorted(ratios, key=itemgetter(1), reverse=True)
        return [obj for obj, ratio in sorted_ratios[:5]]
            

api.add_resource(Company, '/companies/<int:company_id>')
api.add_resource(Companies, '/companies')
api.add_resource(Search, '/search/<string:company_name>')

if __name__ == '__main__':
    app.run(debug=True)
