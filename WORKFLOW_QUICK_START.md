# Quick Start - GitHub Actions Manual Trigger

## ⚡ Avvia il bot Telegram in 3 passaggi

### Passo 1: Vai alla sezione Actions
Accedi al repository GitHub e clicca sulla tab **"Actions"** nella barra di navigazione superiore.

### Passo 2: Seleziona il workflow
Nella lista di sinistra, troverai **"Telegram Manual Trigger - Normativa Italiana"**. Clicca su di esso.

### Passo 3: Clicca "Run workflow" e scegli il comando

1. Vedrai un pulsante verde **"Run workflow"** sulla destra
2. Clicca su di esso
3. Nel dropdown **"Seleziona il comando da eseguire"**, scegli uno dei comandi disponibili:
   - ✅ `/fiscale` - Novità tributarie e fiscali (default)
   - ✅ `/normativa` - Aggiornamenti normativi generali
   - ✅ `/codice_civile` - Modifiche al Codice Civile
   - ✅ `/crisi_impresa` - Normativa sulla crisi d'impresa
   - ✅ `/status` - Stato del bot e diagnostica

4. Clicca il pulsante verde **"Run workflow"** per avviare

## 📊 Monitora l'esecuzione

Dopo aver cliccato "Run workflow":
- Il workflow apparirà nella lista con status **"In esecuzione"** (cerchio giallo)
- Una volta completato, vedrai **✅ Completato** (cerchio verde)
- In caso di errore, vedrai **❌ Errore** (cerchio rosso)

Clicca su qualsiasi run per visualizzare i dettagli e i log completi.

## 🔧 Configurazione iniziale (necessaria una sola volta)

### Generare il token Telegram

1. Apri Telegram e avvia una chat con **@BotFather**
2. Invia il comando: `/newbot`
3. Segui le istruzioni di BotFather per creare il bot
4. BotFather ti fornirà un **token** nel formato:
   ```
   1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgh
   ```
5. Salva questo token (lo userai nel passo successivo)

### Configurare il Secret su GitHub

1. Vai a **Settings > Secrets and variables > Actions** del repository
2. Clicca su **"New repository secret"**
3. Nome: `TELEGRAM_TOKEN`
4. Valore: Incolla il token di BotFather (da sopra)
5. Clicca **"Add secret"**

**Fatto!** Ora puoi usare il workflow con il tasto START.

## 💡 Consigli

- Il primo run potrebbe impiegare un po' di tempo (download dipendenze)
- I run successivi saranno più veloci
- Puoi visualizzare i log dettagliati cliccando sul run nella lista
- Il workflow mantiene la cronologia di tutte le esecuzioni

## 🆘 Troubleshooting

**Il pulsante "Run workflow" non appare?**
- Verifica di essere sulla pagina corretta: `/actions/workflows/telegram-manual-trigger.yml`
- Ricarica la pagina (F5)

**Errore: "TELEGRAM_TOKEN non configurato"?**
- Il secret TELEGRAM_TOKEN non è configurato
- Segui i passaggi "Configurare il Secret su GitHub" sopra

**Il workflow è rosso (errore)?**
- Clicca sul run per visualizzare i log
- Verifica che il token sia corretto
- Assicurati che il bot @StudioCappelli_bot sia attivo su Telegram

---

**Domande? Consulta il README.md per la documentazione completa.**
