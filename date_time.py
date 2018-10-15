#############################################################
# Date & Time
#############################################################
import datetime
a = datetime.datetime.utcnow()
b = str(a)
print('str(a): {}'.format(str(a))) #2018-05-23 21:23:53.873442
print('str(b): {}'.format(str(b))) #2018-05-23 21:23:53.873442

print('repr(a): {}'.format(repr(a))) #datetime.datetime(2018, 5, 23, 21, 23, 53, 873442)
print('repr(b): {}'.format(repr(b))) #'2018-05-23 21:23:53.873442'

a = [1,2,3,4]
b = 'sample string'

print(str(a))
print(repr(a))

print(str(b))
print(repr(b))
