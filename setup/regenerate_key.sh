#!/bin/bash

# このスクリプト自体のパスをget
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# 親ディレクトリのパスを取得
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"


echo "#coding:utf-8" > "$PROJECT_ROOT/config/local.py"
echo "SECRET_KEY=\"$(python3 "$PROJECT_ROOT"/setup/secret_key.py)\"" >> "$PROJECT_ROOT"/config/local.py

