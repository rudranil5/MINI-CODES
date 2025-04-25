def hcf(listname,size):
    factor=1    #1 is least common factor
    for i in range (2,listname[0]+1):       #factor is always <= the number
        for j in range(0,size):              
            if listname[j]%i!=0:            #checks list elements are not factor
                break
            elif j==size-1:                 #if i divides all elements of lists
                factor=i

    return factor

#main
a=[]
num=int(input("How many numbers?  "))
for i in range(num):   
    a.append(int(input("Enter  number {} : ".format(i+1))))     #.format puts the item in the curly braces
    
print("The GCD/HCF of the {} numbers are - ".format(num),hcf(a,num))

