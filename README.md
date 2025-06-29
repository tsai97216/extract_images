# 🖼️ 圖片提取器 (Image Extractor Tool)

一個簡單實用的小工具，可以快速將散落在複雜資料夾結構中的所有圖片，提取並集中到一個新的資料夾中。

> **註記**：此專案的介紹文件、部分程式碼邏輯及圖示由 **Google Gemini** 協助生成。

---

## 📖 專案簡介

您是否也曾為了整理散佈在數十個、甚至數百個子資料夾中的照片而煩惱？這個工具就是為了解決這個問題而生。它提供了一個直觀的圖形介面，讓您只需點選幾下，就能自動化完成圖片的搜尋與複製任務，大幅節省您寶貴的時間。

## ✨ 主要功能

* **圖形化介面**：無需使用任何指令，所有操作皆透過簡單的彈出視窗完成。
* **遞迴搜尋**：能自動深入所有子資料夾，找出每一張圖片。
* **智慧複製**：將所有找到的圖片複製到您指定的單一目標資料夾中。
* **自動重新命名**：若在不同資料夾中有同名檔案，程式會自動為其加上後綴 (如 `image_1.jpg`)，避免檔案被覆蓋。
* **跨平台腳本**：核心的 Python 腳本可在 Windows, macOS, Linux 上執行。
* **Windows 執行檔**：提供已打包好的 `.exe` 檔，讓沒有安裝 Python 的 Windows 使用者也能直接使用。

## 📸 畫面預覽

（建議您在此處放上一張操作過程的 GIF 動態圖）

![操作示意圖](https://i.imgur.com/8x2M6b4.gif) 
*1. 選擇來源資料夾 -> 2. 選擇目標資料夾 -> 3. 完成！*

## 🚀 如何使用

### 對於一般使用者 (Windows)

1.  前往本專案的 [Releases](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY/releases) 頁面。
2.  下載最新版本的 `Image_Extractor.exe` 檔案。
3.  直接雙擊執行，並依照視窗提示操作即可。

### 對於開發者 (從原始碼執行)

1.  確保您的電腦已安裝 Python 3。
2.  複製本專案：
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git)
    ```
3.  進入專案目錄：
    ```bash
    cd YOUR_REPOSITORY
    ```
4.  執行 Python 腳本：
    ```bash
    python extract_images.py
    ```

## 🛠️ 如何自行打包成 .exe (Windows)

如果您想修改程式碼後自行打包，請依照以下步驟：

1.  安裝 PyInstaller：
    ```bash
    py -m pip install pyinstaller
    ```
2.  在專案根目錄執行打包指令（請確保您的圖示檔 `my_icon.ico` 也在此處）：
    ```bash
    pyinstaller --onefile --windowed --icon="my_icon.ico" extract_images.py
    ```
3.  打包完成的 `.exe` 檔案會出現在 `dist` 資料夾中。

## 📝 待辦事項 (To-Do)

* [ ] 新增「移動檔案」而非「複製」的選項。
* [ ] 加入處理大型資料夾時的進度條。
* [ ] 支援更多圖片格式（例如 `.heic`, `.svg` 等）。
* [ ] 提供 macOS 版本的 `.app` 打包檔。

## 📜 授權 (License)

本專案採用 [MIT License](LICENSE) 進行授權。

---
