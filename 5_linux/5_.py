import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str)
parser.add_argument('--age', type=str)

args = parser.parse_args()
print("Name")
<<<<<<< HEAD



# 1. Кодим скрипт на питоне.
# 2. Скачиваем его на сервер.
# 3. Заходим на сервер.
# 4. Заходим в скрин, и запускаем скрипт.
# 5. Выходим из скрина, и проверяем наличие созданного файла (можно проверить содержимое с помощью "cat").
# 6. Заходим обратно в скрин, вырубаем скрипт.
# 7. Выходим из скрина, и из сервера.
# 8. Скачиваем к себе на локалку сгенерированный сервером файл.

import names
import time
from datetime import datetime

file_path = '/home/u_23_22/names.txt'

while True:

    with open(file_path, 'a+') as file_txt:
        now = datetime.now()

        user_name = names.get_full_name()
        dt_string = now.strftime('%d/%m/%Y %H:%M:%S')

        result_str = user_name + ' -- ' + dt_string + '\n'

        file_txt.write(result_str)

    time.sleep(0.5)
=======
>>>>>>> 238b06661e09d9fbd585980d599b661681f67122
