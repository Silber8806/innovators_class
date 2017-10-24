# Problems created by Hanying Liu, Brandeis University 2018 Finance Masters.

#1 Write a program to calculate the daily,weekly and monthly payment based on the
#given hours, rate per hour payment.
#(assume he has to work 5 day a week and 22 day a month)
#Hour per day:6
#Rate:22.5
#Pay ?

rate_per_hour=22.5
hour_per_day=6
#Calculate daily, weekly, monthly payment
daily_payment=rate_per_hour * hour_per_day
weekly_payment=daily_payment * 5
monthly_payment=daily_payment * 22
#Print out the result
print("Your payment is:")
print("Daily payment: %s" % daily_payment)
print("Weekly payment: %s" % weekly_payment)
print("Monthly payment: %s" % monthly_payment)

#2 There are five number, 95, 830, 225, 490, 991
#Print the mean, sum and variance of these five number.
#(Hint: The formula for variance: The average of the squared differences from the Mean.)

#Assign the five number
n1=95
n2=830
n3=225
n4=490
n5=991
#Calculate sum, average, variance
total=n1+n2+n3+n4+n5
avg_num=total/5
var=((n1-avg_num)**2+(n2-avg_num)**2+(n3-avg_num)**2+(n4-avg_num)**2+(n5-avg_num)*
#Print out the result
print("Your result is:")
print("Total: %s" % total)
print("Mean: %s" % avg_num)
print("Variance: %s" % var)

#3 Write a program to calculate the perimeter and the area of the regtangular.
#The program should start with asking the users input of length and width of the regtangular.
#(Hint:To ask for a user's input for length, you could use the function:
#length=input("Enter the length of the regtangular: ")
#This line asks for user to input the length and store it in the length variable.

#ask the user to type in length and width
length=input("Enter the length of the regtangular: ")
width=input("Enter the width of the regtangular: ")
#Calculate perimeter, area
perimeter =length +width
area =length * width
#Print out the result
print("Your result is:")
print("Perimeter: %s" % perimeter)
print("Area: %s" % area)

#4 Adele is taking the Python Class. Please write a program to calculate the weighted grade as the final grade for her.
#The weights for the student final grades are:
#Class participation: w_class_par=0.10
#Problem Sets: w_ps=0.15
#Mid-term Exam: w_mid-term=0.25

#assign the grade weight variables
w_class_par=0.10
w_ps=0.15
w_mid_term=0.25
w_final=0.5
#ask the user to different grades
class_par=input("Enter your class participation grade: ")
ps=input("Enter your problem set grade: ")
mid_term=input("Enter your mid-term exam grade: ")
final=input("Enter your final exam grade: ")
#Calculate weighted grade
weighted_grade =w_class_par * class_par + w_ps * ps + w_mid_term * mid_term + w_f
#Print out the result
print("Your weighted grade: %s" % weighted_grade)


