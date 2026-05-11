# Smart Health-Sync 🏃‍♂️
智慧化個人健康與運動策略系統

## 專案簡介
本系統透過使用者輸入的生理數據，自動計算能量代謝指標（BMR、TDEE、BMI），
並利用機器學習模型預測健康風險，提供客製化的飲食建議與運動處方。

---

## 環境需求
- Python 3.10
- Git

---

## 安裝步驟

### 1. Clone 專案
```bash
git clone https://github.com/你的帳號/smart_health.git
cd SMART_HEALTH
```

### 2. 建立虛擬環境
```bash
python -m venv venv
```

### 3. 啟動虛擬環境
```bash
# Windows (Git Bash)
source venv/Scripts/activate

# Mac / Linux
source venv/bin/activate
```

> 成功後 terminal 左邊會出現 `(venv)` 字樣

### 4. 安裝套件
```bash
pip install -r requirements.txt
```

### 5. 設定 VSCode 直譯器（第一次使用需要）
1. 按 `Ctrl+Shift+P`
2. 搜尋 `Python: Select Interpreter`
3. 選擇 `Python 3.10.11 (venv) .\venv\Scripts\python.exe`（標示 Recommended 的那個）

---

## 執行方式

### 測試基礎計算模組
```bash
python src/calculator.py
```

### 執行主程式
```bash
python main.py
```

---

## 專案結構
```
smart_health/
├── data/               # 資料集放這裡（不上傳至 GitHub）
├── notebooks/
│   └── eda.ipynb       # 探索性資料分析
├── src/
│   ├── calculator.py   # BMR / TDEE / BMI 計算
│   ├── data_loader.py  # 資料載入與清理
│   └── user_input.py   # 使用者輸入介面
├── main.py
├── requirements.txt
└── README.md
```

---

## 資料集
請至 Kaggle 下載 [Body Fat Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/body-fat-prediction-dataset)，
下載後將 `.csv` 檔放入 `data/` 資料夾。

> ⚠️ `data/` 資料夾不會上傳至 GitHub，每位組員需自行下載。

---

## 注意事項
- 每次開啟新的 terminal 都需要重新啟動虛擬環境（步驟 3）
- 不要將 `venv/` 資料夾上傳至 GitHub（已加入 `.gitignore`）