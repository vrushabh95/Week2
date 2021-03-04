list=[]
tupleX=()

for x in range(5):
    num=(int(input("Enter the value ")))
    list.insert(x,num)

tupleX=tuple(list)
print("Elements in list=",list)
print("Elements in tuples=",tupleX)