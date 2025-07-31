# Creating sets 

unique_numbers = {1,2,3,4,5}

# if you add udplicate values they will be ingnored
duplciate_test = {1,2,2,3,3,4,5,5}

empty_set = set() # we can not use {} because it creates an empty dictionary

print("Unique values: " , unique_numbers)
print("Duplicate values: " , duplciate_test)

### operations for sets 

# add elements 
unique_numbers.add(11)
print(unique_numbers)

unique_numbers.remove(3) # Removes an element (errors out if the element is not found)
print(unique_numbers)

unique_numbers.discard(30) # Discards an element (does not error out if the element is not found)
print(unique_numbers)

# has this removed anything or not ? 


num = 111
len_unique = len(unique_numbers)
unique_numbers.discard(num)

if len_unique == len(unique_numbers): 
    print("The number " ,  num , " does not exist in the set")
else: 
    print('The number ' , num , ' has been removed')


# Set operation 

set1 = {1,2,3}
set2 = {3,4,5}

union = set1 | set2
print(union)

intersection = set1 & set2
print(intersection)

difference = set2 - set1
print(difference)