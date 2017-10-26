#Assign the variables
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