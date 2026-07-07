# 📊 Excel Automation Platform

> 基于 Python 开发的企业 Excel 自动化处理平台。

一个模拟企业办公场景的 Excel 自动化处理工具，支持批量读取 Excel、数据清洗、去重、统计分析、结果导出以及 GUI 图形界面操作，适用于企业数据处理及自动化办公场景。

---

# ✨ Project Features

✅ 批量导入多个 Excel 文件

✅ 自动合并 Excel 数据

✅ 删除重复记录

✅ 删除空行

✅ 标准化日期格式

✅ 按门店销售统计

✅ 按产品销售统计

✅ 导出处理后的 Excel 报告

✅ 自动生成运行日志

✅ GUI 图形界面操作

---

# 📷 Software Preview

## 图形界面

![](docs/gui.png)

---

## 数据清洗结果

![](docs/result.png)

---

## 门店销售统计

![](docs/sheet1.png)

---

## 产品销售统计

![](docs/sheet2.png)

---

# 📁 Workflow

```
Excel Files
      │
      ▼
Batch Read
      │
      ▼
Merge Data
      │
      ▼
Data Cleaning
 ├─────────────┐
 ▼             ▼
Remove       Date Format
Duplicate
      │
      ▼
Statistics
      │
      ▼
Export Excel
      │
      ▼
Generate Log
```

---

# 📂 Project Structure

```
excel-automation-platform/

├── config/
│   └── config.json
│
├── docs/
│   ├── gui.png
│   ├── result.png
│   ├── sheet1.png
│   └── sheet2.png
│
├── src/
│   ├── reader.py
│   ├── cleaner.py
│   ├── exporter.py
│   ├── logger.py
│   ├── processor.py
│   ├── statistics.py
│   └── __init__.py
│
├── gui.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🔧 Technology Stack

| 技术 | 说明 |
|------|------|
| Python | 开发语言 |
| Pandas | Excel 数据处理 |
| OpenPyXL | Excel 文件读写 |
| Tkinter | GUI 图形界面 |
| Logging | 日志记录 |
| JSON | 配置管理 |

---

# 🚀 Quick Start

## 1. 安装依赖

```bash
pip install -r requirements.txt
```

---

## 2. 启动 GUI

```bash
python gui.py
```

---

## 3. 命令行运行

```bash
python main.py
```

---

# 💼 Business Scenario

本项目模拟企业日常 Excel 数据处理流程。

适用于：

- ERP 数据整理
- 财务数据汇总
- 销售统计分析
- 门店经营分析
- Excel 自动化办公
- 数据清洗
- 数据统计报表

典型流程：

```
批量读取 Excel
        │
        ▼
自动合并
        │
        ▼
数据清洗
        │
        ▼
删除重复
        │
        ▼
统计分析
        │
        ▼
导出 Excel
        │
        ▼
生成运行日志
```

---

# ⭐ Project Highlights

- 模块化项目架构
- GUI 桌面工具
- Excel 自动化处理
- Pandas 数据分析
- OpenPyXL 文件操作
- 数据清洗
- 销售统计分析
- 自动生成日志
- 企业级目录结构
- Python 自动化开发

---

# 📈 Project Result

✔ 成功批量读取 Excel

✔ 自动完成数据清洗

✔ 自动删除重复记录

✔ 自动统计销售数据

✔ 自动导出 Excel

✔ GUI 图形界面操作

✔ 自动生成运行日志

✔ 模块化代码设计

---

# 👨‍💻 Author

Joy Wang

GitHub：

https://github.com/wjoy00337-debug
