# Excel Automation Platform

Enterprise Excel Data Processing Tool Based on Python.

## 项目介绍

企业每天会产生大量 Excel 数据，例如订单、库存、销售、客户、采购等报表。人工处理通常需要反复进行合并、去重、格式统一和统计分析，效率低且容易出错。

本项目通过 Python 实现 Excel 数据自动处理，支持批量读取、数据清洗、去重、日期格式统一、统计分析、结果导出和 GUI 图形界面操作，适用于运营、财务、采购、销售、仓库等业务场景。

## 功能

- 批量读取多个 Excel 文件
- 自动合并数据
- 删除空行
- 删除重复数据
- 统一日期格式
- 按店铺、商品生成统计结果
- 导出处理后的 Excel 文件
- 生成运行日志
- GUI 图形界面选择输入/输出目录

## 技术栈

- Python 3
- pandas
- openpyxl
- tkinter
- logging
- pathlib

## 使用方式

### 命令行运行

```bash
pip install -r requirements.txt
python main.py
```

### 图形界面运行

```bash
python gui.py
```

## 项目结构

```text
excel-automation-platform/
├── data/
├── output/
├── logs/
├── config/
│   └── config.json
├── screenshots/
├── src/
│   ├── reader.py
│   ├── cleaner.py
│   ├── exporter.py
│   ├── logger.py
│   ├── processor.py
│   └── statistics.py
├── main.py
├── gui.py
├── requirements.txt
└── README.md
```

## 后续规划

- 增加异常数据导出
- 增加更灵活的配置项
- 增加图表日报
- 打包为 Windows EXE
