#Sarah nevű lánynak van egy preferncia listája, amibe beleírja, hogy mit szeretne mennyiért és mit egyátalán nem. 
#A lista alapján értékeljük a megadott válaszokat és írjuk ki, hogy elfogadja-e az ajánlatot vagy sem.
sarah_want_list= { 
    "new york": 4000,
    "san francisco": 4000,
    "favourite_citys_ultimate": [  "chicago", ],
    "not_wanted_citys": ["washington"], 
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

not_wanted_city = sarah_want_list["not_wanted_citys"]
ulitimate_city = sarah_want_list["favourite_citys_ultimate"]

#printeld ki "EGY" f-string használatával hogy az adott feltételek (város és albérlet ára) mellett be tudna e költözni az adott helyre. 
# Azaz ha 1db stringbe kell tenni a választ akkor változóba kell rakni az if elemek eredményét és a végén kiírni egy f-stringben.
if city in not_wanted_city:
    result = "no thx. Washington is not wanted"
elif city in ulitimate_city:
    result = "accepted! Chicago is ultimate"
elif city in ["new york", "san francisco"] and max_rent < 4000 : 
    result = "accepted for this price"
elif  max_rent <= sarah_want_list["everithing_else"]:
    result = "accepted for this price"
else:
    result = "forbidden. Too expensive"

msg = f"Sarah says: {city.title()} {result} for ${max_rent}"
print(msg)




