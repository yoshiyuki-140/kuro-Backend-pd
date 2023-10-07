# 開発者向けのREADME


## その他

- このREADMEは完全ではないです。<br>
自分なりにわかりやすく書いたつもりですが
**うまく動かない**<br>
**書いてある内容がわかんない**<br>
等あれば[https://github.com/yoshiyuki-140/CivicSeek/issues/new/choose](https://github.com/yoshiyuki-140/CivicSeek/issues/new/choose)へコメントしてください<br>
PD実践の期間内であれば読んどきます.

## Setup

1. まず自分のパソコンにgithubにあるソースコードをコピー(これをリポジトリのクローンといいます)
    ```bash
    # リポジトリクローン
    git clone https://github.com/yoshiyuki-140/CivicSeek.git
    ```

1. コピーしたフォルダに移動します
    ```bash
    # リポジトリのフォルダに移動
    cd CivicSeek
    ```

1. 仮想環境を起動します(パソコンさんによってことなる)
    1. Mac,Linux
        ```bash
        # 仮想環境用フォルダの作成
        # 実行するとvenvというフォルダが作成される
        python3 -m venv venv
        # 仮想環境起動
        ./venv/bin/activate
        ```
    1. Windowns-11
        ```powershell
        # 仮想環境用フォルダの作成
        # 実行するとvenvというフォルダが作成される
        python.exe -m venv venv
        # 仮想環境起動
        ./venv/Scripts/Activate.ps1
        # pipを最新版にアップデート
        python.exe -m pip install --upgrade pip
        ```

1. 必要なpythonパッケージを自分のパソコンに入れます

    ```bash
    pip install -r requirements.txt
    ```

1. 実行します(パソコンさんによって異なる)

    1. Mac,Linux
        ```bash
        python3 manage.py runserver
        ```

    1. Windows-11
        ```powershell
        python.exe manage.py runserver
        ```

    上記を実行したら
    http://127.0.0.1:8000/
    にアクセスしてください.
