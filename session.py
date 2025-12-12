import subprocess
import sys
from pathlib import Path


def open_page(filepath, current_window=None, user_id=None):
    path = Path(filepath).resolve()

    if current_window is not None:
        try:
            current_window.destroy()
        except Exception as e:
            print("Could not destroy window:", e)

    args = [sys.executable, str(path)]
    if user_id is not None:
        args.append(str(user_id))

    try:
        subprocess.Popen(args, cwd=str(path.parent))
    except Exception as e:
        print(f"Failed to launch page: {e}")