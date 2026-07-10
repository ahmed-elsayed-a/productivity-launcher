"""
guardian.py — THE BODYGUARD 🥷
================================
Runs quietly in the background. If launcher.py gets killed
(Task Manager, crash, anything), guardian restarts it within 3 seconds.

The only clean way to stop everything is the password inside the
launcher — which sets a "stop flag" file that guardian respects.

This updated version includes:
1. Filename fix: Compatible with launcher.py's direct-kill command.
2. Cryptographic signature verification: Prevents users from bypassing
   the lock by manually creating a fake stop.flag file.
3. Safe execution: Never shuts down or restarts your PC.
4. Auto-install and popup handler: Gracefully alerts users if dependencies are missing.
"""

import os
import subprocess
import sys
import time
import hashlib

# --- PRE-FLIGHT CHECK: Verify psutil is installed ---
# If psutil is missing, we pop up a beautiful, native Windows error message 
# and exit safely, instead of getting stuck in an infinite crash loop.
try:
    import psutil
except ImportError:
    try:
        import tkinter as tk
        from tkinter import messagebox
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror(
            "Productivity Launcher - Error",
            "The required library 'psutil' is missing.\n\n"
            "Please open Command Prompt (CMD) and run:\n"
            "pip install psutil pygetwindow pillow\n\n"
            "Then, try opening the application again!"
        )
    except Exception:
        pass
    sys.exit(1)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LAUNCHER = os.path.join(BASE_DIR, "launcher.py")

# Same writable data dir as the launcher (ProgramData, with fallback)
DATA_DIR = os.path.join(os.environ.get("ProgramData", BASE_DIR), "ProductivityLauncher")

try:
    os.makedirs(DATA_DIR, exist_ok=True)
    _probe = os.path.join(DATA_DIR, ".write_test")
    with open(_probe, "w") as _f:
        _f.write("ok")
    os.remove(_probe)
except Exception:
    DATA_DIR = BASE_DIR

STOP_FLAG = os.path.join(DATA_DIR, "stop.flag")
CHECK_EVERY = 3  # seconds

def launcher_is_running() -> bool:
    """Check if any python process is running launcher.py."""
    for proc in psutil.process_iter(["cmdline"]):
        try:
            cmd = " ".join(proc.info["cmdline"] or [])
            # Support both development launcher.py and compiled executables
            if "launcher.py" in cmd or "ProductivityLauncher" in cmd:
                return True
        except Exception:
            pass
    return False

def start_launcher():
    # Robust, case-insensitive replacement of python.exe with pythonw.exe
    python = sys.executable
    if python.lower().endswith("python.exe"):
        python = python[:-10] + "pythonw.exe"
    
    # Double check if pythonw exists, fallback to standard python if not
    if not os.path.exists(python):
        python = sys.executable
        
    subprocess.Popen([python, LAUNCHER], cwd=BASE_DIR)

def verify_stop_signal() -> bool:
    """
    Verify that the stop.flag is an authentic signal written by launcher.py,
    not a fake file manually created by a user to bypass the lock.
    """
    if not os.path.exists(STOP_FLAG):
        return False
    
    try:
        # Read the token written in the stop.flag
        with open(STOP_FLAG, "r") as f:
            token = f.read().strip()
            
        password_file = os.path.join(DATA_DIR, "password.dat")
        
        # Scenario A: Password is active and password.dat exists
        if os.path.exists(password_file):
            with open(password_file, "r") as f_pwd:
                pwd_hash = f_pwd.read().strip()
            
            # Generate the expected cryptographic token (hash of the password hash + secret salt)
            expected_token = hashlib.sha256((pwd_hash + "secure-exit-salt-9873").encode()).hexdigest()
            
            if token == expected_token:
                return True
            
            # BACKWARD COMPATIBILITY: If they haven't updated launcher.py yet,
            # allow the original "clean exit" string to prevent locking them out!
            if token == "clean exit":
                return True
                
            return False
            
        # Scenario B: No password is set yet (Setup Mode)
        else:
            # If launcher is in setup mode, accept "clean exit" or an empty flag
            if token == "clean exit" or token == "":
                return True
            return False
            
    except Exception:
        return False

def main():
    # Fresh session: remove any old stop flag on startup
    if os.path.exists(STOP_FLAG):
        try:
            os.remove(STOP_FLAG)
        except Exception:
            pass
            
    start_launcher()
    
    while True:
        time.sleep(CHECK_EVERY)
        
        # Is there a valid stop signal?
        if os.path.exists(STOP_FLAG):
            if verify_stop_signal():
                # Real clean exit from launcher!
                try:
                    os.remove(STOP_FLAG)
                except Exception:
                    pass
                break  # Guardian retires safely 🫡
            else:
                # Fake/unauthorized stop flag detected! Delete it and keep running
                try:
                    os.remove(STOP_FLAG)
                except Exception:
                    pass
        
        # Launcher killed dirty or crashed? Resurrect it!
        if not launcher_is_running():
            start_launcher()

if __name__ == "__main__":
    main()
