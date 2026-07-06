from pathlib import Path
import pandas as pd

def read_excel_files(input_folder: str, logger):
    folder = Path(input_folder)
    files = list(folder.glob("*.xlsx"))

    if not files:
        logger.warning(f"未找到Excel文件：{folder.resolve()}")
        return []

    dataframes = []
    for file in files:
        try:
            df = pd.read_excel(file)
            df["来源文件"] = file.name
            dataframes.append(df)
            logger.info(f"读取成功：{file.name}，{len(df)} 行")
        except Exception as e:
            logger.exception(f"读取失败：{file.name}，原因：{e}")

    return dataframes
