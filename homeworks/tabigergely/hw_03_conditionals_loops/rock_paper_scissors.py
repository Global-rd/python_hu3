while True:
    rounds = (int(input("Mennyi kört szeretnél játszani?")))
    if rounds % 2 != 0:
        break
    else:
        print("Kérlek egy páratlan számot adj meg.")


