import pandas as pd
from src.reader import read_excel_files
from src.cleaner import clean_data
from src.statistics import build_summary
from src.exporter import export_excel

def process_excel(input_folder: str, output_folder: str, output_file: str, config: dict, logger):
    config = dict(config)
    config["input_folder"] = input_folder
    config["output_folder"] = output_folder
    config["output_file"] = output_file

    dataframes = read_excel_files(input_folder, logger)
    if not dataframes:
        raise FileNotFoundError("输入目录中没有找到可处理的 .xlsx 文件")

    merged_df = pd.concat(dataframes, ignore_index=True)
    logger.info(f"合并完成，共 {len(merged_df)} 行")

    cleaned_df = clean_data(merged_df, config, logger)
    summaries = build_summary(cleaned_df, logger)

    output_path = export_excel(cleaned_df, summaries, output_folder, output_file, logger)

    return {
        "file_count": len(dataframes),
        "merged_rows": len(merged_df),
        "cleaned_rows": len(cleaned_df),
        "output_path": str(output_path),
        "summary_count": len(summaries),
    }
