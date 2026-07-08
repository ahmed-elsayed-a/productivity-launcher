"""
guardian.py — THE BODYGUARD 🥷
================================
Runs quietly in the background. If launcher.py gets killed
(Task Manager, crash, anything), guardian restarts it within 3 seconds.

The only clean way to stop everything is the password inside the
launcher — which sets a "stop flag" file that guardian respects.

Run (it starts the launcher itself):
    pythonw guardian.py        <- pythonw = no console window
"""

import os
import subprocess
import sys
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LAUNCHER = os.path.join(BASE_DIR, "launcher.py")
STOP_FLAG = os.path.join(BASE_DIR, "stop.flag")   # created on clean password exit

CHECK_EVERY = 3   # seconds


def launcher_is_running() -> bool:
    """Check if any python process is running launcher.py."""
    try:
        import psutil
    except ImportError:
        return False
    for proc in psutil.process_iter(["cmdline"]):
        try:
            cmd = " ".join(proc.info["cmdline"] or [])
            if "launcher.py" in cmd:
                return True
        except Exception:
            pass
    return False


def start_launcher():
    # use pythonw so no black console window appears
    python = sys.executable.replace("python.exe", "pythonw.exe")
    if not os.path.exists(python):
        python = sys.executable
    subprocess.Popen([python, LAUNCHER], cwd=BASE_DIR)


def main():
    # fresh session: remove any old stop flag
    if os.path.exists(STOP_FLAG):
        os.remove(STOP_FLAG)

    start_launcher()

    while True:
        time.sleep(CHECK_EVERY)

        # clean exit? (launcher writes stop.flag after correct password)
        if os.path.exists(STOP_FLAG):
            os.remove(STOP_FLAG)
            break                      # guardian retires 🫡

        # launcher killed dirty? resurrect it
        if not launcher_is_running():
            start_launcher()


if __name__ == "__main__":
    main()
