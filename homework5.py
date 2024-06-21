immutable_var = (67, ['Hello' , 6.4 ], True)
print(immutable_var)
#immutable_var[1] = 'World' Если мы имеем полностью кортеж , данные не сможем поменять так как это
# не изменяеммый тип данных , но можно в нем указать, изменяемую часть приведя область в [] скобках
# при этом если указать 1 сегмент например- immutable_var[1] = 'World'.
# и будет в кортеже immutable_var = (67, ['Hello'] , 6.4 , True), все ровно выдаст ошибку TypeError: 'tuple' object does not support item assignment
# Решением для изменения будет указать область например - immutable_var = (67, ['Hello' , 6.4 ], True)
# и в команде на изменения тоже нужно указать область и Id изменяемого обьекта
# например immutable_var[1][0] = 'World' . Тогда мы сможем увидеть что слово Hello изменилось на слово World
immutable_var[1][0] = 'World'
print(immutable_var)
mutable_list = [25 , 'Sun' , 9.8 , False ]
mutable_list [0]= 50
print(mutable_list)
