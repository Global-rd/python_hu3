
def register_user(users, name, age):
    """
    Registers a user to the users list.
    """
    user = {"name": name, "age": age}
    users.append(user)
    print(f"User registered successfully: {name}")

def update_user_age(users, name, new_age):
    """
    Updates a user's age based on the new age input.
    """
    for user in users:
        if user["name"] == name:
            user["age"] = new_age
            print(f"User {name}'s age has been updated to {new_age}")
            return
    print(f"No user named {name} found in the registry")


def display_user_info(users, name):
    """
    Displays a single user's information
    """
    for user in users:
        if user["name"] == name:
            print(f"User info - Name: {user['name']} Age: {user['age']}")
            return
    print(f"No user named {name} found in the registry")

def display_all_users(users):
    """
    Displays all user's information
    """
    print("Registered users:")
    for id, user in enumerate(users, 1):
        print(f"{id} - {user['name']}")


def main():
    users = []
    register_user(users=users, name="Alice", age=13)
    register_user(users=users, name="Bob", age=14)
    register_user(users=users, name="Chad", age=15)
    register_user(users=users, name="Dexter", age=16)
    print(users)
    update_user_age(users=users, name="Teddy", new_age=14)
    print(users)
    display_all_users(users=users)

main()


#[
#    {"name": "John", "age": 10},
#    {"name": "Mary", "age": 11}
#    {"name": "Timmy", "age": 12}
#]