# Basic while loop 

# while <condition>: -> while this condition is true , do x 
# count = 0 
# while count < 5: 
#     print(count)
#     count +=1 # do not forget to increment , otherwhise you will have an infinite loop 
    
    
# password mananger 
password = "secret123"
attempts = 0 

while True: 
    user_input = input("Enter password: ")

    if user_input == "": 
        print("You enetered nothing. Try again")
        continue 
    
    attempts +=1 
    
    # what happens when the user is correct 
    if user_input == password: 
        print("login successful")
        break 
    
    # what happens when the user is incorrect
    if attempts >= 5: 
        print("Too many attemps , account locked")
        break 
    
    print("Incorrect password, try again")
    

