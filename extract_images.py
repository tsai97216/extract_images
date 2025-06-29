import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import os

def extract_all_images_to_folder():
    """
    主功能：選擇一個來源資料夾，再選擇一個目標資料夾，
    然後搜尋來源及其所有子資料夾中的圖片，並將它們全部複製到目標資料夾。
    """
    root = tk.Tk()
    root.withdraw()

    # 1. 選擇包含圖片的來源資料夾
    source_dir = filedialog.askdirectory(title="請選擇包含圖片的來源資料夾")
    if not source_dir:
        messagebox.showinfo("提示", "您沒有選擇任何來源資料夾。")
        return

    # 2. 選擇要存放所有圖片的目標資料夾
    destination_dir = filedialog.askdirectory(title="請選擇要存放所有圖片的目標資料夾")
    if not destination_dir:
        messagebox.showinfo("提示", "您沒有選擇任何目標資料夾。")
        return
        
    # 定義圖片檔案的副檔名
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')
    copied_files_count = 0
    
    # 3. 執行搜尋與複製操作
    try:
        # os.walk 會遍歷資料夾、子資料夾和檔案
        for dirpath, _, filenames in os.walk(source_dir):
            for filename in filenames:
                # 檢查檔案副檔名是否為圖片
                if filename.lower().endswith(image_extensions):
                    source_path = os.path.join(dirpath, filename)
                    destination_path = os.path.join(destination_dir, filename)
                    
                    # 如果目標資料夾已有同名檔案，可以加上編號避免覆蓋 (可選)
                    if os.path.exists(destination_path):
                        base, ext = os.path.splitext(filename)
                        i = 1
                        while os.path.exists(destination_path):
                            destination_path = os.path.join(destination_dir, f"{base}_{i}{ext}")
                            i += 1
                    
                    shutil.copy2(source_path, destination_path)
                    copied_files_count += 1
        
        success_message = f"處理完成！\n\n總共從來源資料夾中複製了 {copied_files_count} 張圖片到：\n{destination_dir}"
        messagebox.showinfo("處理完成", success_message)

    except Exception as e:
        messagebox.showerror("錯誤", f"處理過程中發生錯誤：\n{e}")

# --- 執行主程式 ---
if __name__ == "__main__":
    extract_all_images_to_folder()