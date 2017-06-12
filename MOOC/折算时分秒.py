second = int(input())
hour = second//3600
minute = (second-hour*3600)//60
second = second-hour*3600-minute*60
print hour,minute,second
