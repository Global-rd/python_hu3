#  set

# hasonló a listához. többelemet tárol
# rendezetlen és megváltozhatatlan, NEM indexelt.
# set elemeit nem lehet megváltoztatni, de hozzáadni és törölni lehet.
# kapcsos zárójelekkel, vagy a set() constructorral hozható létre

original_numbers = {1,2,3,4,5}
new_numbers= {4,5,6,7}

original_numbers.update(new_numbers)        # kiveszi a duplikátumokat    adress ugyanaz maradt (megváltoztatható)

# list-ból kiszedni a duplikációt
numbers_list = [0,0,0,0,1,1,1,1,2,2,2,3,3,3,4,4,5,5,6]   # ez egy lista

numbers_list = list(set(numbers_list))
print(numbers_list)

numbers_list = list(set(numbers_list))     # először set-é, majd listává alakít
print(numbers_list)

# add element
original_numbers.add(10)                    # hozzáadja a 10-et
original_numbers.remove(10)                 # kitörli a 10-et
inter_num = original_numbers.intersection(new_numbers)   # a metszete a két set-nek


# frozernset
