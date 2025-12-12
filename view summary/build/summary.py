import sys
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(PROJECT_ROOT))

from session import open_page
from db import connect_db, get_today_total_expenses, get_today_total_incomes


if len(sys.argv) > 1:
    try:
        user_id = int(sys.argv[1])
    except ValueError:
        user_id = None
else:
    user_id = None


if user_id is not None:
    today_total_expenses = get_today_total_expenses(user_id)
    today_total_income = get_today_total_incomes(user_id)
    today_total = today_total_income - today_total_expenses
else:
    today_total = 0

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("1280x789")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 789,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)


image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    204.0,
    394.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    171.0,
    33.0,
    image=image_image_2
)

canvas.create_rectangle(
    16.0,
    69.0,
    283.0,
    70.0,
    fill="#FFFFFF",
    outline=""
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    190.0,
    368.0,
    image=image_image_3
)

# Button 1: Home
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_page(PROJECT_ROOT / "home" / "build" / "home.py", window, user_id),
    relief="flat",
    bg="#565143",
    activebackground="#565143",
)
button_1.place(
    x=20.0,
    y=121.0,
    width=120.0,
    height=43.0
)

# Button 2: Add Income
button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_page(PROJECT_ROOT / "add income" / "build" / "add_income.py", window, user_id),
    relief="flat",
    bg="#565143",
    activebackground="#565143",
)
button_2.place(
    x=20.0,
    y=193.0,
    width=185.0,
    height=44.0
)

# Button 3: Add Expenses
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_page(PROJECT_ROOT / "add expenses" / "build" / "add_expenses.py", window, user_id),
    relief="flat",
    bg="#565143",
    activebackground="#565143",
)
button_3.place(
    x=20.0,
    y=267.0,
    width=204.0,
    height=43.0
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    103.0,
    708.0,
    image=image_image_4
)

# Button 4: Summary (Current Page)
button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Already on Summary"),
    relief="flat",
    bg="#757575",
    activebackground="#757575",
)
button_4.place(
    x=20.0,
    y=352.0,
    width=210.0,
    height=32.0
)

# Sidebar Total Label
canvas.create_rectangle(
    211.0,
    685.0,
    381.0,
    747.0,
    fill="#565143",
    outline=""
)
today_label = canvas.create_text(
    290,
    710,
    text=f"Rs. {today_total}",
    font=("DonegalOne Regular", 22),
    fill="#00A9A5"
)


image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    640.0,
    49.0,
    image=image_image_5
)

# for graphs/charts
canvas.create_rectangle(
    449.0,
    108.0,
    1243.0,
    615.0,
    fill="#FFFFFF",
    outline=""
)

# text for white space
canvas.create_text(
    846.0, 
    361.0, 
    text=".",
    fill="#CCCCCC", 
    font=("Arial", 20)
)

window.resizable(False, False)
window.mainloop()