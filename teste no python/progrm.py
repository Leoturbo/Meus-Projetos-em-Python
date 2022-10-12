from calendar import week
import sys
from datetime import*
from dateutil.relativedelta import *
now = datetime.now()
print(now)

now = now + relativedelta(months=1, weeks=1, hour=10)

print(sys.argv)
print(sys.argv[0])#program name
print(sys.argv[1])#first arg