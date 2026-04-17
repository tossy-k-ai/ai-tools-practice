import csv

expenses = []

# 起動時に読み込み
try:
    with open("data.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["amount"] = int(row["amount"])
            expenses.append(row)
except FileNotFoundError:
    pass

# ★ AIメール生成
def generate_mail(name, category, amount):
    return f"""{name}様

いつもお世話になっております。
現在「{category}」の案件について、
{amount}円のご提案をさせていただきます。

何卒よろしくお願いいたします。
"""


while True:
    print("\n1:案件追加 2:一覧表示 3:削除 4:検索 5:編集 6:終了")
    choice = input("選択: ")

    if choice == "1":
        name = input("顧客名: ")
        category = input("ステータス（新規/商談中/受注）: ")
        amount = int(input("金額: "))

        expenses.append({
            "name": name,
            "category": category,
            "amount": amount
        })

        # 保存
        with open("data.csv", "w", newline="", encoding="utf-8") as f:
            fieldnames = ["name", "category", "amount"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(expenses)

        print(f"{amount}円追加した！")
    elif choice == "2":
        total = 0
        category_total = {}

        print("\n--- 案件一覧 ---")
        print("顧客名        | 状態   | 金額")
        print("-" * 40)

        for e in expenses:
            print(f"{e['name']:<12} | {e['category']:<6} | {e['amount']:>10}円")
            total += e["amount"]

            # カテゴリ集計
            if e["category"] not in category_total:
                category_total[e["category"]] = 0

            category_total[e["category"]] += e["amount"]

            # メール
            print("  ↓営業メール")
            mail = generate_mail(e["name"], e["category"], e["amount"])
            print(mail)
            print("-" * 40)

        print(f"\n合計: {total}円")
        print("\nカテゴリ別合計:")

        for cat, amt in category_total.items():
            print(f"{cat}: {amt}円")
    elif choice == "3":
        # 一覧表示（番号付き）
        for i, e in enumerate(expenses):
            print(f"{i}: {e['name']} | {e['category']} | {e['amount']}円")

        # 削除する番号入力
        index = int(input("削除する番号: "))

        if 0 <= index < len(expenses):
            deleted = expenses.pop(index)
            print(f"{deleted['name']} を削除しました")

            # CSVも更新
            with open("data.csv", "w", newline="", encoding="utf-8") as f:
                fieldnames = ["name", "category", "amount"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)

                writer.writeheader()
                writer.writerows(expenses)
        else:
            print("無効な番号です")
    elif choice == "4":
        keyword = input("顧客名で検索: ")

        found = False

        for e in expenses:
            if keyword.lower() in e["name"].lower():
                print(f"顧客: {e['name']} | 状態: {e['category']} | 金額: {e['amount']}円")
                found = True

        if not found:
            print("該当データなし")
    elif choice == "5":
        # 一覧表示
        for i, e in enumerate(expenses):
            print(f"{i}: {e['name']} | {e['category']} | {e['amount']}円")

        index = int(input("編集する番号: "))

        if 0 <= index < len(expenses):
            e = expenses[index]

            print("空Enterで変更なしにできます")

            new_name = input(f"顧客名（現在: {e['name']}）: ")
            new_category = input(f"ステータス（現在: {e['category']}）: ")
            new_amount = input(f"金額（現在: {e['amount']}）: ")

            if new_name:
                e["name"] = new_name
            if new_category:
                e["category"] = new_category
            if new_amount:
                e["amount"] = int(new_amount)

            print("更新しました")

            # CSV更新
            with open("data.csv", "w", newline="", encoding="utf-8") as f:
                fieldnames = ["name", "category", "amount"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)

                writer.writeheader()
                writer.writerows(expenses)

        else:
            print("無効な番号です")
    elif choice == "6":
        break