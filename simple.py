## task 5 on python full stack development (pythonlife)
#compound intrest and simple intrest

    #simple intrest
amount=float(input("Enter the principle amount: "))  # collecting the principle amount
rate=float(input("Enter the rate of intrest: "))    # collecting the intrest rate
years=float(input("Enter the no.of years: "))     # collecting the no.of years

si = round((amount*rate*years)/100)      #formula to calculate compound intrest
print("the simple intrest for ",amount, "is ",si) 
