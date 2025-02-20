import tkinter
from src.backend.api.pixela_api import posting_pixel, update_pixel, delete_pixel
from PIL import Image, ImageTk
import webbrowser

class MainWindow:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Habit Tracker")
        self.root.geometry("800x650")
        self.entry_add = tkinter.Entry(self.root, width=10)
        self.entry_add.place(relx=0.3, rely=0.9, anchor='center', y=-100)

        self.add_button = tkinter.Button(self.root, text="Add Today Habit", command=self.add_quantity, width=25, height=2)
        self.add_button.place(relx=0.5, rely=0.9, anchor='center', y=-100)
        
        self.delete_button = tkinter.Button(self.root, text="Delete Today Habit", command=delete_pixel, width=25, height=2)
        self.delete_button.place(relx=0.5, rely=0.9, anchor='center', y=-60)
        
        self.update_button = tkinter.Button(self.root, text="Update Today Habit", command=self.update_quantity, width=25, height=2)
        self.update_button.place(relx=0.5, rely=0.9, anchor='center', y=-20)

        self.entry_update = tkinter.Entry(self.root, width=10)
        self.entry_update.place(relx=0.3, rely=0.9, anchor='center', y=-20)

        self.stats_button = tkinter.Button(self.root, text="See my statistics", command=self.show_statistics, width=25, height=2)
        self.stats_button.place(relx=0.5, rely=0.9, anchor='center', y=20)

        image = Image.open("src/frontend/assets/pixela.png")
        resized_image = image.resize((600, 350), Image.LANCZOS)
        self.image = ImageTk.PhotoImage(resized_image)
        self.image_label = tkinter.Label(self.root, image=self.image)
        self.image_label.place(relx=0.5, rely=0.25, anchor='center', y=80)

        


        self.root.mainloop()

    def add_quantity(self):
        user_input = self.entry_add.get()
        posting_pixel(user_input)
        self.entry_add.delete(0, 'end')

    def update_quantity(self):
        user_input = self.entry_update.get()
        update_pixel(user_input)
        self.entry_update.delete(0, 'end')

    def show_statistics(self):
        webbrowser.open("https://pixe.la/v1/users/nickcj/graphs/graph1.html")
