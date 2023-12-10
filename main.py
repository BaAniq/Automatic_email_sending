from random import choice

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
print(quote_of_day)
quotes_list.remove(quote_of_day)
with open("Left_quotes.txt", 'w') as left_quotes:
    for quote in quotes_list:
        left_quotes.write(quote)