place_name = input("Add meg a helységnevet: ").strip().lower()
cost =int( input("Add meg az árat USD-ben: "))

if place_name == "washington":
    print("Semmi pénzért nem lakna Washington városban.")
elif place_name == "chicago":
    print("Bármit megadna azért hogy Chicago városban lakhasson.")
elif place_name in ["san francisco", "new york"] and cost < 4000:
    print(f"Kivenné a lakást { place_name.capitalize() } városban.")
elif cost < 3000: #ez már csak olyan eset lehet ahol a városnév idegen, ezért elég a cost-ot nézni
    print(f"Kivenné a lakást { place_name.capitalize() } városban.")
else: #ez pedig csak az az eset lehet ahol a városnév idegen, és túl drága
    print(f"Nem venné ki a lakást { place_name.capitalize() } városban.")

""" if place_name.lower() == "washington":
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
        print("Ekkora összegért csak New York-ot vagy San Fransisco-t választaná.")""" 