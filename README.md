# 🔒 Productivity Launcher

**Don't resist distraction. Kill it.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![OS: Windows](https://img.shields.io/badge/OS-Windows-0078D4?logo=windows&logoColor=white)](https://www.microsoft.com/windows)
[![Language: Python](https://img.shields.io/badge/Language-Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)

A fullscreen focus mode for Windows built on one rule: **only what you add exists.** Your chosen apps and websites live on a clean launcher — everything else closes 
itself automatically within seconds. Getting out needs a password that someone else keeps.

<img width="1920" height="1080" alt="Screenshot (9)" src="https://github.com/user-attachments/assets/8163684d-a33f-411d-ae06-21ef64feadbb" />
*Fullscreen focus mode, locked. The counter at the top is live — every app or tab outside the whitelist gets closed automatically, and this app is counting every one it kills.*

> 🎓 **Taking a course on YouTube?** Whitelist just that one channel — not all of YouTube. Recommendations, unrelated videos, and Shorts stay locked out, so "just one video" never turns into an hour of scrolling. [See how it works ↓](#-take-a-course-not-a-rabbit-hole)

---

## ✨ Features

- 🎓 **Distraction-Free Course Links** — The standout feature: whitelist a single YouTube channel or a single course/page path instead of a whole website. Learn without the rabbit hole — recommendations, unrelated videos, and Shorts are all still blocked.
- 🎯 **Whitelist Mode** — No block lists. Anything you didn't explicitly allow gets closed within seconds.
- 🌐 **Websites as Apps** — Type `https://site.com` and it opens as a clean window: no address bar, no tabs, no wandering.
- 🗓️ **Built-in Planner Button** — Pairs with [my daily planner](https://ahmed-elsayed-a.github.io/) (set your own URL in `config.json`).
- 🖼️ **3 Built-in Wallpapers** — Embedded in the app, rotating every 3 hours; or pick your own custom image.
- 🕐 **Mond-style Clock** — Elegant day, date, and time displays in the classic minimalist Rainmeter look.
- 🔑 **Family-Held Password** — Stored safely as a salted hash. Exit and Settings are locked behind it.
- 👤 **Per-User Setup** — Runs only on your Windows account; other accounts on the PC are completely untouched.

---

## 🚀 Setup Guide (Under 2 Minutes) — Recommended

Most people should use the ready-made `.exe` — no Python, no dependencies, nothing to install.

### Step 1: Download the App

1. Go to the [**Releases**](https://github.com/ahmed-elsayed-a/productivity-launcher/releases) page.
2. Under the latest release, click **`ProductivityLauncher.exe`** to download it.

### Step 2: Save It Somewhere Permanent

Move `ProductivityLauncher.exe` into a folder you'll keep, e.g. `Documents\ProductivityLauncher\`. Don't leave it in your Downloads folder — the app stores its settings next to where it's run, and you don't want to lose them if you clean out Downloads later.

### Step 3: Run It

1. Double-click **`ProductivityLauncher.exe`**.
   > ⚠️ Windows may show a **"Windows protected your PC"** SmartScreen warning because the app isn't code-signed. Click **More info** → **Run anyway**. This is expected for a small independent project — the source code is fully open above for anyone to inspect.
2. The launcher opens as a normal, free window (Setup Mode).
3. Click the **⚙ Settings** button in the bottom-left:
   - Type a website URL → press **Enter** (the button is created and named automatically).
   - Or click **📂 Browse .exe** to select a local program.
   - _Remember: this whitelist is everything that will exist once focus mode is locked!_
4. Have a **Family Member** or friend type a lock password twice, then click **🔒 Set & Lock**. The app is now running in fullscreen locked mode!

<img width="1100" height="700" alt="setup-mode-empty(1)" src="https://github.com/user-attachments/assets/3463c745-5998-4f79-9eaa-3592fed53cfd" />
*Fresh lock — 0 distractions blocked so far. Exit and Settings are both gated behind the password you just set.*

---

## 🎓 Take a Course, Not a Rabbit Hole

**This is the feature that makes this launcher different from a plain website blocker.**

Normally, a whitelisted website is unlocked entirely — for example, adding `youtube.com` lets the whole site through, recommendations, Shorts, and all. But you can lock a website entry down to **just one specific path or one specific YouTube channel**, so you can study without opening the door to the rest of the site. Take that Udemy course, watch that YouTube lecture series, or read those docs — with zero risk of "just checking one notification" turning into an hour lost.

**Example: A specific course page or docs subsection**

1. In **⚙ Settings**, enter the exact URL of the course/page you want, e.g.:
   ```
   https://www.coursera.org/learn/machine-learning
   ```
2. Press Enter. That entry — and any page *underneath* that path (e.g. `.../machine-learning/lecture/1`) — will be reachable. Anything else on the same domain (the homepage, other courses, unrelated pages) stays blocked.

**Example: A specific YouTube channel, without Shorts**

1. In **⚙ Settings**, enter the channel's handle URL, e.g.:
   ```
   https://www.youtube.com/@3blue1brown
   ```
2. Press Enter. Now:
   - The channel's page and its videos are reachable.
   - Any individual video is checked against the channel's real ownership (via YouTube's own public metadata) before it's allowed — so a link to a video from a *different* channel won't slip through, even if it opens inside a YouTube tab.
   - **Shorts are always blocked**, even Shorts posted by the same allowed channel — no infinite-scroll rabbit hole.

<img width="544" height="697" alt="settings" src="https://github.com/user-attachments/assets/852dcb5a-83b2-40ed-8ab1-8b757f9bae62" />
*The 🔒 icon next to `@3blue1brown` and `coursera.org` marks entries locked to one channel or one path — `notion.so` below them has no restriction and stays fully open.*

> ⚠️ **Requirement:** These path/channel restrictions only work with **Google Chrome, Microsoft Edge, Brave, or Opera** set as your browser in Settings — Firefox and "System default" can only allow/block a whole domain, not a specific path or channel. See the **Frequently Asked Questions** below for why.

---

## 🖥️ Create a Desktop Shortcut for Daily Use

1. Right-click **`ProductivityLauncher.exe`**.
2. Hover over **Send to** → click **Desktop (create shortcut)**.
3. Go to your Desktop and double-click the new shortcut any time you want to launch it.

---

## 🔒 Lock It Down for Real (Un-bypassable Mode)

Out of the box, the app relies on the honor system: you could technically delete the `.exe` to exit. To make it genuinely tamper-proof, an Administrator (like a family member) can set this up once:

1. **Move the `.exe`** to a system directory, such as `C:\Program Files\ProductivityLauncher`, that requires Admin approval to modify or delete.
2. **Update your shortcut** on your desktop to point to the new path.
3. **Set your daily account as a Standard User**, not an Administrator (Settings → Accounts → Other Users).
4. **Restrict the password file**: it lives in `C:\ProgramData\ProductivityLauncher\`. The Admin can restrict it by right-clicking the folder → **Properties** → **Security** → selecting your daily Standard user account → **Edit** → checking **Deny** for "Write" and "Delete" permissions.

_Result: Deleting the app or resetting the password will now require an Administrator password — which you do not know!_

> 💡 If you're setting this up alone, the same idea still works: have someone else set both your Windows Administrator password **and** the app's lock password, so neither one is something you know.

---

## 👤 Using It Alone? (No family around)

The password locking mechanism works best when you don't know the password. If you are using this completely solo, try these clever tricks:

- **The Random Mash:** Look away from your keyboard and mash 20+ random keys into the password boxes (copy and paste the same random mash into both boxes). Click Set & Lock. Now, literally nobody on Earth knows the password!
- **The Remote Friend:** Have a friend over Discord or a phone call type a password for you and save it on their phone. They are now your virtual, remote guardian!
- **The Sealed Envelope:** Write a complex password on a physical piece of paper, seal it inside an envelope, and place it somewhere genuinely annoying to reach (like in your garage, basement, or car trunk).
  - _Why this works:_ Procrastination cravings usually last only **2–5 minutes**. Adding physical friction is often enough to outlast the craving!

---

## 💬 Frequently Asked Questions

**Q: What if I forgot to add a necessary app?**

**A:** Have your password holder enter the password on the exit screen → go to **⚙ Settings** → add the application or website.

**Q: Can an expert bypass this?**

**A:** A true Windows administrator can bypass any blocker. That is why the **Standard Account** step is highly recommended. It stops you at 1 AM when your willpower is depleted, and when locked down properly, it is incredibly secure.

**Q: Why do course/channel restrictions require Chrome, Edge, Brave, or Opera specifically?**

**A:** Those four browsers are all built on the same underlying engine (Chromium) and expose a local debugging interface the launcher uses to check every page you open in real time and close anything outside the allowed path or channel. Firefox doesn't expose that interface in current versions, so it can only be used with whole-domain website entries, not path- or channel-level restrictions.

**Q: Is the `.exe` safe if it's not code-signed?**

**A:** The `.exe` is built directly from the same source code available in this repository, so anyone can review exactly what it does. If you'd rather not trust an unsigned binary, use the **Run from Source** method below instead.

---

## 🛠️ Built With

AHMED ELSAYED, using some AI help, and:

- **Pure Python + Tkinter** — Native GUI library. No heavy frameworks, clean performance.
- **Base64 Wallpaper Embeds** — Wallpapers are completely embedded in the code, keeping the project extremely lightweight.
- **PyInstaller** — Used to package `launcher.py` into the standalone `.exe` release.

---

## 👨‍💻 Running From Source (For Developers)

If you'd rather run the Python source directly instead of the `.exe` — to inspect the code, modify it, or build your own release — here's how.

### Option A: Download the Script Directly

1. Install [Python](https://python.org/downloads).
   > ⚠️ **Important:** During installation, check the box that says **"Add Python to PATH"**!
2. Open Command Prompt (`Win + R` → type `cmd` → **Enter**) and install dependencies:
   ```
   pip install psutil pygetwindow pillow
   ```
3. Download **`launcher.py`** from this repository into its own folder.
4. Right-click **`launcher.py`** → **Open with** → **Python**.

### Option B: Clone the Repository

```
git clone https://github.com/ahmed-elsayed-a/productivity-launcher.git
cd productivity-launcher
pip install psutil pygetwindow pillow
python launcher.py
```

---

## 📄 License

Distributed under the **MIT License**. Free to use, modify, and distribute. **Please credit the original project if you share or fork it.**
