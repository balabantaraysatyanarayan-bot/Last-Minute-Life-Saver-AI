#------- student biodata -----------!
name = input ("enter your name :")
print ("my name is .", name)
school = input ("enter your school name :")
print ("my school name .", school)
classes = int (input ("enter your class name :"))

Roll_No = int (input("enter your roll.no. :"))
print ("my roll no. ", Roll_No)

#--------- student marksheet --------!



sub_name = ["FLO", "SLE", "TLS", "SSH", "GEO"]
print ("our subject :",sub_name )

#------- student marks ------!
marks = {}
#student marks of subject wise.... !
marks ["FLO"] = int (input ("enter the marks :"))
marks ["SLE"] = int (input ("enter the marks :"))
marks ["TLS"] = int (input ("enter the marks :"))
marks ["SSH"] = int (input ("enter the marks :"))
marks ["GEO"] = int (input ("enter the marks :"))

for key, value in marks.items():
    print (key, "=", value)


#-------- student total marks ------!
total = 0
for x in marks.values():
    total += x
print ("student total marks :",total)


#----------student result system --------!
average = total / len(marks)
if (average >= 89):
    grade = "A"
elif (average >= 78):
    grade = "B"
elif (average >= 68):
    grade = "C"
else:
    grade = "D"

print ("total average :", average)
print ("your grade is :",grade)



#------result-----!
print ("total marks of student :", total)
print ("average marks of student :",average)
print ("final your grade is :",grade)
