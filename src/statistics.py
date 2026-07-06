def build_summary(df, logger):
    summaries = {}

    if "店铺" in df.columns and "销售额" in df.columns:
        summaries["按店铺统计"] = (
            df.groupby("店铺", as_index=False)["销售额"].sum()
            .sort_values("销售额", ascending=False)
        )
        logger.info("生成统计：按店铺统计")

    if "商品" in df.columns and "数量" in df.columns:
        summaries["按商品统计"] = (
            df.groupby("商品", as_index=False)["数量"].sum()
            .sort_values("数量", ascending=False)
        )
        logger.info("生成统计：按商品统计")

    return summaries
