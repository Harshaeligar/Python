number=int(input("Enter the number"))
temp= number
reverse=0
while(number>0):
    reminder= number % 10
    reverse= reverse * 10+ reminder
    number=number//10
if(temp == reverse):
    print("nNumber is a palindrome")
else:
    print("Number is not palindrome")
                                        