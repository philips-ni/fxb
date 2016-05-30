import pymongo
import urllib
from pymongo import MongoClient
client=MongoClient(host='127.0.0.1',port=27017)
db=client.fxb
companies_collection=db.companies

def get_my_products(user_name):
    all_products = companies_collection.find()
    ret_items = []
    for product in all_products:
        ret_items.append(product)
    return ret_items

def add_company(company_doc):
    companies_collection.insert_one(company_doc)
    
