import pandas as pd

def clean_data(df: pd.DataFrame, config: dict, logger) -> pd.DataFrame:
    before_rows = len(df)

    if config.get("drop_empty_rows", True):
        df = df.dropna(how="all")

    duplicate_subset = config.get("duplicate_subset", [])
    if duplicate_subset:
        valid_cols = [col for col in duplicate_subset if col in df.columns]
        if valid_cols:
            df = df.drop_duplicates(subset=valid_cols)
            logger.info(f"按字段去重：{valid_cols}")
        else:
            logger.warning("配置了去重字段，但表格中未找到对应字段，跳过字段去重")
    else:
        df = df.drop_duplicates()
        logger.info("未配置去重字段，按整行去重")

    for col in config.get("date_columns", []):
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce").dt.strftime("%Y-%m-%d")
            logger.info(f"统一日期格式：{col}")

    after_rows = len(df)
    logger.info(f"清洗完成：{before_rows} 行 -> {after_rows} 行")
    return df
