import json
from pathlib import Path
from src.logger import setup_logger
from src.processor import process_excel

def load_config():
    config_path = Path("config") / "config.json"
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    logger = setup_logger()
    config = load_config()
    logger.info("Excel Automation Platform 启动")
    result = process_excel(
        input_folder=config["input_folder"],
        output_folder=config["output_folder"],
        output_file=config["output_file"],
        config=config,
        logger=logger,
    )
    logger.info(f"处理完成：{result}")

if __name__ == "__main__":
    main()
