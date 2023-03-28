import math
answer_1="investment"
answer_2="bond"
answer_3="simple"
answer_4="compound"
print ("Investment- To calculate the amount of interest you'll earn on your investment.")
print ("Bond - To calculate the amount you'll have to pay on a home loan.")
print (" ")
print ("Enter either 'Investment' or 'Bond' from the menu above to proceed:")
print(" ")
def main():
    investment_or_bond= input ("Please enter Investment or Bond-").lower()
    if investment_or_bond==answer_1:
        print("Thank you for choosing Investment")
        print(" ")
        s_or_c= str(input("Now please enter simple or compound interest-")).lower()
        if s_or_c== answer_3:
            print("Thank you for choosing simple interest")
            principle=0
            rate=0
            time=0
            while principle<=0:
                principle= float(input(" please enter the deposit amount-"))
            while rate<=0:
                rate= int(input(" please enter the rate of interest-"))
            while time<=0:
                time= int(input(" please enter the no of years-"))
            print (principle)
            print (rate)
            print (time)
            A = principle*(1 + rate/100*time)
            print ("Total amount will be £{}" .format (A))
        if s_or_c== answer_4:
            print("thank you for choosing compound interest")
            principle=0
            rate=0
            time=0
            while principle<=0:
                principle= float(input(" please enter the deposit amount-"))
            while rate<=0:
                rate= int(input(" please enter the rate of interest-"))
            while time<=0:
                time= int(input(" please enter the no of years-"))
            print (principle)
            print (rate)
            print (time)
            A = principle * pow((1+rate/100),time)
            print ("Total amount will be £{}" .format (A))
    if investment_or_bond==answer_2:
        print("thank you for choosing bond")
        present_value=0
        rate=0
        term=0
        while present_value<=0:
            present_value=float(input("please enter present value of the house-"))
        while rate<=0:
            rate=float(input("please enter interest rate-"))
        while term<=0:
            term=float(input("please enter number of months plan to repay-"))
        print(present_value)
        print(rate)
        print(term)
        r=(rate/100/12 * present_value)/(1 - (1 + rate/100/12)**(-term))
        print ("Monthly repayment will approximate £{}" .format (r))
        exit()
    if investment_or_bond!= answer_1 or answer_2:
        print ("Invalid entry- Please enter either investment or bond")
    repeat=input(" Do you want to try again?").lower()
    if repeat=="yes":
        main()
    else:
        print ("Thank you GoodBye")
        exit ()
main()