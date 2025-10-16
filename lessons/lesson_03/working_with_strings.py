fruit = "raspberry and apple"
fruit_length = len(fruit)
print(fruit_length)

#concatenation / konkatenálás
first_name = "Istvan Gabor"
last_name = "Nagy"

full_name = first_name + " " + last_name
print(full_name)
introduction = "My name is " + first_name + " " + last_name + "."
print(introduction)

#interpolated string / f-string
introduction = f"My name is {first_name} {last_name}."
print(introduction)

#indexing, slicing
print(fruit)
print(fruit[0])
print(fruit[1])
print(fruit[2])
print(fruit[3])

print(fruit[-1])
print(fruit[1:3]) #inclusive - exclusive
print(fruit[:2])
print(fruit[-2:])
print(fruit[-1::-1])

#string metódusok

#metódus: amit egy objektum tud csinálni
#attribútum: ami jellemzi az objektumot

#objektum: kutya
#metódus: ugat, eszik, iszik, alszik
#attribútum: életkor, fajtája, testsúlya, neve

print("----------")

print(fruit)
print(fruit.capitalize())
print(fruit.upper())
print(fruit.title())

print(fruit.replace("a", "#"))

fruit = "        apple        "

print(fruit.strip()) # lstrip(), rstrip()


#method chaining
print(fruit.upper()
           .replace("A", "#")
           .strip())