from pathlib import Path
import pandas as pd

def export_excel(df, summaries: dict, output_folder: str, output_file: str, logger):
    Path(output_folder).mkdir(parents=True, exist_ok=True)
    output_path = Path(output_folder) / output_file

    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="清洗后数据", index=False)
        for sheet_name, summary_df in summaries.items():
            summary_df.to_excel(writer, sheet_name=sheet_name, index=False)

    logger.info(f"导出成功：{output_path.resolve()}")
    return output_path
