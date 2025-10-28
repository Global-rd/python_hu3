#arbitrary positional arguments
def calculate_total_price(*items):

    total = 0

    for _, price, quantity in items:
        total += price * quantity

    return total



total = calculate_total_price(
                            ("Apple", 300, 2),
                            ("Orange", 400, 1),
                            ("Banana", 500, 3)
)
print(total)

#arbitrary keyword arguments

def describe_person(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for k,v in kwargs.items():
        print(f"Key: {k} value: {v}")


describe_person(name="John", age=11, job="programmer")


def introduce_person(name, age, *hobbies, country="Hungary", **additional_info):
    print(f"Name: {name}")
    print(f"Name: {age}")
    print(f"Country: {country}")

    if hobbies:
        print("Hobbies: ")
        for hobby in hobbies:
            print(hobby)
    
    if additional_info:
        print("additonal info:")
        for k,v in additional_info.items():
            print(f"{k} - {v}")


introduce_person("Bob",
                13,
                "hiking", "reading", "programming",
                country="Switzerland",
                occupation="programmer", has_pet=True)
