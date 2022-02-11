# python-practice
## [My playlist](https://www.youtube.com/playlist?list=PLi7THDBnHl-vHxeUdsLnAH3u19ytlxX0W)


```
Web-разработка
ИИ Машинное обучение
Анализ данных
Автоматизация задач
Десктопные приложения
Игры и другое.
Не строго типизированный язык
```
__________
```
 message = 'Hello, world'
 print ('Hello, world')
message = '58
 print ('Hello, world')

2+89
2/2
10//3
```'
## Разметка:
чтобы это определить:
```
lenochka_1 = 10
# print (type (lenochka_1), lenochka_1)
```

+  INT - целые числа
+  FLOAT - число с плавющей запятой
+  STR - строковый тип
+  BOOL - логический тип (true/fols)

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

```
import math - импортнуть библиотеку с мат.ф-ций
mm = math.sqrt(49))
print (mm, type (mm))

Задачка:
Есть список с рус.буквами: 
list1 = (а, б, в, г, д, е, ё, ж, з, и, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ъ, ы, ь, э, ю, я)
на основании этого списка создать список, в котором будут цифры от первой буквы до размера списка с буквами.
list2 = (1, ..., длина(list1))
Проитерировать эти списки таким образом, чтобы на выходе получить массив,
 в котором идет чередование сперва четная цифра потом буква по порядку, 
когда закончатся четные, добавляем нечетные и буквы продолжаются по порядку. Повторений быть не должно!
Пример: [2, а, 4, б, 6, в....3, с, 5, т и т.д.]


continue - завершает текущую иттерацию и продолжает следующую.

range() - возвращает последовательность чисел.
По умолчанию он начинается с 0, увеличивается на 1 и останавливается перед указанным числом.
nums = list(range(5))
print(nums[4])
______________
список от 0 до 4: a=[0,1,2,3,4] Далее выведите индекс числа 1, и Вы увидите что индекс данного числа будет равен 1. Например индекс числа 0 будет равен 0. Из эксперимента следует что range(5) создаёт список от 0 до 4: [0, 1,2,3,4] и индекс 0 будет равен 0, а индекс числа 4 будет равен 4.

nums = list(range(5, 8))
print(len(nums))
____________
range создаёт списки до указанного аргумента, в нашем случае это 5,6,7

What is the result of this code?
nums = list(range(3, 15, 3))
print(nums [2] )
__________
список от 3 до 15( третяя цифра указывает величину шага в списке, также мы помним, что число 15 не выводится, потому что оно последнее)
Список получается такой: [3,6,9,12] Нужно вывести - nums[2] Так как мы помним, что отсчёт элементов начинается с нуля: [3(0),6(1),9(2),12(3)] 
То и ответ будет такой: nums[2] = 9

for i in range(0, 20, 2):
print(i)
__________
Для цикла "i" в диапазоне от 0 до 20, с шагом в 2 элемента (третьей цифрой указывается шаг, с которым выводить элементы цикла), вывести цикл "i" 

list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]])
_________
мы раскрываем первые скобки [list[4]] то есть считаем в первых скобках числа до 4( первую цифру берем за 0) получается 5, 
то есть эта скобка [list[4]] будет равняться 5 Далее раскрываем следующую скобку [list[5]] и вместо 4 уже 5
и начинаем считать числа из первых скобок (первую цифру берем за 0) получается 8


list = [1,2,3,4] 
if len(list) % 2 ==0: 
print(list[0])
____________
1) используем len(считает количество всех элементов в списке.
Элементов 4. %(знак целочисленного деления, равном будет остаток от деления,4делим на 2,остаток от деления 0)4%2=0, 0==0(0равен 0, ==оператор сравнения) значение истина,
зачит цикл if будет выполняться. 3) ставим [0], так как первый элемент списка стоит на позиции 0(отчет идет от 0)
4)Ставим : во второй строчке(правила питона) ИТОГО: list = [1,2,3,4] If len(list)%2==0: print(list[0])


letters = ['x', 'y', 'z']
letters.insert(1, 'w')
print(letters[2])
___________
Считаем элементы списка: letter[0]=x letter[1]=y letter[2]=z insert (1,’w’) значит вместо [1] элемента встанет w,
а y встанет [2] letter[0]=x letter[1]=w letter[2]=y letter[3]=z Ответ: y

list = [1, 2, 3]
for var in list:
print(var)
____________________________________
Задачка:

Данный код решает проблему FizzBuzz и использует слова «Solo» и «Learn» вместо «Fizz» и «Buzz».
Он принимает на вход n и выводит числа от 1 до n.
Для каждого числа, кратного 3, вместо числа выведите «Соло».
Для каждого числа, кратного 5, печатает «Learn» вместо числа.
Для чисел, кратных как 3, так и 5, выведите «SoloLearn».
Вам нужно изменить код, чтобы пропустить четные числа, чтобы логика применялась только к нечетным числам в диапазоне.


n = int(input())
for x in range(1, n):
    if x % 3 == 0 and x % 5 == 0:
        print("SoloLearn")
    elif x % 3 == 0:
        print("Solo")
    elif x % 5 == 0:
        print("Learn")
    else:
        print(x)
_____________________________        
        
n = int(input())
for x in range(1, n,2):
    if x % 3 == 0 and x % 5 == 0:
        print("SoloLearn")
        continue
    elif x % 3 == 0:
        print("Solo")
        continue
    elif x % 5 == 0:
        print("Learn")
        continue
    else:
        print(x)
   
```

Повторное использование кода: функции и модули.














































