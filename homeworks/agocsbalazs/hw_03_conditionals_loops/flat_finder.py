#Sarah nevű lánynak van egy preferncia listája, amibe beleírja, hogy mit szeretne mennyiért és mit egyátalán nem. 
#A lista alapján értékeljük a megadott válaszokat és írjuk ki, hogy elfogadja-e az ajánlatot vagy sem.
sarah_want_list= { 
    "new york": 4000,
    "san francisco": 4000,
    "chicago":float('inf'),
    "washington":float('-inf'), 
    "everithing_else": 3000
}

#csak értelmes városnevet fogadjon el
while True:
    city = input("Enter the city where your flats in: ").strip().lower()
    if city.isdigit() == False and len(city) > 0:
        break
    print("Invalid city name. Please enter a valid city name.") 


#csak számot fogadjon el a bérleti díjnak
max_rent = int(input("Enter the rent you asging for your flat $: "))

#printeld ki "EGY" f-string használatával hogy az adott feltételek (város és albérlet ára) mellett be tudna e költözni az adott helyre. 
# Azaz ha 1db stringbe kell tenni a választ akkor változóba kell rakni az if elemek eredményét és a végén kiírni egy f-stringben.
    
default_max = 3000 
max_price = sarah_want_list.get(city, default_max)

if max_price == float('-inf'):
    result = "forbidden. Too expensive"
elif max_rent <= max_price:
    result = "accepted!"
else:
    result = "too expensive."

print(f"Sarah says: {city.title()} - {result} (${max_rent})")






