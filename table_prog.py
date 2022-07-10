#Table Program 

a=int(input("Enter your lucky number: "))

for i in range(a):
    print(i) #just printing value of i

print()
for j in range(1,10):
    print(j*j) #printing the square of i--> i*i,

print()
for k in range(a): #loop inside a loop                  k l
                                                        #0 1,2,3,4,5,6,7,8,9 
    print("Table numbers of :",k)
    for l in range(1,10):
        print(k*l)  # Multiplying two int values k and l
    print()   

     
print()
count=0
for l in range(a): #loop inside a loop 7    
    '''L M N
                                            0 0 0,1,2,3,4,5,6
                                            0 1 0,1,2,3,4,5,6
                                            0 2 0,1,2,3,4,5,6
                                            0 3 0,1,2,3,4,5,6
                                            0 4 0,1,2,3,4,5,6
                                            0 5 0,1,2,3,4,5,6
                                            0 6 0,1,2,3,4,5,6
                                            1 0 0,1,2,3,4,5,6
                                            1 1 0,1,2,3,4,5,6
                                            1 2 0,1,2,3,4,5,6
                                            1 3 0,1,2,3,4,5,6
                                            1 4 0,1,2,3,4,5,6
                                            1 5 0,1,2,3,4,5,6
                                            1 6 0,1,2,3,4,5,6
'''
    for m in range(a): #7
        for n in range(a):  #7
            count=count+1

print(f"{a}*{a}*{a}: {count}")