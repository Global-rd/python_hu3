items = ["apple", "cherry", "banana", "date"]
treshold_list = [1,2,3]
#length = len(items)
#print(length)
#
#if length > treshold:
#    print(f"The list has {length} items, treshold is {treshold}")

#walrus

if (length := len(items)) > (treshold := len(treshold_list)):
    print(f"The list has {length} items, treshold is {treshold}")