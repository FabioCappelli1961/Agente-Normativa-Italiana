#!/bin/bash

# Script di installazione e setup automatico
# Agente Normativa Italiana

echo "========================================"
echo "🚀 AGENTE NORMATIVA ITALIANA - SETUP"
echo "========================================"
echo ""

# Step 1: Controlla Python
echo "[1/4] Verificando Python..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 non trovato. Installa Python 3.9+"
    exit 1
fi
echo "✅ Python trovato: $(python3 --version)"
echo ""

# Step 2: Crea virtual environment
echo "[2/4] Creando virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment creato"
else
    echo "✅ Virtual environment già presente"
fi
echo ""

# Step 3: Attiva virtual environment e installa dipendenze
echo "[3/4] Installando dipendenze..."
source venv/bin/activate
pip install --upgrade pip &> /dev/null
pip install -r requirements.txt
echo "✅ Dipendenze installate"
echo ""

# Step 4: Registra comandi Telegram
echo "[4/4] Registrando comandi Telegram..."
python3 setup_commands.py
echo ""

echo "========================================"
echo "✅ SETUP COMPLETATO!"
echo "========================================"
echo ""
echo "Prossimi step:"
echo "1. Copia il file .env.example in .env"
echo "2. Compila .env con le tue credenziali"
echo "3. Avvia l'agente: python3 main.py"
echo ""
echo "Repository: https://github.com/FabioCappelli1961/Agente-Normativa-Italiana"
echo "Bot Telegram: @StudioCappelli_bot"
echo ""
