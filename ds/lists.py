### Lists / arrays 
# List are ordered , mutable 
numbers = [1,2,3,4,5,6,7]
mixed = ["hello", 12 , 3.9, True]
empty_list = [] 

# print(numbers , mixed , empty_list)
# print(len(numbers) , len(mixed) , len(empty_list))

# Accessing an array (index begins at 0)
first_item = numbers[0]
print(first_item)
last_item = numbers[-1]
print(last_item)

# slicing lists [start: stop-1] --> [start:stop)
print("slicing")
sliced_num = numbers[1:]
print(sliced_num)

# modifying lists
print("modifying lists \n")
num_ls = [343,52,5,25,2,6,8,854,3,365,3,15,5,4,2,74,2,67,45,7]
print(num_ls)

# chaning the first element in the list
num_ls[0] = 4
print(num_ls)

# append 
print('Appending \n')
print(num_ls)
print(len(num_ls))

num_ls.append("Thibedi")
print(num_ls)
print(len(num_ls))

# insert 
print('Insert \n')
print(num_ls)
# num_ls.insert(4, "position 4")
print(num_ls)

# remove 
num_ls.remove(4)
print(num_ls)

# pop 
num_ls.pop()
print(num_ls)

num_ls.pop(4)
print(num_ls)

# help(num_ls.pop)
num_ls.sort()
print(num_ls)
num_ls.sort(reverse=True)
print(num_ls)

num_ls.reverse
print(num_ls)