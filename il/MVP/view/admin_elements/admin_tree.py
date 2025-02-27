import customtkinter as ctk
from tkinter import ttk


class Tree(ctk.CTk):
    def __init__(self, frames):

        self.students_tree = ttk.Treeview(frames.main_frame, columns = ('id', 'name', 'age', 'phone'), show = 'headings')
        self.students_tree.heading('id', text = 'ID')
        self.students_tree.heading('name', text = 'Имя')
        self.students_tree.heading('age', text = 'Возраст')
        self.students_tree.heading('phone', text = 'Телефон')
        self.students_tree.column('id', width = 50)
        self.students_tree.column('name', width = 50)
        self.students_tree.column('age', width = 50)
        self.students_tree.column('phone', width = 50)
        self.students_tree.bind("<<TreeviewSelect>>", self.on_select())

        self.teachers_tree = ttk.Treeview(frames.main_frame, columns = ('id', 'name', 'phone'), show = 'headings')
        self.teachers_tree.heading('id', text = 'ID')
        self.teachers_tree.heading('name', text = 'Имя')
        self.teachers_tree.heading('phone', text = 'Телефон')

    def on_select(self):
        select_item = self.students_tree.selection()
        print(select_item)
        if select_item:
            print(select_item)

