my_set = { 1,2,3,43,4,5,5,6,7,7,7,8,8,8,8,"gaurav","Pune",
            ("dbda,hpcsa","diot","dac"),frozenset({"dbda,hpcsa","diot","dac"})
          }

# print( len(my_set))
my_subset1 = {100,200,300}
my_subset2 = {1,2,3,300}

# print(my_set) 

# print(my_set.intersection(my_subset1))
# print(my_set.intersection(my_subset2))

# print(frozenset({"dbda,hpcsa","diot","dac"}) in my_set )
# print(("dbda,hpcsa","diot","dac") in my_set)
# print("dbda" in my_set)
# print("Pune" in my_set)


# print(my_set.isdisjoint(my_subset1))
# print(my_set.isdisjoint(my_subset2))

# print(my_set.issuperset(my_subset1))

# print(my_subset1.issubset(my_set))
# print(my_subset2.issubset(my_set))

# print(my_set.union(my_subset1))
# print("actual set:",my_set)

# print(my_set.intersection(my_subset2))
#print(my_subset1.difference(my_subset2))

# print(my_subset1.symmetric_difference(my_subset2))

# my_copy=set()
# print(my_copy)
# my_copy=my_subset2.copy()
# print(my_copy)
# print(my_subset1)
# print(my_subset2)
# print(my_subset1.update(my_subset2))
# print(my_subset1)

# print(my_subset1.intersection_update(my_subset2))
# print(my_subset1)
# print(my_subset1)
# print(my_subset2)
# print(my_subset1.difference_update(my_subset2))
# print(my_subset1)
# my_subset3= {1000,2000,300}
# my_subset4 = {40,50}
# print(my_subset1.intersection_update(my_subset2, my_subset3,my_subset4))
# print(my_subset1)

print(my_subset1)
print(my_subset2)
# print(my_subset1.symmetric_difference_update(my_subset2))
# print(my_subset1)

copy_set= set()
# copy_set=my_subset2.copy()
#copy_set.add(50000)
# # print(copy_set)
# copy_set = set()
# copy_set = my_subset1.copy()
# copy_set.remove(200)
# print(copy_set)
# copy_set = set()
# copy_set = my_subset1.copy()
# copy_set.discard(200)
# #copy_set.discard(20)
# print(copy_set)
#print(copy_set)




copy_set.add(789654)
copy_set.add(11111)
copy_set.add(3333)
copy_set.add(99999)
print(copy_set)
# copy_set.pop()
# print(copy_set)
# print(copy_set)
copy_set.clear()
print(copy_set)

