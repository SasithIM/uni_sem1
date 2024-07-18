limits=[30,30,30,90,0]
rates = [30,7,5,8,25]
fixed_charges=[400,150,100,850,500] 
bill=0

usage = int(input()) #45

if usage > 60:
    bill+=60*42-30*30-30*37

for i in range(5):
    bill += usage * rates[i] + fixed_charges[i]
    usage -= limits[i]
    if not usage>0:
        break
print(bill)