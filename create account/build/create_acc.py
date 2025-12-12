from pathlib import Path
from tkinter import messagebox
from db import connect_db
from session import open_page

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets/frame0")

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1280x789")
window.configure(bg = "#000000")

def create_account():
    username = entry_1.get()
    password = entry_2.get()
    confirm = entry_3.get()

    if username == "" or password == "" or confirm == "":
        messagebox.showerror("Error", "Please fill all fields")
        return

    if password != confirm:
        messagebox.showerror("Error", "Passwords do not match")
        return

    conn = connect_db()
    if conn is None:
        messagebox.showerror("Error", "Database connection failed")
        return

    cursor = conn.cursor()

    # Check if username already exists
    cursor.execute("SELECT * FROM user WHERE user_name=%s", (username,))
    exists = cursor.fetchone()

    if exists:
        messagebox.showerror("Error", "Username already exists")
        conn.close()
        return

    # Insert new user
    cursor.execute("INSERT INTO user (user_name, password) VALUES (%s, %s)",
                   (username, password))
    conn.commit()

    messagebox.showinfo("Success", "Account created successfully!")
    conn.close()

    open_page(PROJECT_ROOT / "login" / "build" / "login.py", window)



canvas = Canvas(
    window,
    bg = "#000000",
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
    298.0,
    389.0,
    image=image_image_1
)

canvas.create_text(
    95.0,
    66.0,
    anchor="nw",
    text="MoneyManage",
    fill="#FDE293",
    font=("Inter", 40 * -1)
)

canvas.create_text(
    95.0,
    247.0,
    anchor="nw",
    text="User Name",
    fill="#FFFFFF",
    font=("Jost Regular", 24 * -1)
)

canvas.create_text(
    95.0,
    167.0,
    anchor="nw",
    text="Welcome! Create an account",
    fill="#FFFFFF",
    font=("Jost Regular", 24 * -1)
)

canvas.create_text(
    95.0,
    351.0,
    anchor="nw",
    text="Password",
    fill="#FFFFFF",
    font=("Jost Regular", 24 * -1)
)

canvas.create_text(
    95.0,
    447.0,
    anchor="nw",
    text="Confirm Password",
    fill="#FFFFFF",
    font=("Jost Regular", 24 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    280.0,
    311.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Jost Regular", 24 * -1),
    show='•'
)
entry_1.place(
    x=115.0,
    y=286.0,
    width=330.0,
    height=49.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    280.0,
    414.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Jost Regular", 24 * -1),
    show='•'
)
entry_2.place(
    x=115.0,
    y=389.0,
    width=330.0,
    height=49.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    280.0,
    510.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Jost Regular", 24 * -1),
    show='•'
)
entry_3.place(
    x=115.0,
    y=485.0,
    width=330.0,
    height=49.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    874.0,
    389.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=create_account,
    relief="flat",
    bg='#4C4C4C',
    activebackground="#4C4C4C"
)
button_1.place(
    x=95.0,
    y=594.0,
    width=370.0,
    height=74.0
)


window.resizable(False, False)
window.mainloop()
