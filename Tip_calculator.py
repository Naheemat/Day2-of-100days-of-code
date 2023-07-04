#Greeting
print('Welcome to my amazing tip calculator!')
#User's total bill input
Total_bill = float(input('How much is your total bill? $'))
#Input 10, 12 or 15 depending on the amount of tip you want.
tip = int(input('What percentage tip would you like to give? 10, 12 or 15 \n'))
#How many people are to share the total bill.
no_of_people = int(input('How many people are to split the bill? \n'))
#To get the tip percentage
tip_percentage =  Total_bill * (1 + tip/100)
#To know the amount to be paid by each individual.
tip_per_person = (tip_percentage / no_of_people)
#To round up the final tip to be paid by each person to 2 decimal places.
final_amount = '{:.2f}'.format(tip_per_person)
#To print the final amount to be paid by each individual
print('Each person should pay ${}'.format(final_amount))
print('Thanks for using my Tip calculator.')