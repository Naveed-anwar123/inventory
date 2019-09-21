@ECHO OFF
start cmd.exe /C "python manage.py runserver 
timeout 5
start "C:\Users\NaveedAnwar\AppData\Local\Google\Chrome SxS\Application\chrome.exe" "http://127.0.0.1:8000/login"