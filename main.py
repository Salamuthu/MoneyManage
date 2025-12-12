import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.append(str(PROJECT_ROOT))

from login.build.login import window as login_window

if __name__ == "__main__":
    login_window.mainloop()

