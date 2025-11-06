# 🚀 Telegram Signal Trader – MT5 Auto Trading Bot

**Fully automated bot that reads trading signals from your VIP Telegram channel/group and executes them instantly on MetaTrader 5**

```
✅ Real-time signal detection (any language, any format)
✅ Smart TP selection (TP1 or TP2 automatically)
✅ Progressive lot sizing with direction change protection
✅ 35% equity safety stop (configurable)
✅ Full Telegram control panel (/start, /stop, /baselot…)
✅ Duplicate protection + spread filter
✅ Works 24/7 on VPS or local PC
```

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Telethon](https://img.shields.io/badge/Telethon-1.36-green)
![MT5](https://img.shields.io/badge/MetaTrader5-Demo%20/%20Live-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🎯 What This Bot Does

```
VIP Telegram Channel
        │
        ▼
  New signal message
        │
        ▼
Bot parses: Action · Symbol · Entry · TP1 · TP2
        │
        ▼
 Executes trade on MT5 instantly
        │
        ▼
Sends confirmation + P&L to your private chat
```

You keep full control via Telegram commands.

---

## 📋 Table of Contents
1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Step-by-Step Setup](#step-by-step-setup)
4. [Configuration](#configuration)
5. [Running the Bot](#running-the-bot)
6. [Telegram Commands](#telegram-commands)
7. [Safety & Risk](#safety--risk)
8. [Troubleshooting](#troubleshooting)
9. [License](#license)

---

## ✨ Features

```text
• Works with ANY signal format (you can adapt the parser)
• Arabic / English / any language supported
• Smart TP1 vs TP2 decision
• Progressive lot size (martingale-style but safe)
• Auto-close opposite positions when direction changes
• Max spread filter
• Equity safety stop (default 35%)
• Duplicate signal protection
• Full remote control via Telegram
```

---

## ⚙️ Prerequisites

```bash
Python 3.10+
MetaTrader 5 terminal installed
pip install telethon python-telegram-bot MetaTrader5
```

---

## 🛠 Step-by-Step Setup (10 minutes)

### 1. Get Telegram API_ID & API_HASH
```text
1. Go → https://my.telegram.org/auth
2. Login with your phone number
3. Click "API development tools"
4. Create new application
   • App title: SignalBot
   • Short name: signalbot
   • Platform: Desktop
5. Copy API_ID and API_HASH
```

### 2. Create Your Telegram Bot (BotFather)
```text
1. Open Telegram → @BotFather
2. /newbot
3. Name: My Signal Trader
4. Username: my_signal_trader_bot
5. Copy the token → 123456789:AAFxxxxxxxxxxxxxxxx
```

### 3. Get Your VIP Channel / Group ID
**Easiest method (works for private channels):**

```text
1. Search @userinfobot
2. Tap "Start"
3. Go to your VIP channel
4. Forward ANY message from the channel → @userinfobot
5. Bot replies:
   ┌────────────────────────────────
   │ Id: -1001234567890
   └────────────────────────────────
→ Use exactly this number (including -100)
```

> Alternative bots: @getidsbot, @RawDataBot

### 4. Get Your Personal Chat ID (to receive notifications)
```text
1. Open chat with your new bot
2. Send any message (e.g. /start)
3. Open this link:
   https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates
4. Find:
   "chat":{"id":5939411038 ← this is your ID
```

---

## ⚙️ Configuration – Edit `main.py`

```python
class Config:
    BOT_TOKEN      = "123456789:AAF..."           # ← from BotFather
    SOURCE_CHANNEL = -1001234567890               # ← from step 3
    BOT_CHAT_IDS   = [5939411038]                 # ← your personal ID(s)
    API_ID         = 1234567                      # ← my.telegram.org
    API_HASH       = "0123456789abcdef0123456789abcdef"

    # MT5 Account (change to your own)
    MT5_ACCOUNT    = 5039718172
    MT5_PASSWORD   = "HvIwHa_6"
    MT5_SERVER     = "MetaQuotes-Demo"   # or your broker
    MT5_PATH       = ""                  # leave empty
```

> **SECURITY TIP**: Add these files to `.gitignore`:
> ```
> *.session
> session*
> ```

---

## 🚀 Running the Bot

```bash
# First run – will ask for phone code
python main.py
```

You will receive:
```text
✅ Listening for signals...
🤖 Simple Trading Bot Online
```

Then in your private chat with the bot:
```
/start   → activate trading
```

**For 24/7 on VPS (recommended):**

```bash
# Linux screen
screen -S signalbot
python main.py
# Ctrl+A → D to detach

# Or pm2
pip install pm2
pm2 start main.py --name "SignalBot" --interpreter python3
pm2 save
pm2 startup
```

---

## 📱 Telegram Commands – Full Remote Control

```
/start           → Activate bot
/stop            → Deactivate
/status          → Account + settings
/positions       → Open trades
/close           → Close ALL

/baselot 0.05    → Change base lot
/safety 30       → Safety stop % (5-80)
/stoploss 20     → SL points (5-100)
/spread 8        → Max spread

/smarttargets    → Toggle smart TP
/safetyoff       → Toggle safety
/help            → All commands
```

---

## ⚠️ Safety & Risk Warning

```text
• Progressive lot sizing = HIGH RISK
• Always test on DEMO account first
• 35% equity loss → automatic shutdown
• Bot can lose money faster than you can react
• Use only money you can afford to lose
• Author is NOT responsible for any losses
```

---

## 🐛 Troubleshooting

```text
Login code not received?
→ Check correct phone number at my.telegram.org

MT5 connection failed?
→ Open MT5 → Tools → Options → Expert Advisors
→ Tick "Allow DLL imports"
→ Login to your account

Signal not parsed?
→ Send me the exact message → I’ll update the parser
→ Current parser works with:
   شراء/بيع — XAUUSD
   الدخول: 2345.67
   • TP1: 2350.00
   • TP2: 2360.00
```

---

## 🤝 Contributing

```text
• Fork → improve parser for your signal format
• Add new features
• Open issues
• Pull requests welcome!
```

---

## ⭐ Star this repo if it saved you hours!

```
MIT License © 2025
Free to use, modify, and distribute.
```

---

**Made with ❤️ for VIP signal traders**

