age = 35
pointcard=True
count=5
if (age < 18):
    print('チケットを売ることはできません')
elif ((60 <= age) or ((pointcard == True) and (count == 5))):
    print('チケットは1000円です')
else:
    print('チケットは1800円です')
