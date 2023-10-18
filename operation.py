my_string = "ICC T20 2022 WC"
my_list=['I', 'C', 'C', ' ', 'T', '2', '0', ' ', '2', '0', '2', '2', ' ', 'W', 'C']
my_tuple=('I', 'C', 'C', ' ', 'T', '2', '0', ' ', '2', '0', '2', '2', ' ', 'W', 'C')
my_range = range(1,5,1)
#print(my_range)

# print("The operations in the following table are defined on Mutable/Immutable sequence types")
# print("--------------------------------------------------------------------------")


# print("x in s -- True if an item of s is equal to x, else False")
#x= "C"
# print(x in my_string)
# print(x in my_list)
# print(x in my_tuple)
# print(1 in my_range)

# print("x not in s -- False if an item of s is equal to x, else True")
# x= "C"
# print(x not in my_string)
# print(x not in my_list)
# print(x not in my_tuple)
# print(7 not in my_range)

# print("s+t -- 	the concatenation of s and t")
# list_t= ['A','U','S','T','R','A','L','I','A']
# tuple_t = ('A','U','S','T','R','A','L','I','A')
# string_t = "Australia"

# print(my_string + string_t)
# print(my_list+list_t)
# print(my_tuple+tuple_t)
# print(my_range + my_range ) # TypeError: unsupported operand type(s) for +: 'range' and 'range'


#print("s * n or n * s -- 	equivalent to adding s to itself n times")
# n = 2 
# print(my_string * n)
# print(my_list*n)
# print(my_tuple*n)
# print(my_range *n ) # TypeError: unsupported operand type(s) for *: 'range' and 'range'


# print("s[i] -- ith item of s, origin 0")
# print(my_string[1])
# print(my_list[1])
# print(my_tuple[1])
# print(my_range[1])


# print("s[i:j] -- slice of s from i to j(Exclusive) and step 1 ")
# print(my_string[1:10])
# print(my_list[1:10])
# print(my_tuple[1:10])
 #print(my_range[1:10])

# print("s[i:j:k] -- 	slice of s from i to j with step k")
# print(my_string[1:10:2])
# print(my_list[1:10:2])
# print(my_tuple[1:10:2])


# print("len(s) -- length of s")
# print(len(my_string))
# print(len(my_list))
# print(len(my_tuple))
# print(len(my_range))



# print("min(s) -- smallest item of s ")
# print(min(my_string))
# print(min(my_list))
# print(min(my_tuple))
# print(min(my_range))

# print(min(my_string).isspace())
# print(min(my_list).isspace())
# print(min(my_tuple).isspace())


# print("max(s) -- largest item of s ")
# print(max(my_string))
# print(max(my_list))
# print(max(my_tuple))
# print(max(my_range))


# print("s.index(x[, i[, j]]) -- 	index of the first occurrence of x in s (at or after index i and before index j)")
# print(my_string.index('C'))
# print(my_list.index('C'))
# print(my_tuple.index('C'))
# print(my_range.index(1))



#print("s.count(x) -- 	total number of occurrences of x in s")
# print(my_string.count('C'))
# print(my_list.count('C'))
# print(my_tuple.count('C'))
# print(my_range.count(1))


# print("s[i] = x -- 	item i of s is replaced by x")
#my_string[1] = 'T'  # TypeError: 'str' object does not support item assignment 
# my_list[1] =  "G"
# #my_tuple[1] = "G" # TypeError: 'tuple' object does not support item assignment
# #my_range[1] = 1 # TypeError: 'range' object does not support item assignment
# print(my_list)

# print("s[i:j] = t -- slice of s from i to j is replaced by the contents of the iterable t ");
#my_string[1:3] = ["G","A"]  # TypeError: 'str' object does not support item assignment 
my_list[1:3] =   ["G","A"]
#my_tuple[1:3]  = ["G","A"] # TypeError: 'tuple' object does not support item assignment
#my_range[1] = [1,2] # TypeError: 'range' object does not support item assignment
print(my_list)