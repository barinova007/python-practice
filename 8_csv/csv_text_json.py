
file_path = 'C:/Users/Barinova/PycharmProjects/pythonProject3/text_files/'
text_file_title = 'text_1.txt'

file_title = file_path + text_file_title
#создали файл в папке:
# f = open(file_title, 'w')
# f.write("Hello,Masya")
# f.close()

# вписать текст списком
ll = ['QA', 'Manual']

with open(file_title, 'w') as f:
    # writer = f.writelines('Hello, QA!')
    # f.writelines(str(ll))
    # разные строчки
    f.writelines("\n".join(ll))

    for i in ll:
        f.write(i)
        f.write('\n')


import csv, json

file_path = 'C:/Users/Barinova/PycharmProjects/pythonProject3/text_files/'
file_name = 'json_file.json'

json_file = file_path + file_name

dict_item = {
    1: "Julia",
    2: [1, 2, 3, 4],
    3: {"name": "Lena", "salary": 2000},
    "city": "Kyiv"
}

with open(json_file, 'r') as jf:
    reader = jf.read()
    json_object = json.loads(reader)

    print(json_object['1'])


with open(json_file, 'a') as jf:
    json.dump(dict_item, jf)


asd = []


def amount():

    word = input("Word: ")
    how_many = int(input("Repeat: "))
    for i in range(how_many):
        asd.append(word + str(i))
    return asd


print(amount())


file = "C:/Users/Barinova/PycharmProjects/pythonProject3/text_files/text_1.txt/"

with open(file, 'w') as f:
    writer = f.writelines('\n'.join(asd))

users_list = [
    ["Vadim", 32],
    ["Alexey", 34],
    ["Julia", 19]
]

users_dict = [
    {'name': 'Vadim', 'age': 32},
    {'name': 'Lena', 'age': 27},
    {'name': 'Alexey', 'age': 19}
]
with open(csv_file_name, 'w') as cf:
    columns = ['name', 'age']
    writer = csv.DictWriter(cf, fieldnames=columns, lineterminator='\n')
    writer.writeheader()

    row_1 = {"name": "Lena", "age": 27}
    writer.writerow(row_1)

with open(csv_file_name, 'a') as cf:
    columns = ['name', 'age']
    writer = csv.DictWriter(cf, fieldnames=columns, lineterminator='\n')
    writer.writerows(users_dict)

with open(csv_file_name, 'r') as csv_f:
    reader = csv.DictReader(csv_f)

    age_list = []
    for i in reader:
        age_list.append(i["age"])
        print(i)

file_path = "C:/Users/Barinova/PycharmProjects/pythonProject3/text_files/"
file_name = "python_json_lesson.json"
file_p_n = file_path + file_name

with open(file_p_n, "r") as jf:
    json_data = jf.read()
    json_object = json.loads(json_data)
    print(json_data, type(json_data))
    print(json_object, type(json_object))
    print(json_object["1"])

with open(file_p_n, "w") as jf:
    json.dump(dict_item, jf)


new_users_list = []
for item in range(0, 100):

    for ul_item in users_list:
        name_age = []
        new_name = ul_item[0] + "_" + str(item)
        new_age = 10 + item
        name_age.append(new_name)
        name_age.append(new_age)
        new_users_list.append(name_age)

#
with open(file_path_name, 'w') as cf:
    writer = csv.writer(cf, lineterminator='\n')
    writer.writerows(users_list)

users_list = [
    ['Lena', 27],
    ['Alexey', 34],
    ['Julia', 19]
]


new_users_list = []


with open(file_path_name, 'w') as cf:
    columns = ['name', 'age']
    writer = csv.DictWriter(cf, fieldnames=columns)
    writer.writeheader()

    row_1 = {'name': 'Lena', 'age': 27}

    writer.writerow(row_1)

with open(file_path_name, 'w') as csv_f:
    columns = ['name', 'age']
    writer = csv.DictWriter(csv_f, fieldnames=columns, lineterminator='\n')
    # row_1 = ['Lena', 27]

    writer.writerows(users_dict)

with open(cvs_file_name, 'r') as csv_f:

    reader = csv.reader(csv_f)
    line_count = 0
    age_list = []

    for row in reader:
        print(row)

age_list.append(int(row['age']))




