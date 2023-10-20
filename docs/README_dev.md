# 開発者向けのREADME

上から目線の文言で大変恐縮ですが,メンバーの中には横文字ばかり使うと内容を把握できない人もいるのかなと思いできるだけ避けて書いたつもりです.<br>
横文字慣れている人には少し冗長だと思います.悪しからず.<br>
> P.S. dockerじゃなくてごめんよ！
> P.S. 今後docker使うかもだし、どうせデプロイの時bash使うだろうからコマンド系はbashを標準で書いときますね.
> どころころpowershell script書いてるけど別段消す必要もなかったから入れてるだけです。悪しからず.

## 開発環境構築

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
        ```

1. 必要なpythonパッケージを自分のパソコンに入れます

    ```bash
    pip install -r requirements.txt
    ```
1. local.pyの作成
    Create a file called `local.py` at `CivicSeek/config/local.py`

    ```bash
    # on CivicSeek
    touch local.py
    ```

1. SECRET_KEYの生成<br>
    # The way to generate SECRET_KEY on your laptop.

    ## Generate SECRET_KEY
    You have to move into project root Dir, In this case, you move to CivicSeek. And type the following code.

    ```bash
    $ cd CivicSeek
    $ python3 manage.py shell
    >>> from django.core.management.utils import get_random_secret_key
    >>> get_random_secret_key()
    'xxxx' <- This is generated secret key. 
    ```

    # Example
    ```bash
    > python3 manage.py shell
    Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    >>> from django.core.management.utils import get_random_secret_key
    >>> get_random_secret_key()
    '_fr91ikc^!6!pu$0-1$*ivqhm!#7d72-3!b)a53#3a5qo$-+=q'
    ```

    [ここ](./generateSECRET_KEY.md)で書いたのをはっつけた.



1. local.pyの作成&編集<br>
    local.pyの中にSECRET_KEY変数を作成し
    `get_random_secret_key()`
    の実行結果を
    SECRET_KEYに代入

    ```python
    # CivicSeek/config/local.py
    # SECRET_KEYの中身は各々異なる
    SECRET_KEY="_fr91ikc^!6!pu$0-1$*ivqhm!#7d72-3!b)a53#3a5qo$-+=q"
    ```

1. 実行します(パソコンさんによって異なる)

    1. Mac,Linux
        ```bash
        python3 manage.py migrate # create DB
        python3 manage.py runserver
        ```

    1. Windows-11
        ```powershell
        python.exe manage.py migrate # create DB
        python.exe manage.py runserver
        ```

    上記を実行したら
    http://127.0.0.1:8000/
    にアクセスしてください.
