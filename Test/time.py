from re import match
from datetime import datetime, timedelta

__author__ = 'Owain'


def do_something():
    for i in range(5):
        match("^\d+?\.\d+?$", 5) is None

print(datetime.now() + timedelta(days=10))

start = datetime.datetime.now()
do_something()
end = datetime.datetime.now()
print("%.2gs" % (end-start))
