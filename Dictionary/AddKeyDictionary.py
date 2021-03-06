dictionary = {5:10,6:10}
print("before update",dictionary)
key = int(input("enter the kay value"))
value = int (input("enter the value"))
dictionary.update({key:value})
print("after update",dictionary)
