#Homework 02
#Task 2

from pprint import pprint

user_info = { "name": "Mike", 
             "age": 25, 
             "favourite_meals": [ 
                 "pizza", 
                 "carbonara",
                   "sushi" 
                   ],
               "phone_contacts": { 
                   "Mary": "+36701234567",
                   "Tim": "+36207654321",
                    "Tim2": "+36304567321",
                    "Jim": "+364005000" } 
                    }
                    
user_input = input("Please give me 4 programming languages separated by a comma and without spaces: ")

skill = user_input.split(",")

user_info["skill"]= skill #subtask No 1

user_info["favourite_meals"].sort()  #subtask No 2

print(user_info["favourite_meals"][-2]) #subtask No 3

user_info["favourite_meals"].append("spaghetti") #subtask No 4

new_added_elements = user_info["favourite_meals"][2:4]  

user_info["favourite_meals"].extend(new_added_elements) #subtask No 5

user_info["favourite_meals"] = list(set(user_info["favourite_meals"])) #subtask No 6

# first_element = user_info["favourite_meals"][0] 
# last_element = user_info["favourite_meals"][-1]
# user_info["favourite_meals"][0] = last_element
# user_info["favourite_meals"][-1] = first_element 

user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0] #subtask No 7


user_info["phone_contacts"]["Jonathan"] = ("+36309125484") #subtask No 8

del user_info["phone_contacts"]["Tim"]  #subtask No 9

user_info["phone_contacts"]["Eliah"] = ["+36704128596" ,"+36203359427"] #subtask No 10

print(user_info["skill"][-3:][::-1]) # extra task 1

user_info["phone_contacts"] ["Tim"] = user_info["phone_contacts"] ["Tim2"] # extra task 2

del user_info["phone_contacts"] ["Tim2"]

print(skill)

pprint(user_info)