from traceback import print_tb


list = [2,3,2,5,9,0]
tuple1 = (2,3,2,5,9,0)

arranged = sorted(list)
arrangedtuple = sorted(tuple1)

for i in list:
    total = sum(arranged[:5])
    print(total)
print(arranged)
# print(arranged[::-2] , arrangedtuple)
# print(arrangedtuple)
