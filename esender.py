import requests
import smtplib,email,ssl
from api_keys import password,api_key,my_email
import turtle
import os
import pandas as pd
import dataframe_image as dfi


my_email=my_email
password=password


screen=turtle.Screen()

def best_book(date='current',query='hardcover-fiction',api_key=api_key):
    url="https://api.nytimes.com/svc/books/v3/lists"
    query_url = url + "/" + date + "/" + query +".json?"+"api-key=" + api_key
    resp=requests.get(query_url).json()
    num_results=len(resp["results"]['books'])
    rank=[resp["results"]['books'][i]["rank"] for i in range(num_results)]
    amazon_product_url=[resp["results"]['books'][i]["amazon_product_url"] for i in range(num_results)]
    primary_isbn13=[resp["results"]['books'][i]["primary_isbn13"] for i in range(num_results)]
    publisher=[resp["results"]['books'][i]["publisher"] for i in range(num_results)]
    title=[resp["results"]['books'][i]["title"] for i in range(num_results)]
    author=[resp["results"]['books'][i]["author"] for i in range(num_results)]
    categry=[query for i in range(num_results)]
    pub_date=[date for i in range(num_results)]
    
    #getting previous_published_date
    #previous_published_date=resp["results"]['previous_published_date']

    category_dict={"rank":rank,
           "title":title,
           "author":author,
           "category":categry,
           "primary_isbn13":primary_isbn13,
           "publisher":publisher,
           "pub_date":pub_date,
           "amazon_product_url":amazon_product_url}  
       
    return pd.DataFrame(category_dict)


screen.title("The New York Times Best Sellers books")
image=os.path.join("images","nyt.gif")
screen.addshape(image)
turtle.shape(image)

user_answer_1=screen.textinput(title="Fiction or Non Fiction" , prompt=f"What's your prefer? fiction/nonfiction")
user_answer_2=screen.textinput(title="hardcover/e-Book/audio" , prompt=f"What kind of book you prefer? hardcover/e-Book/audio ")
user_choose=user_answer_2+"-"+user_answer_1
best_books=best_book(query=user_choose,api_key=api_key)
best_books.to_csv("output/turtle.csv",index=False)
dfi.export(best_books,"images/nyt_turtle.png")



user_answer_3=screen.textinput(title="email" , prompt=f"Please put your email address here or type exit and find the turtle.csv in output fulder")



screen.exitonclick()


