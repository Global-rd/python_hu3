place_name = input("Add meg a helységnevet: ").strip()
cost =int( input("Add meg az árat USD-ben: "))

if place_name.lower() == "washington":
    print("Semmi pénzért nem lakna Washington városban.")
elif cost >= 4000:
    if place_name.lower() == "chicago":
        print("Bármit megadna azért hogy Chicago városban lakhasson.")
    else:
        print("Ekkora összegért csak Chicago-t választaná.")
else:
    if place_name.lower() in [ "new york" , "san fransisco"]:
        print(f"Kivenné a lakást { place_name.capitalize() } városban.")
    elif cost < 3000:
        print(f"Kivenné a lakást { place_name.capitalize() } városban.")
    else:
        print("Ekkora összegért csak New York-ot vagy San Fransisco-t választaná.")