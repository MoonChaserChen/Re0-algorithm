from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
od['e'] = 5
od['f'] = 6
print(od.popitem())  # ('f', 6)
print(od.popitem(last=False))  # ('a', 1)
print(od)  # [('b', 2), ('c', 3), ('d', 4), ('e', 5)]
od.move_to_end('c')
print(od)  # [('b', 2), ('d', 4), ('e', 5), ('c', 3)]
od.move_to_end('e', last=False)
print(od)  # [('e', 5), ('b', 2), ('d', 4), ('c', 3)]