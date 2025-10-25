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
languages = input("Adj meg 4 programozási nyelvet vesszővel elválasztva (pl: python,java,c++,html): ")
user_info["skills"] = languages.split(",")
print("\nFrissített user_info (skills hozzáadva):")
print(user_info)
user_info["favourite_meals"].sort()
print("\nRendezett favourite_meals lista:")
print(user_info["favourite_meals"])
print("\nA favourite_meals lista utolsó előtti eleme:")
print(user_info["favourite_meals"][-2])
user_info["favourite_meals"].append("spaghetti")
print("\nÚj étel hozzáadva:")
print(user_info["favourite_meals"])
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
user_info["favourite_meals"].sort()
print("\nDuplikátumok eltávolítva:")
print(user_info["favourite_meals"])
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])
print("\nDuplikált lista (3. és 4. elem újra hozzáadva):")
print(user_info["favourite_meals"])
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = \
    user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
print("\nElső és utolsó elem felcserélve:")
print(user_info["favourite_meals"])
user_info["phone_contacts"]["Anna"] = "+36701112233"
print("\nÚj kontakt hozzáadva:")
print(user_info["phone_contacts"])
del user_info["phone_contacts"]["Tim"]
print("\n'Tim' törölve:")
print(user_info["phone_contacts"])
user_info["phone_contacts"]["John"] = ["+36301234567", "+36307654321"]
print("\nÚj ember két telefonszámmal:")
print(user_info["phone_contacts"])