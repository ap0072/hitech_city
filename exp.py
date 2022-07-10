name="kuppala bala mamatha" #change to full name 
d={"egg":"hen","aeroplane":"pilot","bus":"driver"}

def finding_unique_using_dict(name):
    d={}
    print(d)
    
    for i in name:
        print(i)
        if i not in d.keys(): #k,u,p
            d[i]=1  #"k":1
        else:
            d[i]=d[i]+1
    print(d)
# unique(non_veg)

def finding_unique_using_list(name):
    l=[]
    s=set() #

    for i in name:
        l.append(i)
    print("list",l)
    for i in l:
        s.add(i)
    print("set",l)
    count123=[]
    for i in s:
        count123.append(l.count(i))
    print(count123)

def finding_unique_using_string(name):
    for i in name:
        print(f"{i}:{name.count(i)}")

finding_unique_using_list(name)
finding_unique_using_dict(name)
finding_unique_using_string(name)