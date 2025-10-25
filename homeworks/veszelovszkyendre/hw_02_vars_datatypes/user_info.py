user_info = {
    "name": "Mike",
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
        "Jim": "+364005000"
    }
}

prog_lan = input(
    "Kérlek, adj meg 4 programozási nyelvet vesszővel elválasztva! ")

skills_list = prog_lan.split(",")

user_info["skills"] = skills_list

user_info["favourite_meals"].sort()

print("Favorite meals utolső előtti eleme: ", user_info["favourite_meals"][-2])

user_info["favourite_meals"].append("spaghetti")

third_fourth_elements = user_info["favourite_meals"][2:4]

user_info["favourite_meals"].extend(third_fourth_elements)

seen = set()

unique_meals = []

for meal in user_info["favourite_meals"]:
    if meal not in seen:
        unique_meals.append(meal)
        seen.add(meal)

user_info["favourite_meals"] = unique_meals

user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]

user_info["phone_contacts"]["Andrew"] = "+361234567"

user_info["phone_contacts"].pop("Tim")

user_info["phone_contacts"]["Jack"] = ["+369876543", "+364442222"]

print(
    "Skills lista utolsó 3 eleme ellentétes sorrendben:", user_info["skills"][-3:][::-1])

if "Tim2" in user_info["phone_contacts"]:

    user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop(
        "Tim2")
print(user_info["phone_contacts"])
