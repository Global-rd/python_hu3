import json

def write_json(response, json_path):
    """lekérdezés írása jsonbe"""
    try:
        with open(json_path, "w") as file:
                json.dump(response, file)
        print("A fájl írása sikeresen megtörtént.")
    except Exception as e:
        print("Hiba a fájl írása közben")


def change_direction(row):
    if row["price_change_percentage_24h"] > 0:
        return '+'
    elif row["price_change_percentage_24h"] < 0:
         return '-'
    else:
        return '0'