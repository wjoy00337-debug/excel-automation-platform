import json
import threading
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from src.logger import setup_logger
from src.processor import process_excel

class ExcelAutomationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Excel Automation Platform v1.1")
        self.root.geometry("760x520")
        self.input_var = tk.StringVar(value=str(Path("data").resolve()))
        self.output_var = tk.StringVar(value=str(Path("output").resolve()))
        self.output_file_var = tk.StringVar(value="merged_result.xlsx")
        self.build_ui()

    def build_ui(self):
        tk.Label(self.root, text="Excel Automation Platform", font=("Microsoft YaHei UI", 18, "bold")).pack(pady=15)
        tk.Label(self.root, text="企业 Excel 数据自动处理工具：批量合并、清洗、统计、导出", font=("Microsoft YaHei UI", 10)).pack(pady=5)
        frame = tk.Frame(self.root)
        frame.pack(fill="x", padx=30, pady=10)
        tk.Label(frame, text="输入目录：", width=12, anchor="w").grid(row=0, column=0, pady=8)
        tk.Entry(frame, textvariable=self.input_var, width=70).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="浏览", command=self.choose_input).grid(row=0, column=2)
        tk.Label(frame, text="输出目录：", width=12, anchor="w").grid(row=1, column=0, pady=8)
        tk.Entry(frame, textvariable=self.output_var, width=70).grid(row=1, column=1, padx=5)
        tk.Button(frame, text="浏览", command=self.choose_output).grid(row=1, column=2)
        tk.Label(frame, text="输出文件名：", width=12, anchor="w").grid(row=2, column=0, pady=8)
        tk.Entry(frame, textvariable=self.output_file_var, width=70).grid(row=2, column=1, padx=5)
        self.start_button = tk.Button(self.root, text="开始处理", font=("Microsoft YaHei UI", 12, "bold"), width=18, height=2, command=self.start_process)
        self.start_button.pack(pady=10)
        tk.Label(self.root, text="运行日志：", anchor="w").pack(fill="x", padx=30)
        self.log_box = scrolledtext.ScrolledText(self.root, height=14)
        self.log_box.pack(fill="both", expand=True, padx=30, pady=10)

    def choose_input(self):
        folder = filedialog.askdirectory()
        if folder:
            self.input_var.set(folder)

    def choose_output(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_var.set(folder)

    def write_log(self, message):
        self.log_box.insert(tk.END, message + "\n")
        self.log_box.see(tk.END)
        self.root.update_idletasks()

    def load_config(self):
        config_path = Path("config") / "config.json"
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def start_process(self):
        self.start_button.config(state="disabled")
        self.log_box.delete("1.0", tk.END)
        thread = threading.Thread(target=self.run_process)
        thread.daemon = True
        thread.start()

    def run_process(self):
        try:
            input_folder = self.input_var.get()
            output_folder = self.output_var.get()
            output_file = self.output_file_var.get()
            if not output_file.endswith(".xlsx"):
                output_file += ".xlsx"
            self.write_log("程序启动...")
            self.write_log(f"输入目录：{input_folder}")
            self.write_log(f"输出目录：{output_folder}")
            logger = setup_logger()
            config = self.load_config()
            result = process_excel(input_folder, output_folder, output_file, config, logger)
            self.write_log("处理完成！")
            self.write_log(f"读取文件数：{result['file_count']}")
            self.write_log(f"合并行数：{result['merged_rows']}")
            self.write_log(f"清洗后行数：{result['cleaned_rows']}")
            self.write_log(f"统计Sheet数量：{result['summary_count']}")
            self.write_log(f"输出文件：{result['output_path']}")
            messagebox.showinfo("处理完成", f"处理完成！\n\n输出文件：\n{result['output_path']}")
        except Exception as e:
            self.write_log(f"处理失败：{e}")
            messagebox.showerror("处理失败", str(e))
        finally:
            self.start_button.config(state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExcelAutomationApp(root)
    root.mainloop()
