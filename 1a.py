marks1=int(input("enter the marks in the firsttest"))
marks2=int(input("enter the marks in the second test"))
marks3=int(input("enter the marks in the third test"))
if(marks1>marks2):
    if(marks2>marks3):
       total=marks1+marks2
    else:
        total=marks1+marks3
elif(marks1>marks3):
    total=marks1+marks2
else:
    total = marks2 + marks3

Avg=total/2
print("The average of the best two test marks is",Avg)