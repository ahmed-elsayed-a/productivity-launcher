# 🔒 Productivity Launcher

**Don't resist distraction. Kill it.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![OS: Windows](https://img.shields.io/badge/OS-Windows-0078D4?logo=windows&logoColor=white)](https://www.microsoft.com/windows)
[![Language: Python](https://img.shields.io/badge/Language-Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)

A fullscreen focus mode for Windows built on one rule: **only what you add exists.** Your chosen apps and websites live on a clean launcher — everything else closes itself automatically within seconds. Getting out needs a password that someone else keeps.

---

## ✨ Features

- 🎯 **Whitelist Mode** — No block lists. Anything you didn't explicitly allow gets closed within seconds.
- 🌐 **Websites as Apps** — Type `https://site.com` and it opens as a clean window: no address bar, no tabs, no wandering.
- 🗓️ **Built-in Planner Button** — Pairs with [my daily planner](https://ahmed-elsayed-a.github.io/) (set your own URL in `config.json`).
- 🖼️ **3 Built-in Wallpapers** — Embedded in the app, rotating every 3 hours; or pick your own custom image.
- 🕐 **Mond-style Clock** — Elegant day, date, and time displays in the classic minimalist Rainmeter look.
- 🔑 **Family-Held Password** — Stored safely as a salted hash. Exit and Settings are locked behind it.
- 🥷 **Guardian Process** — If you try to force-close the launcher, the guardian process brings it right back in 3 seconds.
- 👤 **Per-User Setup** — Runs only on your Windows account; other accounts on the PC are completely untouched.

---

## 🚀 Setup Guide (Under 5 Minutes)

You only need **two files** to run this app: `launcher.py` and `guardian.py`.

### Step 1: Install Python
Download and install [Python](https://python.org/downloads). 
> ⚠️ **Important:** During installation, make sure to check the box that says **"Add Python to PATH"**!

### Step 2: Install Dependencies
Open your Command Prompt (`Win + R` → type `cmd` → press **Enter**) and paste the following command, then press **Enter**:
```bash
pip install psutil pygetwindow pillow
```

### Step 3: Download the Files
Download these two files into a single folder on your computer:
* 🖥️ **`launcher.py`**
* 🛡️ **`guardian.py`** (Note: If your file is named `guardian1.py` on GitHub, rename it to `guardian.py`!)

### Step 4: Configure & Run
1. Right-click **`launcher.py`** → click **Open with** → select **Python** (or **Python Launcher for Windows**).
2. The launcher will open as a normal, free window (Setup Mode).
3. Click the **⚙ Settings** button in the bottom-left:
   * Type a website URL → press **Enter** (the button is created and named automatically).
   * Or click **📂 Browse .exe** to select a local program.
   * *Remember: this whitelist is everything that will exist once focus mode is locked!*
4. Have a **Family Member** or friend type a lock password twice, then click **🔒 Set & Lock**. The app is now running in fullscreen locked mode!

---

## 🖥️ Create a Desktop Shortcut for Daily Use

To open the Productivity Launcher quickly every day, create a desktop shortcut:

1. Right-click **`launcher.py`** in your folder.
2. Hover over **Send to** → click **Desktop (create shortcut)**.
3. Go to your Desktop and locate the new shortcut.
4. To run it, simply double-click it! 
   * *If it doesn't open with Python by default:* Right-click the shortcut → click **Open with** → click **Choose another app** → select **Python** (and check the box that says **"Always use this app to open .py files"**).

---

## 🔒 Lock It Down for Real (Un-bypassable Mode)

Out of the box, the app relies on the honor system: you could technically delete the Python files to exit. To make it genuinely tamper-proof, an Administrator (like a family member) can set this up once:

1. **Move the folder** containing your files to a system directory, such as `C:\Program Files\ProductivityLauncher` (requires Admin approval to delete/modify files).
2. **Update your shortcut** on your desktop to point to the new path.
3. **Set your daily account as a Standard User**, not an Administrator (Settings → Accounts → Other Users).
4. **Restrict the password file**: 
   The password file lives in `C:\ProgramData\ProductivityLauncher\`. The Admin can restrict it by right-clicking the folder → clicking **Properties** → **Security** → selecting your daily Standard user account → clicking **Edit** → checking **Deny** for "Write" and "Delete" permissions.
   
*Result: Deleting the app, resetting the password, or terminating the guardian process will now require an Administrator password—which you do not know!*

---

## 👤 Using It Alone? (No family around)

The password locking mechanism works best when you don't know the password. If you are using this completely solo, try these clever tricks:

* **The Random Mash:** Look away from your keyboard and mash 20+ random keys into the password boxes (copy and paste the same random mash into both boxes). Click Set & Lock. Now, literally nobody on Earth knows the password!
* **The Remote Friend:** Have a friend over Discord or a phone call type a password for you and save it on their phone. They are now your virtual, remote guardian!
* **The Sealed Envelope:** Write a complex password on a physical piece of paper, seal it inside an envelope, and place it somewhere genuinely annoying to reach (like in your garage, basement, or car trunk). 
  * *Why this works:* Procrastination cravings usually last only **2–5 minutes**. Adding physical friction is often enough to outlast the craving!

---

## 💬 Frequently Asked Questions

**Q: What if I forgot to add a necessary app?**  
**A:** Have your password holder enter the password on the exit screen → go to **⚙ Settings** → add the application or website.

**Q: Can an expert bypass this?**  
**A:** A true Windows administrator can bypass any blocker. That is why the **Standard Account** step is highly recommended. It stops you at 1 AM when your willpower is depleted, and when locked down properly, it is incredibly secure.

---

## 🛠️ Built With

* **Pure Python + Tkinter** — Native GUI library. No heavy frameworks, clean performance.
* **Base64 Wallpaper Embeds** — Wallpapers are completely embedded in the code, keeping the project extremely lightweight.

---

## 📄 License

Distributed under the **MIT License**. Free to use, modify, and distribute. **Do not forget credits!**
