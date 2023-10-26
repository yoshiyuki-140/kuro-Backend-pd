#!/bin/bash
# The way to tidy environmet.

PROJECT_ROOT="$(pwd)"

IP="127.0.0.1"
PORT=8000

# 開発時に有用なコード達

function run () {
    # Wsl2 only
    explorer.exe http://"$IP":"$PORT"/
    python3 "$PROJECT_ROOT"/manage.py runserver
}

function admin () {
    explorer.exe http://"$IP":"$PORT"/admin
    python3 "$PROJECT_ROOT"/manage.py runserver
}


function test () {
    python3 "$PROJECT_ROOT"/manage.py test
}

function migrate () {
    python3 "$PROJECT_ROOT"/manage.py makemigrations
    python3 "$PROJECT_ROOT"/manage.py migrate
}

alias mig="migrate"
