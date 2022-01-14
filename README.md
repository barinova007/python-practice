# python-practice

+ ## Web-разработка
+ ## ИИ Машинное обучение
+ ##  Анализ данных
+ ## Автоматизация задач
+ ## Десктопные приложения
+ ## Игры и другое.
+ ## Не строго типизированный язык

__________
```
 message = 'Hello, world'
 print ('Hello, world')
message = '58
 print ('Hello, world')

2+89
2/2
10//3
```
## Разметка:
чтобы это определить:
```
lenochka_1 = 10
# print (type (lenochka_1), lenochka_1)
```

+  INT - целые числа
+  FLOAT - число с плавющей запятой
+  STR - строковый тип
+  BOOL - логический тип

## Математические операции:
+ A + B - сложение
+ A - B - вычитание
+ A * B - умножение
+ A / B - деление 
+ A // B - целая часть от деления
+ A %  B - остаток от деления
+ A ** B - возведение в степень
  
 ## Операторы сравнения 
+ ">"  - больше
+ "<"  - меньше
+ ">=" - больше или равно
+ "<=" - меньше или равно
+ "==" - равно
+ "!=" - не равно


##  Условия
+ if   условие 1 и действие 1
+ elif условие 2 и действие 2
+ else условие 3 и действие 3

##
+ and (и) -логическое умножение
+ or (или) - логическое сложение
+ not (не) - логическре отрицание

```
age = 19
if (age>=18):
    print (Вход разрешён)
elif: (age>=18) and  (age<25)   
    print (Только в паре)
else:
    print (Вход разрешён)
```

## Пользовательский ввод
+ input

```
age  = int(input ("Сколько тебе лет?"))
if (age>=18):
    print (Вход разрешён)
elif: (age>=18) and  (age<25)   
    print (Только в паре)
else:
    print (Вход разрешён)
```
## Операторы
+  INT () - создаёт целочисленное
+  FLOAT () - создаёт вещественные число
+  STR () -  создаёт строку

## Функции
+ def имя_функция (параметры)
    определение_функции
````
def hello ():
    print ('Hello, world')

x = int (input ("Введите 1 число:") 
y = int (input ("Введите 2 число: ")  

def sum (a,b):
    return a + b
print (sum (x,y))

либо 
z = sum (x,y)
print (z)

def f (a):
    return 2*a - 2
print (f(2))
````

## Область видимости переменных
а = 45
b - 5
def f() :
    global a
    a - a + 2
    print (a)

## Циклы (for, while)
+ for - итерирование пербор каждого объекта 

```
name = "Lena"
for i in name:
    print (i)
```
+ range - написать 10 раз имя Лена
```
name = "Lena"
for i in range (1,11):
    print (i)
```

+ while - предусловие
```
i = 1
while i < -10:
      print (i)
      i = i + 1
      break - остановить цикл

i = 1
while i < -10:
      if i !=5:
      print (i)
      i = i + 1
      continue - продолжить, перскочил


while 1 == 1:
    print ('Бесконечный цикл')
```

## Списки 

```
spisok = []
numbers = [3,4,5,6,7,8,5]
print(numbers)
numbers = [3,4,5,6,7,8,5,[name]]
print(numbers)
numbers = [3,4,5,6,7,8,5,[1,5,6]]
print(numbers)

names = ['Имя', 'Пёс']
print (names [1])

```


import math - импортнуть библиотеку с мат.ф
mm = math.sqrt(49))
print (mm, type (mm))
















































