import csv
import os
from datetime import date, datetime

CSV_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "expenses.csv")
FIELDNAMES = ["date", "amount", "category", "note"]


def ask_date():
    """Ask for a date in YYYY-MM-DD format. Empty input means today."""
    while True:
        text = input("日期 (YYYY-MM-DD，直接按 Enter 使用今天): ").strip()
        if not text:
            return date.today().isoformat()
        try:
            return datetime.strptime(text, "%Y-%m-%d").date().isoformat()
        except ValueError:
            print("  ✗ 日期格式錯誤，請輸入像 2026-11-24 的格式。")


def ask_amount():
    """Ask for a positive number."""
    while True:
        text = input("金額: ").strip()
        try:
            amount = float(text)
        except ValueError:
            print("  ✗ 金額必須是數字。")
            continue
        if amount <= 0:
            print("  ✗ 金額必須大於 0。")
            continue
        # Store integers without the trailing ".0"
        return int(amount) if amount.is_integer() else round(amount, 2)


def ask_category():
    """Ask for a non-empty category (stored in lowercase)."""
    while True:
        text = input("類別 (例如 food / transport / entertainment): ").strip().lower()
        if text:
            return text
        print("  ✗ 類別不可為空。")


def ask_note():
    """Optional note."""
    return input("備註 (可留空): ").strip()


def save_expense(expense, path=CSV_FILE):
    """Append one expense to the CSV file, writing the header if needed."""
    need_header = not os.path.exists(path) or os.path.getsize(path) == 0
    with open(path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        if need_header:
            writer.writeheader()
        writer.writerow(expense)


def main():
    print("=== 記帳工具：新增支出 ===")
    count = 0
    while True:
        expense = {
            "date": ask_date(),
            "amount": ask_amount(),
            "category": ask_category(),
            "note": ask_note(),
        }
        save_expense(expense)
        count += 1
        print(f"✓ 已儲存（本次共新增 {count} 筆）\n")
        again = input("繼續新增？(y/n): ").strip().lower()
        if again != "y":
            break
    print(f"完成，資料已儲存至 {CSV_FILE}")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n已中止。")
