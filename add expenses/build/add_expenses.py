import sys
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
from tkinter.ttk import Combobox
from datetime import datetime

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
    outline="")

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    193.0,
    295.0,
    image=image_image_3)


# Button 1: Home/Dashboard
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_page(PROJECT_ROOT / "home" / "build" / "home.py", window, user_id),
    relief="flat",
    bg='#565143',
    activebackground="#565143",
)
button_1.place(
    x=20.0,
    y=121.0,
    width=110.0,
    height=30.0
)

# Button 2: Add Income
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
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
    x=20.0,
    y=193.0,
    width=188.0,
    height=44.0
)

# Button 3: Add Expenses (Current Page - Just prints)
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Already on Add Expenses"),
    relief="flat",
    bg='#757575',
    activebackground="#757575",
)
button_3.place(
    x=20.0,
    y=279.0,
    width=204.0,
    height=32.0)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    103.0,
    708.0,
    image=image_image_4
)

# Button 4: Summary
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
    847.0,
    387.0,
    image=image_image_5
)

canvas.create_text(
    560.0,
    182.0,
    anchor="nw",
    text="Date:",
    fill="#000000",
    font=("DonegalOne Regular", 24 * -1)
)
canvas.create_text(
    899.0,
    182.0,
    anchor="nw",
    text="Time:",
    fill="#000000",
    font=("DonegalOne Regular", 24 * -1)
)
canvas.create_text(
    560.0,
    278.0,
    anchor="nw",
    text="Amount:",
    fill="#000000",
    font=("DonegalOne Regular", 24 * -1)
)
canvas.create_text(
    560.0,
    385.0,
    anchor="nw",
    text="Category:",
    fill="#000000",
    font=("DonegalOne Regular", 24 * -1)
)
canvas.create_text(
    560.0,
    480.0,
    anchor="nw",
    text="Note:",
    fill="#000000",
    font=("DonegalOne Regular", 24 * -1)
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    846.0,
    104.0,
    image=image_image_6
)

# Entry 1: Date
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    704.0,
    245.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Jost Regular", 20 * -1)
)
entry_1.place(
    x=571.0,
    y=223.0,
    width=266.0,
    height=42.0
)
entry_1.insert(0, datetime.now().strftime("%Y-%m-%d"))

# Entry 2: Time
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    988.0,
    245.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Jost Regular", 20 * -1)
)
entry_2.place(
    x=909.0,
    y=223.0,
    width=158.0,
    height=42.0
)
entry_2.insert(0, datetime.now().strftime("%H:%M"))

# Entry 3: Amount
entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    704.0,
    341.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Jost Regular", 20 * -1)
)
entry_3.place(
    x=571.0,
    y=319.0,
    width=266.0,
    height=42.0
)

# Entry 4: Category
entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    704.0,
    447.0,
    image=entry_image_4
)
category_values = ["Food & Drinks", "Transportation", "Bills & Utilities", "Health", "Education", "Entertainment", "Household", "Personal Care", "Miscellaneous"]
entry_4 = Combobox(
    values=category_values,
    state="readonly",
    font=("Arial", 12)
)
entry_4.place(
    x=571.0,
    y=425.0,
    width=266.0,
    height=42.0
)

# Entry 5: Note
entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    704.0,
    542.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Jost Regular", 20 * -1)
)
entry_5.place(
    x=571.0,
    y=520.0,
    width=266.0,
    height=42.0
)

def save_expense():
    if user_id is None:
        messagebox.showerror("Error", "User not logged in!")
        return

    date = entry_1.get()
    time = entry_2.get()
    amount = entry_3.get()
    category = entry_4.get()
    note = entry_5.get()

    if amount == "" or category == "":
        messagebox.showerror("Error", "Amount and Category are required!")
        return

    try:
        conn = connect_db()
        cursor = conn.cursor()

        query = """
            INSERT INTO expense (amount, category, note, date_entry, time_entry, user_id)
            VALUES (%s, %s, %s, %s, %s, %s)
            """

        cursor.execute(query, (amount, category, note, date, time, user_id))
        conn.commit()

        messagebox.showinfo("Success", "Expense added successfully!")

        # After saving → go to home page (with user_id)
        open_page(PROJECT_ROOT / "home" / "build" / "home.py", window, user_id)

    except Exception as e:
        messagebox.showerror("Database Error", str(e))

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=save_expense,
    relief="flat",
    bg="#FDE293",
    activebackground="#FDE293",
)
button_5.place(
    x=690.0,
    y=613.0,
    width=312.0,
    height=63.0
)

window.resizable(False, False)
window.mainloop()