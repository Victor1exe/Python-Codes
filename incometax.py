#program to calculate tax (Tax Calculator)
# initialize the constats
TAX_RATE=0.20
STANDAR_DEDUCTION=10000.0
DEPENDENT_DEDUCTION=3000.0

#request the inputs
grossIncome=float(input("Enter the gross income:"))
numDepndents=int(input("Enter the number of dependents:"))

#compute the income tax
taxableIncome= grossIncome - STANDAR_DEDUCTION-DEPENDENT_DEDUCTION* numDepndents
incomeTax=taxableIncome*TAX_RATE

#display the income tax
print("The income tax is $", str(incomeTax))
#checking output for muliple inputs: