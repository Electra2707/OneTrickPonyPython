import tkinter as tk
from PIL import ImageTk
import sqlite3
from numpy import random

BG_BISTRE = "#352208"
BG_ECRU = "#E1BB80"
BG_COYOTE = "#7b6b43"
BG_DRAB = "#685634"
BG_COYOTEE = "#806443"


def fetch_db():
    connection = sqlite3.connect("data/recipes.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sqlite_schema WHERE type='table';")
    all_tables = cursor.fetchall()

    idx = random.randint(0, len(all_tables)-1)
    table_name = all_tables[idx][1]
    cursor.execute("SELECT * FROM " + table_name + ";")
    table_records = cursor.fetchall()
    connection.close()
    return table_name, table_records


def pre_process(table_name, table_records):
    title = "".join(
        [f" {ch}" if ch.isupper() else ch for ch in table_name[:-6]])[1:]

    ingredients = []
    for i in table_records:
        name = i[1]
        qty = i[2]
        unit = i[3]
        ingredients.append(qty + " " + unit + " of " + name)
    return title, ingredients


def clear_widgets(frame, root):
    for widget in frame.winfo_children():
        widget.destroy()
    load_frame1(root)


def load_frame1(root):
    frame2 = tk.Frame(root, width=500, height=600, bg=BG_ECRU)
    frame2.tkraise()

    table_name, table_records = fetch_db()
    title, ingredients = pre_process(table_name, table_records)

    logo_img = ImageTk.PhotoImage(file="assets\RRecipe_logo_bottom.png")
    logo_wiget = tk.Label(frame2, image=logo_img, bg=BG_DRAB)
    logo_wiget.image = logo_img
    logo_wiget.pack(pady=20)

    tk.Label(
        frame2,
        text=title,
        bg=BG_BISTRE,
        fg=BG_COYOTE,
        font=("tkHeadingFont", 20)
    ).pack()

    for i in ingredients:
        tk.Label(
            frame2,
            text=i,
            bg=BG_BISTRE,
            fg=BG_COYOTE,
            font=("tkMenuFont", 12)
        )
    tk.Button(
        frame2,
        text="Back",
        font=("TkHeadingFont", 18),
        bg=BG_BISTRE,
        fg="white",
        cursor="hand2",
        activebackground=BG_DRAB,
        activeforeground="black",
        command=lambda: load_frame1(root)
    ).pack(pady=20)


def main(window_width=500, window_height=600):
    root = tk.Tk()
    root.title("Basar System")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_cordinate = (screen_width - window_width) // 2
    y_cordinate = (screen_height - window_height) // 5
    root.geometry(
        f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

    frame1 = tk.Frame(root, width=screen_width,
                      height=screen_height, bg=BG_DRAB)
    frame1.pack_propagate(False)
    frame1.pack()

    logo_img = ImageTk.PhotoImage(file="assets\RRecipe_logo.png")
    logo_wiget = tk.Label(frame1, image=logo_img, bg=BG_DRAB)
    logo_wiget.image = logo_img
    logo_wiget.pack()

    tk.Label(
        frame1,
        text="Cosas en el Inventario",
        bg=BG_BISTRE,
        fg=BG_COYOTE,
        font=("tkMenuFont", 14)
    ).pack()

    tk.Button(
        frame1,
        text="Aleatorio",
        font=("TkHeadingFont", 20),
        bg=BG_BISTRE,
        fg="white",
        cursor="hand2",
        activebackground=BG_DRAB,
        activeforeground="black",
        command=lambda: clear_widgets(frame1, root)
    ).pack(pady=20)

    frame1.tkraise()
    root.mainloop()


if __name__ == "__main__":
    main()
