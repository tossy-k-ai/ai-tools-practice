import csv

expenses = []

class Customer:
    def __init__(self,company,name,address):
        self.company = company
        self.name = name
        self.address = address
    def show(self):
        print(f"会社:{self.company}")
        print(f"担当者:{self.name}")
        print(f"連絡先:{self.address}")


def add_data(): 
        company = input("company")
        name = input("name")
        address = input("address")

        expenses.append(Customer(company,name,address))

def save_data():        
    with open("data2.csv","w",newline="",encoding="utf-8")as f:
            writer = csv.DictWriter(f,fieldnames=["company","name","address"])
            rows = [{"company":e.company,"name":e.name,"address":e.address} for e in expenses]
            writer.writeheader()
            writer.writerows(rows)

def show_data():
        for e in expenses:
            e.show()

try:
    with open("data2.csv","r",encoding="utf-8")as f:
        reader=csv.DictReader(f)
        for e in reader:
            expenses.append(Customer(e["company"],e["name"],e["address"]))
                                       
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