# %%
import requests
from pprint import pprint
from api_keys import api_key
import pandas as pd
import time


#Function for finding all list_name in NYT_API
def list_name_maker(url="https://api.nytimes.com/svc/books/v3/lists/names.json?"+"api-key="+api_key):
    response_=requests.get(url).json()
    result_length=response_["num_results"]
    list_name=[response_["results"][i]["list_name"] for i in range(59)]
    list_name_encoded=[response_["results"][i]["list_name_encoded"] for i in range(59)]
    oldest_published_date=[response_["results"][i]["oldest_published_date"] for i in range(59)]
    newest_published_date=[response_["results"][i]["newest_published_date"] for i in range(59)]
    updated=[response_["results"][i]["updated"] for i in range(59)]
    list_dict={"list_name":list_name,
               "list_name_encoded":list_name_encoded,
               "oldest_published_date":oldest_published_date,
               "newest_published_date":newest_published_date,
               "updated":updated}                      
                                    
                                    
    list_df=pd.DataFrame(list_dict)
    #list_df.to_csv("output/NYT_list.csv",index=False)
    return list_df

#list_name_df=list_name_maker()

#Function for getting Best Sellers List details of one category and making a 
#dataframe and finding previous_published_date

def best_book(date='current',query='hardcover-fiction',api_key=api_key):
    url="https://api.nytimes.com/svc/books/v3/lists"
    query_url = url + "/" + date + "/" + query +".json?"+"api-key=" + api_key
    resp=requests.get(query_url).json()
    num_results=len(resp["results"]['books'])
    rank=[resp["results"]['books'][i]["rank"] for i in range(num_results)]
    primary_isbn10=[resp["results"]['books'][i]["primary_isbn10"] for i in range(num_results)]
    primary_isbn13=[resp["results"]['books'][i]["primary_isbn13"] for i in range(num_results)]
    publisher=[resp["results"]['books'][i]["publisher"] for i in range(num_results)]
    title=[resp["results"]['books'][i]["title"] for i in range(num_results)]
    author=[resp["results"]['books'][i]["author"] for i in range(num_results)]
    categry=[query for i in range(num_results)]
    pub_date=[date for i in range(num_results)]
    
    #getting previous_published_date
    previous_published_date=resp["results"]['previous_published_date']

    category_dict={"rank":rank,
           "primary_isbn10":primary_isbn10,
           "primary_isbn13":primary_isbn13,
           "publisher":publisher,
           "title":title,
           "author":author,
           "category":categry,
           "pub_date":pub_date}  
       
    return pd.DataFrame(category_dict),previous_published_date



#Function for getting 14 published date and dataframes and concatenating them on 1 dataframe
def best_ctg_maker(query='hardcover-fiction',api_key=api_key):
    dfs=[]
    previous_dates=["current"]
    for i in range(14):
        df=best_book(date=previous_dates[i],query=query)
        dfs.append(df[0])
        previous_dates.append(df[1])
        time.sleep(10)
    return pd.concat(dfs)


# Function for concatenating all categories dataframes in one
def best_book_df_maker():
    costum_list=["Hardcover Fiction","Hardcover Nonfiction","E-Book Fiction","E-Book Nonfiction",
             "Audio Fiction","Audio Nonfiction","Combined Print Fiction","Combined Print Nonfiction"]

    Best_books=[]
    for i in costum_list:
        df=best_ctg_maker(query=i)
        Best_books.append(df)
        time.sleep(10)
    #last dataframe concatenating     
    Best_books_df=pd.concat(Best_books)
    #Best_books_df.to_csv("output/best_book_list.csv",index=False)
    return Best_books_df



best_book_df=best_book_df_maker()