#Assign the five number
n1=95
n2=830
n3=225
n4=490
n5=991

#Calculate sum, average, variance
total=n1+n2+n3+n4+n5
avg_num=total/5
var=((n1-avg_num)**2+(n2-avg_num)**2+(n3-avg_num)**2+(n4-avg_num)**2+(n5-avg_num)**2)/5

#Print out the result
print("Your result is:")
print("Total: %s" % total)
print("Mean: %s" % avg_num)
print("Variance: %s" % var)