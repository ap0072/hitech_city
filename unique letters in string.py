#finding the unique letters in a strings

a="Kuppala Bala Mamatha" #change to full name 
l1=[1,2,3]
dic={'a':0,'b':0}

def unique(a):
    l=[]
    count_a=0
    count_b=0
    for i in a:
        print(i)
        if i=='a':
            count_a+=1
        elif i=='b':
            count_b+=1
        else:
            pass
        
    print(count_a,count_b)

unique(a)
unique("Chaluvadi Prasanth Kumar")