# 開発者向けのREADME

## 環境構築の仕方(Windows 11 ver:macのは自分で調べてくれ,linuxの設定はわかる)

1. python([長期サポート版](https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe))をインストール
1. gitを[インストール](https://github.com/git-for-windows/git/releases/download/v2.42.0.windows.2/Git-2.42.0.2-64-bit.exe)する
1. gitの設定は[git初期設定方法](https://qiita.com/ucan-lab/items/aadbedcacbc2ac86a2b3#git%E5%88%9D%E6%9C%9F%E8%A8%AD%E5%AE%9A%E6%89%8B%E9%A0%86%E5%BF%85%E9%A0%88)参照
1. powershellを開いて以下をコピペ

```powershell
# cd -> change directry:ディレクトリ移動,ここで~はホームディレクトリを表す.
cd ~
# mkdir -> make directry:ディレクトリ作成,ここではsomethingディレクトリ(フォルダ)を作成.
mkdir something
cd something
# git の プロキシ設定
git config --global http.proxy http://wwwproxy.kanazawa-it.ac.jp:8080
# プロキシ解除時は
# ```
# $ git config --global --unset http.proxy
# ```
git clone https://github.com/yoshiyuki-140/MyVimrc.git
# 今いるディレクトリの中にあるMyVimrcの中に入っている
# vimrcBackup.vimをホームディレクトリの.vimrcとしてコピーする
# Mac は bashだから(zashかも?)
# $ cp ./MyVimrc/vimrcBackup.vim ~/.vimrc
Copy-Item -Path ./MyVimrc/vimrcBackup.vim -Destination ~/.vimrc
# ローカルにリポジトリをクローン
git clone https://github.com/yoshiyuki-140/CivicSeek.git
# クローンしたリポジトリに移動
cd CivicSeek
# 仮想環境構築
pip install -virtualenv
# 仮想環境管理用のフォルダー作成
virtualenv venv
# 仮想環境起動
./venv/Script/activate.ps1
# プロキシを指定しながら,開発に必要なpythonモジュールをインストール
pip install --proxy="http://wwwproxy.kanazawa-it.ac.jp:8080" -r requirements.txt
# 仮想環境の終了
deactivate
```

# その他
- [Django管理画面のログイン方法](./Django/django_relation_doc.md)
- [バグの報告場所](https://github.com/yoshiyuki-140/CivicSeek/issues)
