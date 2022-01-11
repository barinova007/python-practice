# Переменная String
myName = 'Lena'
print('Тип переменой: ', type(myName), myName)

# Переменная Integer
myAge = 27
print('Тип переменой: ', type(myAge), myAge)

# Переменная Float
myTemp = 36.6
print('Тип переменой: ', type(myTemp), myTemp)

# Переменная Bytes
myAgeBytes = bytes(27)
print('Тип переменой: ', type(myAgeBytes), myAgeBytes)

# Переменная Tuple (Нельзя добавить элемент, нельзя удалить элемент, )
myFamaly = ("Oksana", "Valeriy")
print('Тип переменой: ', type(myFamaly), myFamaly)

# Переменная List
myDocList = ["Passport", "Driver's license", "Deditation insurance"]
print('Тип переменой: ', type(myDocList), myDocList)

# Переменная set (элементы множества всегда уникальны, неупорядоченная коллекция. Для создания пустого множества
# нужно непосредственно использовать set())
mySets = {1, 1, 2, 3, 3, 2}
print('Тип переменой: ', type(mySets), mySets)

#   Переменная frozenset //
myLib = frozenset('П у ш к и')
print('Тип переменой: ', type(myLib), myLib)

# Переменная Dict (Словать)

myDict = {'hello': 'Привет', 'bye': 'Пока'}
print('Тип переменой: ', type(myDict), myDict)

# Создать 2 переменные String, создать переменную в которой суммируете эти переменные. Вывести в консоль. +
strTextOne = 'Это'
strTextTwo = 'Восхитительно'
strTextThree = strTextOne + strTextTwo
print(strTextOne, '+', strTextTwo, '=', strTextThree)

# Создать 2 переменные Integer, создать переменную в которой суммируете эти переменные. Вывести в консоль.
digOne = 635
digTwo = 923
total = digOne + digTwo
print('Результат сложения', digOne, '+', digTwo, '=', total)
point13 = digOne / digTwo
print('Результат деления', digOne, '/', digTwo, '=', point13)
point14 = digOne * digTwo
print('Результат умножения', digOne, '*', digTwo, '=', point14)
digThree = 9
digFour = 3
point15 = digTwo // digFour
print('Результат деления без отстатка', digTwo, '//', digFour, '=', point15)
point16 = digTwo % digThree
print('Остаток от деления', digTwo, '%', digThree, '=', point16)
print((7 + 12) ** 3 + 7 * 4 - 44 / 2 ** 4)

# Дополение HW_1 из второго потока

print(strTextTwo, str(digTwo))
print(strTextTwo + str(digTwo))
