import sys
import subprocess
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
from session import open_page


PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(PROJECT_ROOT))

from db import connect_db, get_total_income, get_total_expenses, get_today_total_expenses, get_today_total_incomes, \
    get_recent_transactions

if len(sys.argv) > 1:
    try:
        user_id = int(sys.argv[1])
    except ValueError:
        user_id = None
        print("Error: User ID is not a valid integer.")
else:
    user_id = None
    print("No user_id passed. Opened directly.")

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.geometry("1280x789")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=789,
    width=1280,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

try:
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
except Exception as e:
    print(f"Asset loading error: {e}")
    print(f"Checking path: {ASSETS_PATH}")

canvas.create_rectangle(
    16.0,
    69.0,
    283.0,
    70.0,
    fill="#FFFFFF",
    outline="")
canvas.create_rectangle(
    439.0,
    335.0,
    1228.0,
    336.0,
    fill="#0E0E0E",
    outline="")

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    193.0,
    148.0,
    image=image_image_3
)

# BUTTON 1
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Dashboard clicked"),
    relief="flat",
    bg='#757575',
    activebackground="#757575",
)
button_1.place(
    x=20.0,
    y=132.0,
    width=110.0,
    height=30.0
)

# BUTTON 2 (Add Income)
button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_page(PROJECT_ROOT / "add income" / "build" / "add_income.py", window, user_id),
    relief="flat",
    bg='#565143',
    activebackground="#565143",
)
button_2.place(
    x=10.0,
    y=193.0,
    width=200.0,
    height=44.0
)

# BUTTON 3 (Add Expenses)
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_page(PROJECT_ROOT / "add expenses" / "build" / "add_expenses.py", window, user_id),
    relief="flat",
    bg='#565143',
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

# BUTTON 4 (View Summary)
button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_page(PROJECT_ROOT / "view summary" / "build" / "summary.py", window, user_id),
    relief="flat",
    bg='#565143',
    activebackground="#565143",
)
button_4.place(
    x=20.0,
    y=339.0,
    width=210.0,
    height=46.0
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    842.0,
    163.0,
    image=image_image_5
)

canvas.create_text(
    457.0,
    54.0,
    anchor="nw",
    text="This month:",
    fill="#000000",
    font=("DonegalOne Regular", 20)
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    576.0,
    187.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    843.0,
    187.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    1110.0,
    187.0,
    image=image_image_8
)

canvas.create_text(
    535.0, 125.0,
    anchor="nw",
    text="Income",
    fill="#000",
    font=("DonegalOne Regular", 24)
)
canvas.create_text(
    788.0,
    126.0,
    anchor="nw",
    text="Expenses",
    fill="#000",
    font=("DonegalOne Regular", 24)
)
canvas.create_text(
    1065.0,
    127.0,
    anchor="nw",
    text="Balance",
    fill="#000",
    font=("DonegalOne Regular", 24)
)

canvas.create_text(
    440.0,
    306.0,
    anchor="nw",
    text="Recent Transactions",
    fill="#000000",
    font=("DonegalOne Regular", 24)
)

canvas.create_rectangle(
    491.0,
    188.0,
    661.0,
    250.0,
    fill="#D8FFDD",
    outline=""
)
income_label = canvas.create_text(
    576,
    218,
    text="0.00",
    fill="#000",
    font=("DonegalOne Regular", 22)
)

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
    text="Rs. 0",
    font=("DonegalOne Regular", 22),
    fill="#00A9A5")

canvas.create_rectangle(
    440.0,
    365.0,
    1218.0,
    638.0,
    fill="#FFFFFF",
    outline=""
)

canvas.create_rectangle(
    758.0,
    188.0,
    928.0,
    250.0,
    fill="#FFDCDC",
    outline=""
)
expenses_label = canvas.create_text(
    843,
    218,
    text="0.00",
    font=("DonegalOne Regular", 22),
    fill="#000"
)

canvas.create_rectangle(
    1025.0,
    188.0,
    1195.0,
    250.0,
    fill="#D7FDFF",
    outline=""
)
total_label = canvas.create_text(
    1110,
    218,
    text="0.00",
    font=("DonegalOne Regular", 22),
    fill="#000"
)

def load_user_data():
    if user_id is None:
        return

    try:
        total_income = get_total_income(user_id)
        total_expenses = get_total_expenses(user_id)
        monthly_total = total_income - total_expenses
        today_total_expenses = get_today_total_expenses(user_id)
        today_total_income = get_today_total_incomes(user_id)
        today_total = today_total_income - today_total_expenses
        recent = get_recent_transactions(user_id)


        canvas.itemconfig(income_label, text=f"{total_income:.2f}")
        canvas.itemconfig(expenses_label, text=f"{total_expenses:.2f}")
        canvas.itemconfig(total_label, text=f"{monthly_total:.2f}")
        canvas.itemconfig(today_label, text=f"Rs. {today_total}")

        # Recent transactions
        y_start = 380
        for row in recent:
            # Check row length to avoid errors
            if len(row) >= 3:
                cat, amt, dt = row[0], row[1], row[2]
                canvas.create_text(
                    450,
                    y_start,
                    text=f"{dt}   {cat}   Rs.{amt}",
                    anchor="nw",
                    font=("DonegalOne Regular", 18)
                )
                y_start += 30
    except Exception as e:
        print("Error loading data:", e)


load_user_data()

window.resizable(False, False)
window.mainloop()