import smtplib
from api_keys import password

my_email="pink.cookiesender@gmail.com"
password=password


with smtplib.SMTP("smtp.gmail.com") as connection:

    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email, to_addrs="lale.sfzd@gmail.com",msg="Subject:hello\n\n this is the body")
    

