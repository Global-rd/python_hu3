name = input("Kérlek, add meg a neved: ").strip().title()

age = int(input("Kérlek, add meg az életkorod: "))

pyexp = int(input("Kérlek, add meg a Python tapasztalatodat években: "))

want_to_be_dev = input(
    "Szeretne profi Python fejlesztő lenni? (yes/no) ").strip().lower()

dev_text = "wants" if want_to_be_dev == "yes" else "does not want"

age_in_days = age * 365


print(
    f"My character is {age_in_days} old. His/her name is {name} and he/she has {pyexp} years experience. {dev_text}")
