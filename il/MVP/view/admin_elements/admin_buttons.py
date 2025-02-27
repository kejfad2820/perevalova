import customtkinter as ctk
import sys

sys.path.insert(1, 'il/MVP/')

from presenter.admin_presenter import AdminPRESENTER


class Buttons(ctk.CTk):
    def __init__(self, frames, tree):
        self.frames = frames
        self.tree = tree
        self.admin = AdminPRESENTER()
        self.current_presenter = None

        self.students_btn = ctk.CTkButton(self.frames.navigate_frame, text = 'Студенты', command = self.show_students)
        self.students_btn.pack(padx = 5, pady = 3)

        self.teachers_btn = ctk.CTkButton(self.frames.navigate_frame, text = 'Преподаватели', command = self.show_teachers)
        self.teachers_btn.pack(padx = 5, pady = 3)

        self.course_btn = ctk.CTkButton(self.frames.navigate_frame, text = 'Курсы')
        self.course_btn.pack(padx = 5, pady = 3)

        self.record_btn = ctk.CTkButton(self.frames.navigate_frame, text = 'Записи')
        self.record_btn.pack(padx = 5, pady = 3)

        self.report_btn = ctk.CTkButton(self.frames.navigate_frame, text = 'Отчёты')
        self.report_btn.pack(padx = 5, pady = 3)

        self.close_btn = ctk.CTkButton(self.frames.navigate_frame, text = 'Выйти', command = self.on_close)
        self.close_btn.pack(side = 'bottom', pady = 3)

        self.edit_btn = ctk.CTkButton(self.frames.action_frame, text="Редактировать", command = self.create_entry)
        self.edit_btn.pack()

        self.create_btn = ctk.CTkButton(self.frames.action_frame, text="Создать", command=self.create_entry)
        self.create_btn.pack()

        self.remove_btn = ctk.CTkButton(self.frames.action_frame, text="Удалить", command=self.remove_entry)
        self.remove_btn.pack()

        self.complete_btn = ctk.CTkButton(self.frames.create_frame, text="Применить", command=self.close_entry)
   

        

    def on_close(self):
        self.frames.main_frame.quit()

    def show_students(self):
        for widget in self.frames.main_frame.winfo_children():
            if widget != self.frames.action_frame:

                widget.pack_forget()
        students = self.admin.get_students()
        self.tree.students_tree.delete(*self.tree.students_tree.get_children())
        self.current_presenter = self.tree.students_tree
        for row in students:
            self.tree.students_tree.insert("", "end", values = row)
        self.tree.students_tree.pack(side = 'left', fill = 'both', expand = True)

    def show_teachers(self):
        for widget in self.frames.main_frame.winfo_children():
            if widget != self.frames.action_frame:

                widget.pack_forget()

        self.tree.teachers_tree.pack(side = 'left', fill = 'both', expand = True)
        self.current_presenter = self.tree.teachers_tree

    def create_entry(self):
        self.frames.create_frame.pack()
        self.complete_btn.pack()

    def remove_entry(self):
        pass

    def edit_entry(self):
        self.frames.edit_frame.pack()
        self.complete_btn.pack()

    def close_entry(self):
        self.frames.create_frame.destroy()


