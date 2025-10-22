# Unity WebGL + Telegram Mini App + Python Backend

Тестовое задание: интеграция Unity WebGL с Telegram Mini App и Python бэкендом.

## 🎯 Функционал
- Unity WebGL игра в Telegram Mini App
- Сохранение результатов в базу данных
- Топ-10 игроков
- Интеграция с Telegram WebApp
- Python Flask бэкенд

## 🚀 Live Demo
- **Mini App**: https://itaml.github.io/unity_testMiniApps/
- **Telegram Bot**: @myUnityGame_Bot

## 📁 Структура проекта
#/unity/Build/ # Unity WebGL build files
#/miniapp/index.html # Telegram Mini App
#/backend/app.py # Python Flask API
#/backend/requirements.txt
#/backend/schema.sql

## 🛠 Локальная разработка

### Backend
#bash
#cd backend
#pip install -r requirements.txt
#python app.py

#Бэкенд будет доступен на: http://localhost:5000

### Frontend
#cd miniapp
#python -m http.server 8000

#Mini App будет доступна на: http://localhost:8000
