import datetime
import random
day = random.choice(['Εικοστή πέμπτη', 25])
try:
    date = day + ' Μαρτίου'
except TypeError:
    date = datetime.date(1821, 3, day)
else:
    date += ' 1821'
finally:
    print(date)
