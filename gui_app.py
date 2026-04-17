import tkinter as tk
from weather_app import get_weather

expenses = []
import csv

# 起動時読み込み
try:
    with open("data.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["amount"] = int(row["amount"])
            expenses.append(row)
except FileNotFoundError:
    pass
def save_data():
    with open("data.csv", "w", newline="", encoding="utf-8") as f:
        fieldnames = ["name", "category", "amount", "lat", "lon"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(expenses)

def add_data():
    name = entry_name.get()
    category = entry_category.get()
    amount = entry_amount.get()
    lat = entry_lat.get()
    lon = entry_lon.get()

    if name and category and amount and lat and lon:
        expenses.append({
            "name": name,
            "category": category,
            "amount": int(amount),
            "lat": float(lat),
            "lon": float(lon)
        })

        update_list()
        entry_name.delete(0, tk.END)
        entry_category.delete(0, tk.END)
        entry_amount.delete(0, tk.END)
save_data()
def update_list():
    listbox.delete(0, tk.END)
    total = 0  
    for e in expenses:
        listbox.insert(tk.END, f"{e['name']:<10} | {e['category']:<6} | {e['amount']:>10}円")
        total += e["amount"]
        total_label.config(text=f"合計: {total}円")
def delete_data():
    selected = listbox.curselection()

    if selected:
        index = selected[0]
        deleted = expenses.pop(index)
        print(f"{deleted['name']} を削除")

        update_list()
save_data()
def show_weather():
    selected = listbox.curselection()

    if not selected:
        result_label.config(text="選択してください")
        return

    index = selected[0]
    e = expenses[index]

    temp, wind, weather = get_weather(e["lat"], e["lon"])

    if temp is None:
        result_label.config(text="取得失敗")
    else:
        result_label.config(
            text=f"{e['name']} → {weather} / {temp}℃"
        )
# 画面作成
root = tk.Tk()
root.title("案件管理アプリ")

# 入力欄
tk.Label(root, text="顧客名").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="ステータス").pack()
entry_category = tk.Entry(root)
entry_category.pack()

tk.Label(root, text="金額").pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

tk.Label(root, text="緯度").pack()
entry_lat = tk.Entry(root)
entry_lat.pack()

tk.Label(root, text="経度").pack()
entry_lon = tk.Entry(root)
entry_lon.pack()

total_label = tk.Label(root, text="合計: 0円")
total_label.pack()

# ボタン
tk.Button(root, text="追加", command=add_data).pack()
tk.Button(root, text="削除", command=delete_data).pack()
tk.Button(root, text="一覧表示", command=update_list).pack()
tk.Button(root, text="天気を見る", command=show_weather).pack()

result_label = tk.Label(root, text="")
result_label.pack()
# 一覧表示
listbox = tk.Listbox(root, width=50)
listbox.pack()
update_list()

root.mainloop()