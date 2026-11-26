# Expense Tracker（記帳工具）

簡單的命令列記帳工具：輸入每筆支出，並依類別產生圓餅圖。

## 組員與分工

| 成員 | GitHub | 負責模組 | 分支 |
|---|---|---|---|
| 鄭宇宬 | @aclonemen69420 | 輸入模組 `input_expense.py` | `Input` |
| 顏培帆 | @baconyen | 視覺化模組 `plot_pie.py` | `piechart` |

## 環境需求

- Python 3.8 以上
- matplotlib

## 安裝

```bash
git clone https://github.com/aclonemen69420/SE_expense.git
cd SE_expense
pip install -r requirements.txt
```

## 使用方式

### 1. 新增支出（輸入模組）

```bash
python input_expense.py
```

依提示輸入日期、金額、類別與備註（備註可留空）。日期直接按 Enter 代表今天；
輸入錯誤的日期或金額會要求重新輸入。每筆資料會**附加**到 `expenses.csv`。

範例：

```
日期 (YYYY-MM-DD，直接按 Enter 使用今天): 2026-11-24
金額: 120
類別 (例如 food / transport / entertainment): food
備註 (可留空): 午餐便當
✓ 已儲存（本次共新增 1 筆）
繼續新增？(y/n): n
```

### 2. 產生圓餅圖（視覺化模組）

```bash
python plot_pie.py
```

會讀取 `expenses.csv`，依類別加總金額，存成 `pie_chart.png` 並開啟圖表視窗。

可選參數：

| 參數 | 說明 |
|---|---|
| `--no-show` | 只存圖片，不開視窗 |
| `-i FILE` | 指定輸入的 CSV |
| `-o FILE` | 指定輸出的圖片檔名 |

## 資料格式

`expenses.csv`（UTF-8，含標題列）：

| 欄位 | 必填 | 說明 |
|---|---|---|
| `date` | 是 | `YYYY-MM-DD` |
| `amount` | 是 | 大於 0 的數字 |
| `category` | 是 | 類別名稱（自動轉小寫） |
| `note` | 否 | 備註 |


## 專案結構

```
expense-tracker/
├── input_expense.py   # 輸入模組
├── plot_pie.py        # 視覺化模組
├── expenses.csv       # 範例資料 會在輸入資料後產生
├── requirements.txt
└── README.md
```

