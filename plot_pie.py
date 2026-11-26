"""Visualization module (Member B).

Read expenses.csv and draw a pie chart of total spending per category.

Usage:
    python plot_pie.py                 # save pie_chart.png and show the window
    python plot_pie.py --no-show       # only save the image
    python plot_pie.py -i data.csv -o out.png
"""
import argparse
import csv
import os
import sys
from collections import defaultdict

import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_INPUT = os.path.join(BASE_DIR, "expenses.csv")
DEFAULT_OUTPUT = os.path.join(BASE_DIR, "pie_chart.png")

# Fonts that can display Chinese labels; matplotlib uses the first one found.
plt.rcParams["font.sans-serif"] = [
    "Microsoft JhengHei",  # Windows
    "PingFang TC",         # macOS
    "Noto Sans CJK TC",    # Linux
    "Arial Unicode MS",
    "DejaVu Sans",
]
plt.rcParams["axes.unicode_minus"] = False


def load_totals(path):
    """Return {category: total_amount}. Invalid rows are skipped with a warning."""
    if not os.path.exists(path):
        sys.exit(f"找不到資料檔 {path}，請先執行 input_expense.py 新增支出。")

    totals = defaultdict(float)
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for line_no, row in enumerate(reader, start=2):
            try:
                category = row["category"].strip()
                amount = float(row["amount"])
                if not category or amount <= 0:
                    raise ValueError
            except (KeyError, ValueError, AttributeError):
                print(f"警告：略過第 {line_no} 行（資料格式不正確）")
                continue
            totals[category] += amount

    if not totals:
        sys.exit("資料檔中沒有可用的支出資料。")
    return dict(totals)


def draw_pie(totals, output_path, show=True):
    # Largest category first
    items = sorted(totals.items(), key=lambda kv: kv[1], reverse=True)
    labels = [k for k, _ in items]
    values = [v for _, v in items]
    total = sum(values)

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.pie(
        values,
        labels=labels,
        autopct=lambda p: f"{p:.1f}%\n({p * total / 100:,.0f})",
        startangle=90,
        counterclock=False,
        wedgeprops={"edgecolor": "white"},
    )
    ax.set_title(f"支出類別比例（總計 {total:,.0f}）")
    ax.axis("equal")
    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    print(f"已儲存圖表：{output_path}")
    if show:
        plt.show()


def main():
    parser = argparse.ArgumentParser(description="Draw a pie chart of expenses by category.")
    parser.add_argument("-i", "--input", default=DEFAULT_INPUT, help="input CSV file")
    parser.add_argument("-o", "--output", default=DEFAULT_OUTPUT, help="output image file")
    parser.add_argument("--no-show", action="store_true", help="do not open a window")
    args = parser.parse_args()

    totals = load_totals(args.input)
    draw_pie(totals, args.output, show=not args.no_show)


if __name__ == "__main__":
    main()
