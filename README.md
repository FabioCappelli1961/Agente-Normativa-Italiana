# Agente-Normativa-Italiana

Agente autonomo AI per raccolta, analisi e sintesi automatica della normativa italiana.

## Descrizione

Monitora automaticamente:
- Codice Civile
- Normativa Fiscale
- Codice della Crisi d'Impresa
- Normativa Professionale

## Fonti Monitorate

- Normattiva.it
- Gazzetta Ufficiale
- Codice Civile Online
- Studio Cataldi (RSS)
- FISCOeTASSE.com
- Indice Normativa (RSS)
- GiuriCivile
- Diritto della Crisi
- MIMIT (RSS)

## Trigger

**Telegram**: @StudioCappelli_bot (Token: 7879703909:AAFfQHlxBV-tpUeZ6leuR7YHn9VSgxSYMtE)

## Output

- Email settimanale: drcappelli1961@gmail.com
- Chatbot IA via Telegram
- Report professionale con sintesi IA

## Installazione

```bash
git clone https://github.com/FabioCappelli1961/Agente-Normativa-Italiana.git
cd Agente-Normativa-Italiana
pip install -r requirements.txt
python main.py
```

## Uso

### Comandi Telegram

- `/normativa` - Ultiaggiornamenti
- `/codice_civile` - Modifiche Codice Civile
- `/fiscale` - Novita tributarie
- `/crisi_impresa` - Codice della Crisi
- `/status` - Stato agente

## License

MIT

## Autore

Dr. Fabio Cappelli
Studio Cappelli


## GitHub Actions - Workflow Manual Trigger

### Come eseguire il bot con il tasto START

Il bot è ora controllabile direttamente da GitHub tramite un workflow con trigger manuale.

**Procedura:**

1. **Accedi al repository GitHub**: Vai a https://github.com/FabioCappelli1961/Agente-Normativa-Italiana
2. **Apri la scheda "Actions"**: Clicca sulla tab "Actions" nella barra di navigazione superiore
3. **Seleziona il workflow**: Nella lista di sinistra, clicca su "Telegram Manual Trigger - Normativa Italiana"
4. **Clicca il pulsante "Run workflow"**: Vedrai un pulsante verde con questa etichetta sulla destra
5. **Seleziona il comando**: Nel dropdown "Seleziona il comando da eseguire", scegli uno dei seguenti:
   - `/fiscale` - Novità tributarie e fiscali
   - `/normativa` - Aggiornamenti normativi generali
   - `/codice_civile` - Modifiche al Codice Civile
   - `/crisi_impresa` - Normativa sulla crisi d'impresa
   - `/status` - Stato del bot e diagnostica
6. **Avvia l'esecuzione**: Clicca il pulsante "Run workflow" verde
7. **Monitora l'esecuzione**: Il workflow apparirà nella lista e potrai vedere lo stato (In corso, Completato, Errore)

### Configurazione richiesta

Prima di poter eseguire il workflow, è necessario:

1. **Generare il token Telegram**:
   - Avvia una chat con @BotFather su Telegram
   - Usa il comando `/newbot` per creare un nuovo bot
   - Salva il token fornito (formato: `1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgh`)

2. **Aggiornare il Secret TELEGRAM_TOKEN**:
   - Vai a Settings > Secrets and variables > Actions
   - Clicca sul secret "TELEGRAM_TOKEN"
   - Aggiorna il valore con il tuo vero token da BotFather
   - Salva le modifiche

3. **Configurare il bot localmente** (opzionale per test):
   - Copia il file `.env.example` in `.env`
   - Configura le variabili d'ambiente necessarie
   - Esegui `python main.py` localmente

### Note tecniche

- Il workflow usa il trigger `workflow_dispatch` che permette di eseguire il bot manualmente da GitHub
- Tutti i comandi sono definiti nel workflow e disponibili nel dropdown
- Il bot è pre-configurato per inviare messaggi via Telegram
- Ogni esecuzione del workflow viene loggata e può essere monitorata dalla dashboard Actions

