# Creating dictionaries 
student = {
    "name": "Jack", 
    "age": 15, 
    "grades": {
        "maths": 67,
        "physics": 90,
        "IT": 85
    }
}

print(student)
empty_dict = {}

# Accessing values --> direct
name = student["name"]
print(name)

# safer way
physics = student.get('graddddes')

print(type(physics))

if physics == None: 
    print("EMPTY ")

# Modify 
student['friends'] = ['Thato' , 'Landa' , 'Taku', 'Lwazi']
print(student)

student['grades']["maths"] = 87
print(student)

del student['age']
print(student)


print(student.keys())
print(type(student.keys()))
print(list(student.keys()))
print(type(list(student.keys())))

print('items')


print(student.items())
print('values')
print(student.values())

for i in range(10): 
    if i == 3: 
        continue 
    if i == 7: 
        break
    print(i)
    
1 ,2,3, 10, 44, 65

