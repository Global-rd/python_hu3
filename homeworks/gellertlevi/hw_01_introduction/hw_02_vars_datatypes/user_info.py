user_info = { "name": "Mike", "age": 25, "favourite_meals": [ "pizza", "carbonara", "sushi" ], "phone_contacts": { "Mary": "+36701234567", "Tim": "+36207654321", "Tim2": "+36304567321", "Jim": "+364005000" } }
user_input = input("Specify four programming languages separated by commas: ")
prog_lang1,prog_lang2, prog_lang3, prog_lang4= [x.strip() for x in user_input.split(",")]
prog_lang_list = [prog_lang1,prog_lang2, prog_lang3, prog_lang4]
user_info["skills"] = prog_lang_list
user_info["favourite_meals"] = sorted(user_info["favourite_meals"])
'print (user_info["favourite_meals"])'
print(user_info["favourite_meals"][-2])
user_info["favourite_meals"].append("spaghetti")
'user_info["favourite_meals"].append("favourite_meals" [2:3])'
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])
user_info["favourite_meals"] = list(dict.fromkeys(user_info["favourite_meals"]))
user_info["favourite_meals"] [0], user_info["favourite_meals"] [-1] = user_info["favourite_meals"] [-1], user_info["favourite_meals"] [0]
'phone_contacts.update({"emergency_call": 112})'
user_info["phone_contacts"].update({"emergency_call": "112"})
user_info["phone_contacts"].pop("Tim")

print (user_info)



