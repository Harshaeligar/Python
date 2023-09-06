number=[1,5, 4, 4 , 1, 5, 2, 6]
freq={}
for i in number:
    if(i in freq):
        freq[i]+=1
    else:
         freq[i]=1
for key,value in freq.items():
    print("%d : %d"%(key,value))
