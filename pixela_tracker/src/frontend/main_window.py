import tkinter
from src.backend.api.pixela_api import create_account, create_graph, posting_pixel, update_pixel, delete_pixel
from PIL import Image, ImageTk

class MainWindow:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Habit Tracker")
        self.root.geometry("800x600")
        self.add_button = tkinter.Button(self.root, text="Add Today Habit", command=posting_pixel, width=25, height=2)
        self.add_button.place(relx=0.5, rely=0.9, anchor='center', y=-70)
        
        self.delete_button = tkinter.Button(self.root, text="Delete Today Habit", command=delete_pixel, width=25, height=2)
        self.delete_button.place(relx=0.5, rely=0.9, anchor='center', y=-30)
        
        self.update_button = tkinter.Button(self.root, text="Update Today Habit", command=update_pixel, width=25, height=2)
        self.update_button.place(relx=0.5, rely=0.9, anchor='center', y=10)

        image = Image.open("src/frontend/assets/pixela.png")
        resized_image = image.resize((600, 350), Image.LANCZOS)
        self.image = ImageTk.PhotoImage(resized_image)
        self.image_label = tkinter.Label(self.root, image=self.image)
        self.image_label.place(relx=0.5, rely=0.25, anchor='center', y=80)

        self.root.mainloop()
