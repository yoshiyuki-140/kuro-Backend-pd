# スクリプト自体のパスを取得
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
# 親ディレクトリのパスを取得
$ProjectRoot = Split-Path -Parent $ScriptDir

# config/local.py ファイルを作成
"#coding:utf-8`n" | Set-Content -Path "$ProjectRoot\config\local.py"

# SECRET_KEY を生成し、config/local.py ファイルに追加
$SecretKey = (python.exe "$ProjectRoot\setup\secret_key.py")
"SECRET_KEY=`"$SecretKey`"" | Add-Content -Path "$ProjectRoot\config\local.py"
