import datetime
import names
import time
import csv


with open('text.txt', 'w') as f:
    date = str(datetime.datetime.now()) + " "
    name = names.get_full_name()
    writer = f.writelines([date, name])
    writer = f.writelines([date, name, '\n'])

with open("text.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fielnames=["data","name"])
    writer.writeheader()
    while True:
        date = str(datetime.date.today())
        name = names.get_full_name()
        writer.writerow({"date": date, "name": name})
        print(date)
        print(name)
        time.sleep(0.5)