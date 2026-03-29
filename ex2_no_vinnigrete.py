from datetime import datetime
from random import randint
from time import time


date1=input("please enter date 1  (jj-mm-aaaa) ")  #minimal borne
date2=input("please enter date 2  format (jj-mm-aaaa)")

try:
    dt1_format_epoch = int(datetime.strptime(date1, "%d-%m-%Y").timestamp())
    dt2_format_epoch = int(datetime.strptime(date2, "%d-%m-%Y").timestamp())

except ValueError:
        exit("not in the right format")




if dt1_format_epoch >dt2_format_epoch:  #if i enter date1>date2 the range between them is empty
    temp=dt1_format_epoch
    dt1_format_epoch=dt2_format_epoch
    dt2_format_epoch=temp
middleRandomDate=randint(dt1_format_epoch,dt2_format_epoch)
middleRandomDate=datetime.fromtimestamp(middleRandomDate)
if middleRandomDate.weekday()==0 :
    print( "i havent vinnigrete")
else:
    print( "i have vinnigrete")
