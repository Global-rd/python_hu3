# name = input("Kérlek, add meg a neved: ")

name = input("Kérlek, add meg a neved: ").strip().title()

# age = input("Kérlek, add meg az életkorod: ")

age = int(input("Kérlek, add meg az életkorod: "))

pyexp = int(input("Kérlek, add meg a Python tapasztalatodat években: "))

want_to_be_dev = input(
    "Szeretne profi Python fejlesztő lenni? (yes/no) ").strip().lower()

dev_text = "He/she wants to be a Python developer!" if want_to_be_dev == "yes" else "He/she does not want to be a Python developer!"

# name = name.strip().title()

# age = int(age)

age_in_days = age * 365


print(
    f"My character is {age_in_days} old. His/her name is {name} and he/she has {pyexp} years experience. {dev_text}")

# print(name)
# print(age)
# print(pyexp)
