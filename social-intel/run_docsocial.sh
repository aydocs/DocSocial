#!/data/data/com.termux/files/usr/bin/bash

# DocsSocial - Advanced OSINT Intelligence Suite
# Created with 💜 by aydocs

clear
echo ""
echo "========================================"
echo "   🕵️ DocsSocial - Advanced OSINT"
echo "   Created with 💜 by aydocs"
echo "========================================"
echo ""

# Python ve pip kontrolü
if ! command -v python &> /dev/null; then
    echo "❌ Python yüklü değil. Kurmak için: pkg install python"
    exit 1
fi

if ! command -v pip &> /dev/null; then
    echo "❌ pip yüklü değil. Kurmak için: pip install --upgrade pip"
    exit 1
fi

# Bağımlılık kontrolü
echo "🔍 Bağımlılıklar kontrol ediliyor..."
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Tüm bağımlılıklar hazır!"
echo ""
echo "🚀 DocsSocial başlatılıyor..."
echo ""

python docsocial.py

echo ""
echo "🎉 DocsSocial tamamlandı!" 