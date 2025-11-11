#!/usr/bin/env python3
"""
QUICK FIX - Registra immediatamente i comandi Telegram
Esegui: python3 QUICK_FIX.py
"""

import asyncio
import requests

# Token del bot (lo stesso che hai in .env)
TOKEN = "7879703909:AAFfQHlxBV-tpUeZ6leuR7YHn9VSgxSYMtE"

async def register_commands():
    """
    Registra i comandi usando l'API Telegram
    Questo non richiede setup_commands.py, agisce direttamente!
    """
    
    url = f"https://api.telegram.org/bot{TOKEN}/setMyCommands"
    
    commands = [
        {"command": "normativa", "description": "Ultimi aggiornamenti normativi"},
        {"command": "codice_civile", "description": "Modifiche Codice Civile"},
        {"command": "fiscale", "description": "Novita tributarie"},
        {"command": "crisi_impresa", "description": "Codice della Crisi d'Impresa"},
        {"command": "cerca", "description": "Ricerca normativa"},
        {"command": "archivio", "description": "Storico aggiornamenti"},
        {"command": "status", "description": "Stato agente"},
        {"command": "help", "description": "Guida ai comandi"},
        {"command": "start", "description": "Avvia il bot"},
    ]
    
    payload = {"commands": commands}
    
    try:
        print("⚡ Registrando comandi...")
        response = requests.post(url, json=payload)
        result = response.json()
        
        if result.get("ok"):
            print("✅ SUCCESSO! Comandi registrati:")
            print()
            for cmd in commands:
                print(f"  /{cmd['command']} - {cmd['description']}")
            print()
            print("🌟 Prova ora il comando: /normativa")
            print()
            print("📁 Ricorda: I comandi sono MINUSCOLI (NO /Normativa, SI /normativa)")
        else:
            print(f"❌ Errore: {result.get('description', 'Sconosciuto')}")
            
    except Exception as e:
        print(f"❌ Errore di connessione: {str(e)}")
        print("⚠️ Verifica che il token sia corretto nel file")

if __name__ == "__main__":
    print("🚀 QUICK FIX - Registrazione Comandi Telegram")
    print("="*50)
    asyncio.run(register_commands())
