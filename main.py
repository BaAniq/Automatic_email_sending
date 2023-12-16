from random import choice
from datetime import datetime
from smtplib import SMTP

my_email = "dimitoret@gmail.com"
password = "aptz giun elit jebb"


try:
    with open('Left_quotes.txt', 'r+') as left_quotes:
        quotes_list = left_quotes.readlines()
except FileNotFoundError:
    with open('quotes.txt') as quotes:
        quotes_list = quotes.readlines()
    with open("Left_quotes.txt", 'w') as left_quotes:
        for quote in quotes_list:
            left_quotes.write(quote)

quote_of_day = choice(quotes_list)
quotes_list.remove(quote_of_day)
with open("Left_quotes.txt", 'w') as left_quotes:
    for quote in quotes_list:
        left_quotes.write(quote)

today = datetime.now()
weekday = today.weekday()
if weekday == 5:
    with SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs='dimitoret@op.pl', msg=f'Subject:Quote of the day \n\n '
                                                                                f'This is the quote of the day: \n'
                                                                                f' {quote_of_day} ')
