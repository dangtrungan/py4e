try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
except:
    print("Error, please enter numeric input")
pay = hours * rate
if hours > 40:
    pay += (hours - 40) * rate * 0.5
print("Pay:", pay)
