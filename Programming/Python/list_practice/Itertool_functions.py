# https://docs.python.org/3/library/itertools.html
import itertools

# counter = itertools.count()
# print(next(counter))
# print(next(counter))
#
# data = [100, 200, 300, 400]
#
# daily_data = list(zip(itertools.count(), data))
# print(daily_data)
#
#
# daily_data = list(zip(itertools.count(start=1), data))
# print(daily_data)
#
#
# # cycle
# counter = itertools.cycle(("ON", 'OFF'))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter)
#
# my_list = [1,2,3]
# Scanners = ['1.5', 'EC7000', 'MYVISIONX','VisionX']
# Firmware = ['1.5', '2.2.0']
#
#
#
# combinations = itertools.combinations(Scanners,2)
# for p in combinations:
#     print (p)
#
# print("====================================================")
#
# for c in itertools.combinations_with_replacement(Scanners, 3):
#   print(c)

my_list = [5,2,8]
permutations = itertools.permutations(my_list, 2)
for p in permutations:
    print (p)
    print(p[0] * p[1])