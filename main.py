import datetime
import time
# from controller import Control

# Control.run()

test1 = time.time()
print(f'{test1} - {type(test1)} второй тест, прогон по конвертерам')
#time.struct_time(tm_year=2023, tm_mon=2, tm_mday=13, tm_hour=19, tm_min=30, tm_sec=45, tm_wday=0, tm_yday=44, tm_isdst=0) - localtime
print(f'{time.localtime(test1).tm_mday}.{time.localtime(test1).tm_mon}.{time.localtime(test1).tm_year} - localtime')

print('---')
line = ""
while True:
    try:
        line = "{in1}\n{in2}".format(in1=line, in2=input())
    except EOFError: 
        break

print('------')
print(line)