def lcm(listname,size):             
    lowest_common=1        #not needed
    multiplied=1           #needed for loop termination     
    for i in range(size):
       multiplied*=listname[i]         #all numbers of list multiplied
       
    for i in range(max(a),multiplied+1):        #multiple starts from highes number
       for j in range(size):
          if i%listname[j]!=0:                  #terminates if not common multiple
             break
          elif j==size-1:                       #matches for all elements
             lowest_common=i
             return lowest_common


   
#main
a=[]
num=int(input("How many numbers ? "))
for i in range (num):
   a.append(int(input("Enter  number  {}: ".format(i+1))))     #.format replaces the curly braces with variable

print("The LCM of the {} numbers are - ".format(num),lcm(a,num))

