# 🔒 Productivity Launcher

A focus tool for Windows built on one rule: **only what you add exists.** 

When you lock focus mode, only your chosen apps and websites can be opened. Anything else (distracting apps, games, or social media) automatically closes within 3 seconds.

To exit focus mode or change your settings, you must enter a password.

![Screenshot (9)](https://github.com/user-attachments/assets/8163684d-a33f-411d-ae06-21ef64feadbb)
*Fullscreen focus mode, locked. The counter at the top is live — every app or tab outside the whitelist gets closed automatically, and this app is counting every one it kills.*

---

## 🌟 What Makes This Different?

Most website blockers block a list of "bad sites" but leave the rest of the internet open. This launcher does the opposite: it locks down **everything** except what you explicitly allow.

### 🎓 Study on YouTube Without Distractions
If you need to watch an educational YouTube channel (e.g., `@3blue1brown` or `@freecodecamp`) or a specific online course (e.g., on Coursera):
1. Add the specific channel or course URL in Settings.
2. The launcher will let you watch videos from **only that channel**. 
3. If you try to click a recommended video from another channel, or click on "Shorts," the tab will instantly close.

![settings](https://github.com/user-attachments/assets/852dcb5a-83b2-40ed-8ab1-8b757f9bae62)
*The 🔒 icon next to `@3blue1brown` and `coursera.org` marks entries locked to one channel or one path — normal domains stay fully open.*

---

## 🚀 Simple 3-Step Setup

No installation or technical setup is required.

### Step 1: Download the App
1. Go to the [Releases](https://github.com/ahmed-elsayed-a/productivity-launcher/releases) page.
2. Download **`ProductivityLauncher.exe`** and move it to a permanent folder (like your `Documents` folder).

### Step 2: Add Your Apps & Websites
1. Open the app. It will launch in **Setup Mode** (a normal window).
2. Click **⚙ Settings** in the bottom-left corner.
3. Paste your websites (e.g., `https://notion.so`) or click **📂 Browse .exe** to select local apps (e.g., Word, PyCharm).
4. *Tip:* Open your whitelisted websites now and log in. The app will securely remember your login sessions and active browser extensions (like ad blockers) for next time.

### Step 3: Set the Password & Lock
1. In the Settings window, have a family member, friend, or study partner type a secret password.
2. Click **🔒 Set & Lock**. 
3. Your computer is now locked in fullscreen focus mode!

![setup-mode-empty(1)](https://github.com/user-attachments/assets/3463c745-5998-4f79-9eaa-3592fed53cfd)
*Fresh lock — 0 distractions blocked so far. Exit and Settings are both gated behind the password you just set.*

---

## 🛡️ How to Make It 100% Cheat-Proof
If your willpower is low, you might be tempted to bypass the lock by deleting the app. You can make the launcher completely un-bypassable by doing this once:

1. **Move the app** to `C:\Program Files\ProductivityLauncher` (Windows requires administrator permission to delete files here).
2. **Set your daily Windows account** to a **Standard User** (not an Administrator).
3. **Change your Windows Admin password** and have a family member or friend keep it. 

*Result: You cannot delete the app, close it, or bypass the lock without the Admin password—which you do not know!*

---

## 💬 Frequently Asked Questions

### Q: Can I just close the app using Task Manager?
**A:** No. The app has a built-in "guardian" process. If you force-close the launcher from Task Manager, it will automatically detect it and reopen itself within 3 seconds. The only way to close it is to type the correct lock password.

### Q: Do I have to log in to my websites every time I use it?
**A:** No. The launcher securely saves your browser profiles in your local data folder. Your logins, cookies, and browser extensions (like ad-blockers) will stay active across sessions.

### Q: Why do course and YouTube restrictions require Chrome, Edge, Brave, or Opera?
**A:** These browsers are built on the Chromium engine. The launcher uses their built-in developer tools to inspect and close individual distracting tabs. Firefox and other browsers do not support this, so they can only allow or block a whole website domain.

### Q: Is my data safe?
**A:** Yes. The launcher is 100% private and runs entirely on your local machine. No accounts are required, and no data is ever sent to any external servers.
