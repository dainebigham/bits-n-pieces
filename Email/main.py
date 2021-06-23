import smtplib
import random as r
import datetime as dt

with open('quotes.txt', 'r') as f:
    quotes = f.readlines()

quote = r.choice(quotes)

email = 'testdaine@gmail.com'
password = ''

now = dt.datetime.now()
today = now.weekday()

if today == 1:
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email, 
            to_addrs='daine.bigham@gmail.com', 
            msg=f'Subject:Monday Motivational Quote\n\n{quote}')