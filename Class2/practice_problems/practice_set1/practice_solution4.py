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
weighted_grade =w_class_par * class_par + w_ps * ps + w_mid_term * mid_term + w_final * final

#Print out the result
print("Your weighted grade: %s" % weighted_grade)
