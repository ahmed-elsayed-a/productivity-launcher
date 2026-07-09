"""
guardian.py — THE BODYGUARD 🥷
================================
Runs quietly in the background. If launcher.py gets killed
(Task Manager, crash, anything), guardian restarts it within 3 seconds.

The only clean way to stop everything is the password inside the
launcher — which sets a "stop flag" file that guardian respects.

The stop flag lives in ProgramData (same writable home as config.json
and password.dat) because Program Files is read-only for standard users.

Run (it starts the launcher itself):
    pythonw guardian.py        <- pythonw = no console window
"""

import os
import subprocess
import sys
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LAUNCHER = os.path.join(BASE_DIR, "launcher.py")

# same writable data dir as the launcher (ProgramData, with fallback)
DATA_DIR = os.path.join(os.environ.get("ProgramData", BASE_DIR),
                        "ProductivityLauncher")
try:
    os.makedirs(DATA_DIR, exist_ok=True)
    _probe = os.path.join(DATA_DIR, ".write_test")
    with open(_probe, "w") as _f:
        _f.write("ok")
    os.remove(_probe)
except Exception:
    DATA_DIR = BASE_DIR

STOP_FLAG = os.path.join(DATA_DIR, "stop.flag")

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
        try:
            os.remove(STOP_FLAG)
        except Exception:
            pass

    start_launcher()

    while True:
        time.sleep(CHECK_EVERY)

        # clean exit? (launcher writes stop.flag after correct password)
        if os.path.exists(STOP_FLAG):
            try:
                os.remove(STOP_FLAG)
            except Exception:
                pass
            break                      # guardian retires 🫡

        # launcher killed dirty? resurrect it
        if not launcher_is_running():
            start_launcher()


if __name__ == "__main__":
    main()
