import csv

expenses = []

def add_data(): 
        company = input("company")
        name = input("name")
        address = input("address")

        expenses.append({"company":company,"name":name,"address":address})

def save_data():        
    with open("data2.csv","w",newline="",encoding="utf-8")as f:
            writer = csv.DictWriter(f,fieldnames=["company","name","address"])

            writer.writeheader()
            writer.writerows(expenses)
def show_data():
        for e in expenses:
            print(e["company"])
            print(e["name"])
            print(e["address"])

try:
    with open("data2.csv","r",encoding="utf-8")as f:
        reader=csv.DictReader(f)
        for e in reader:
            expenses.append(e)
except FileNotFoundError:
    pass

while True:

    print("1:追加,2:保存,3一覧表示,4終了")
    choice = input()

    if choice=="1":
        add_data()
    
    elif choice=="2":
        save_data()

    elif choice=="3":
        show_data()
    elif choice=="4":
        break  