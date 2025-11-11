#!/usr/bin/env python3
"""
Script per registrare i comandi su BotFather
Esegui questo script una sola volta per configurare i comandi
"""

import asyncio
from telegram import Bot, BotCommand

TOKEN_BOT = "7879703909:AAFfQHlxBV-tpUeZ6leuR7YHn9VSgxSYMtE"

async def setup_commands():
    """Registra i comandi per il bot"""
    bot = Bot(token=TOKEN_BOT)
    
    commands = [
        BotCommand(command="start", description="Avvia il bot"),
        BotCommand(command="normativa", description="Ultimi aggiornamenti normativi"),
        BotCommand(command="codice_civile", description="Modifiche Codice Civile"),
        BotCommand(command="fiscale", description="Novità tributarie"),
        BotCommand(command="crisi_impresa", description="Codice della Crisi d'Impresa"),
        BotCommand(command="cerca", description="Ricerca normativa"),
        BotCommand(command="archivio", description="Storico aggiornamenti"),
        BotCommand(command="status", description="Stato agente"),
        BotCommand(command="help", description="Guida ai comandi"),
    ]
    
    try:
        await bot.set_my_commands(commands)
        print("✅ Comandi registrati con successo!")
        
        # Verifica
        registered_commands = await bot.get_my_commands()
        print("\n📋 Comandi registrati:")
        for cmd in registered_commands:
            print(f"  /{cmd.command} - {cmd.description}")
    except Exception as e:
        print(f"❌ Errore: {str(e)}")

if __name__ == "__main__":
    print("🚀 Registrazione comandi in corso...")
    asyncio.run(setup_commands())
