inum=int(input("enter a number:"))
freq={}
orignal=inum
reverse=0
while(inum>0):
    digit=inum%10
    if(digit in freq):
        freq[digit]+=1
    else:
