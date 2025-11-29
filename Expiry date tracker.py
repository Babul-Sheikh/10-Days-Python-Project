#!/usr/bin/env python3
import datetime
import os

DATA_FILE = "expiry_data.txt"

def load_data():
    data = []
    if not os.path.exists(DATA_FILE):
        return data
    try:
        with open(DATA_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                name, category, date = line.split("|")
                data.append({
                    "name": name,
                    "category": category,
                    "expiry": datetime.date.fromisoformat(date)
                })
    except Exception:
        print("Error reading data file.")
    return data

def save_data(data):
    with open(DATA_FILE, "w") as f:
        for item in data:
            f.write(f"{item['name']}|{item['category']}|{item['expiry'].isoformat()}\n")

def add_item(data):
    name = input("Item name: ").strip()
    category = input("Category: ").strip()
    date_s = input("Expiry (YYYY-MM-DD): ").strip()
    try:
        exp = datetime.date.fromisoformat(date_s)
    except ValueError:
        print("Invalid date format.")
        return
    data.append({"name": name, "category": category, "expiry": exp})
    save_data(data)
    print("Added.")

def show_all(data):
    if not data:
        print("No items.")
        return
    for it in data:
        print(f"{it['name']} | {it['category']} | {it['expiry'].isoformat()}")

def show_expired(data):
    today = datetime.date.today()
    found = False
    for it in data:
        if it["expiry"] < today:
            print(f"{it['name']} expired {it['expiry'].isoformat()}")
            found = True
    if not found:
        print("No expired items.")

def expiring_soon(data, days=7):
    today = datetime.date.today()
    limit = today + datetime.timedelta(days=days)
    found = False
    for it in data:
        if today <= it["expiry"] <= limit:
            print(f"{it['name']} expiring {it['expiry'].isoformat()}")
            found = True
    if not found:
        print("No items expiring soon.")

def main():
    data = load_data()
    while True:
        print("\n1 Add  2 All  3 Expired  4 Soon  5 Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_item(data)
        elif choice == "2":
            show_all(data)
        elif choice == "3":
            show_expired(data)
        elif choice == "4":
            expiring_soon(data)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
