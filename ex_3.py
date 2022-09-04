hoursInput=input('Enter Hours:')
rateInput=input('Enter rate:')
try:
    hoursVar=float(hoursInput)
    rateVar=float(rateInput)
except:
    print('Error: Wrong input')
    quit()
if hoursVar > 40:
    print('Pay: ', (hoursVar*rateVar)*1.5)
else:
    print('Pay: ', hoursVar*rateVar)