# 🔒 Productivity Launcher

**Don't resist distraction. Kill it.**

A fullscreen focus mode for Windows built on one rule: **only what you
add exists.** Your chosen apps and websites live on a clean launcher —
everything else closes itself automatically. Getting out needs a
password that someone else keeps.

## Features

- ✅ **Whitelist mode** — no block lists. Anything you didn't allow gets closed within seconds
- 🌐 **Websites as apps** — type `https://site.com` and it opens as a clean window: no address bar, no tabs, no wandering
- 🗓️ **Built-in planner button** — pairs with [my daily planner](https://ahmed-elsayed-a.github.io) (set your own URL in `config.json`)
- 🖼️ **3 built-in wallpapers** — embedded in the app, rotate every 3 hours; or pick your own image
- 🕐 **Mond-style clock** — day, date and time in the classic Rainmeter look
- 🔑 **Family-held password** — stored as a salted hash; exit and settings are locked behind it
- 🥷 **Guardian process** — force-close the launcher and it's back in 3 seconds
- 👤 **Per-user** — runs on your Windows account only; other users on the PC are untouched

## Setup (5 minutes)

**1.** Install [Python](https://python.org/downloads) — check ✅ **"Add Python to PATH"** during install

**2.** Press `Win + R` → type `cmd` → Enter → paste → Enter:
```
pip install psutil pygetwindow pillow
```

**3.** Download these 4 files into one folder:
`launcher.py` · `guardian.py` · `SETUP.bat` · `START.bat`

**4.** Double-click **`SETUP.bat`** — the launcher opens as a normal,
free window (setup mode)

**5.** Click **⚙ Settings** (bottom-left):
- Type a website → Enter (button is named automatically)
- Or **📂 Browse .exe** to add a program
- Remember: this list is everything that will exist in focus mode

**6.** A FAMILY MEMBER types a password twice → **🔒 Set & Lock**
→ fullscreen locked mode, active from now on

**7.** Daily use: double-click **`START.bat`**
(desktop icon: right-click it → Send to → Desktop)

## Optional: Mond fonts

The clock uses **Anurati** (day) and **Quicksand** (date/time) if
installed — both free fonts. Without them it falls back to Segoe UI
cleanly. For the exact Rainmeter look: download each font → right-click
the `.ttf` → Install → restart the launcher.

## Lock it down for real (recommended)

Out of the box, the app is honor-system: you could delete its files
yourself. To make it genuinely tamper-proof, an ADMIN (family member)
does this once:

1. **Move the folder** to `C:\Program Files\ProductivityLauncher`
   (copy it there, delete the old one — needs admin approval)
2. **Update your shortcuts** (desktop + auto-start toggle: turn it
   OFF → ON once in Settings so it learns the new path)
3. **Your daily account must be a Standard user, not Administrator**
   (Settings → Accounts → Family & other users)
4. The password file lives in `C:\ProgramData\ProductivityLauncher\` —
   the admin can restrict it: right-click → Properties → Security →
   your user: Read only

Result: deleting the app, resetting the password, or killing the
protection all require the admin password — which you don't know.

## Common questions

**Forgot to add an app?** Family enters the password → Settings → add it.

**Change the password?** An admin deletes
`C:\ProgramData\ProductivityLauncher\password.dat` → open the app →
set a new one.

**Something broke?** Delete `config.json` next to the app — it rebuilds
fresh settings on next start.

**Can an expert bypass it?** A true administrator can beat ANY blocker —
Cold Turkey included. That's why step 3 above matters: no admin rights,
no bypass. The app's job is stopping *you at 1 AM*, and locked down
properly, it does 😄

## Built with

Pure Python + Tkinter. No frameworks. Wallpapers embedded as base64 —
the whole app is two files.

## License

MIT — free to use, copy, and improve.DO NOT FORGET CREADITS!
