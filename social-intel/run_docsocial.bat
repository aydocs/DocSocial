@echo off
title DocsSocial - Advanced OSINT Intelligence Suite
color 0B

echo.
echo ========================================
echo    🕵️ DocsSocial - Advanced OSINT
echo    Created with 💜 by aydocs
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

REM Check if requirements are installed
echo 🔍 Checking dependencies...
pip show requests >nul 2>&1
if errorlevel 1 (
    echo 📦 Installing required packages...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ❌ Failed to install dependencies
        pause
        exit /b 1
    )
)

echo ✅ All dependencies are ready!
echo.
echo 🚀 Starting DocsSocial...
echo.

REM Run DocsSocial
python docsocial.py

echo.
echo 🎉 DocsSocial completed!
pause 