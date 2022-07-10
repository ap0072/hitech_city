# Non_veg to Veg 

non_veg=["egg","chicken","mutton","prawns"] #0,1,2,3

veg=["pappu","palak","drumstick","sambar"]

print("Items in Non_veg menu:")
for i in non_veg:
    print(i)

print("length of list non_veg: ",len(non_veg))

print("Accessing the elements in list using index")

print("printing prawns",non_veg[0])

for i in range(len(non_veg)):
    print(i)
    print(f"i like non-veg items,as wel;l as veg items {non_veg[i]}")


for i in range(len(non_veg)+1): 
    try:
        non_veg[i]=veg[i] #updating the elements in non_veg list  with  elements in veg list using index value of list
    except:
        print("error came due to wrong index position")

print("Hey! today is saturday only veg is available.")
print(non_veg)

