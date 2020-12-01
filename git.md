# Git

git，關於這個音訊檔 音訊 說明·資訊，吉特）是一個分散式版本控制軟體，最初由林納斯·托瓦茲創作，於2005年以GPL釋出。最初目的是為更好地管理Linux核心開發而設計。在程式設計中，分散式版本控制（英語：distributed revision control 或 distributed version control，又譯為分布式版本控制），又稱去中心化版本控制（decentralized version control），是一種版本控制的方式，它允許軟體開發者可以共同參與一個軟體開發專案，但是不必在相同的網路系統下工作。其作法是在每個開發者電腦中複製一份完整的代碼庫以及完整歷史。因此在無法連接網路時，仍可以進行軟體的分支及合併，可以加速大部份的作業，增加此情形可以進行的工作，而且系統的代碼庫可以在多家電腦上備份，不需靠單一位置的備份。而多個位置的代碼庫再透過其他機制來達到同步。

## 環境設定

下載[git](https://github.com/git-for-windows/git/releases/download/v2.29.2.windows.2/Git-2.29.2.2-64-bit.exe)
安裝git相關資料

## 設定使用者

```sh
git config --global user.name "User name"
git config --global user.email "User@email.address"
```

## 開始使用

今日練習檔案連結如下
https://github.com/NUUEO/practice_1201.git

1. 開啟終端機
2. 輸入下列指令
   ```sh
   git clone https://github.com/NUUEO/practice_1201.git
   ```
   將相關內容下載置自己的電腦桌面
3. 利用 `cd` 指令切換至homework資料夾
   ```sh
   cd homework
   ```
4. 使用 `add` 指令新增欲上傳至github的文件
   ```sh
   git add 學號.py
   ```
5. 使用 `commit`指令說明新增內容之相關說明
6. 利用vi編輯器按下`i`進行編輯，編輯完成後按下`esc`退出編輯模式並輸入`:wq`儲存後關閉
7. 使用`push`指令將自己完成的程式碼推送至github
8. 使用`pull`指令更新該git庫相關內容（可以看其他人的上傳）