@echo off
call venv\Scripts\activate
call pyside6-uic MisraGui/form.ui -o MisraGui/ui_form.py
python MisraGui/mainwindow.py