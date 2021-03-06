dict1 = {1:10,2:20}
dict2 = {3:30,4:40}
dict3 = {5:50,6:60}
fulldictionary = {}
for d in (dict1,dict2,dict3):
    fulldictionary.update(d)
print(fulldictionary)