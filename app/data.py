import requests
from pprint import pprint
from api_keys import api_key
import pandas as pd
import time

def best_book(date='current',query='hardcover-fiction',api_key=api_key):
    url="https://api.nytimes.com/svc/books/v3/lists"
    query_url = url + "/" + date + "/" + query +".json?"+"api-key=" + api_key
    resp=requests.get(query_url).json()
    num_results=len(resp["results"]['books'])
    rank=[resp["results"]['books'][i]["rank"] for i in range(num_results)]
    primary_isbn13=[resp["results"]['books'][i]["primary_isbn13"] for i in range(num_results)]
    publisher=[resp["results"]['books'][i]["publisher"] for i in range(num_results)]
    title=[resp["results"]['books'][i]["title"] for i in range(num_results)]
    author=[resp["results"]['books'][i]["author"] for i in range(num_results)]
    categry=[query for i in range(num_results)]
    pub_date=[date for i in range(num_results)]
   

    category_dict={"rank":rank,
           "primary_isbn13":primary_isbn13,
           "publisher":publisher,
           "title":title,
           "author":author,
           "category":categry,
           "pub_date":pub_date}  
       
    return pd.DataFrame(category_dict)

