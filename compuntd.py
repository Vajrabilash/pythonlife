## task 5 on python full stack development (pythonlife)
#compound intrest and simple intrest

    #compound intrest
amount=float(input("Enter the principle amount: "))  # collecting the principle amount
rate=float(input("Enter the rate of intrest: "))    # collecting the intrest rate
years=float(input("Enter the no.of years: "))     # collecting the no.of years

ci = round(amount*pow((1+rate/100),years))      #formula to calculate compound intrest
print("the compound intrest for ",amount, "is ",ci) 
