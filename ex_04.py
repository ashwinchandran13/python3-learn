def computpay(hour, rate):
    if hour > 40:
        return (hour * rate) * 1.5
    else:
        return hour * rate

hourInput = input('Enter Hours:')
rateInput = input('Enter rate:')

try:
    hourVar = float(hourInput)
    rateVar = float(rateInput)
except:
    print('Error: Invalid Input')
    quit()

pay = computpay(hourVar, rateVar)
print('Pay', pay)