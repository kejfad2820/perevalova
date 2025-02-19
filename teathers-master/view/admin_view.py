import tkinter.ttk as ttk
import customkinter as ctk

from presenter.admin_presenter import Admin_presenter

class Admin_view(ctk.CTk):
	def __init__(self):
		super().__init__()

		self.title("Admin")
		self.geometry("800x600")

		self.nav_frame = ctk.CTkFrame(self)
		self.nav_frame.pack(side="left", fill="y")

		self.students_btn = ctk.CTkButton(self.nav_frame, text="Students", command=lambda:self.show_students())
		self.students_btn.pack(pady=10, padx=10)

		self.main_frame = ctk.CTkFrame(self)
		self.main_frame.pack(side="right", expand=True, fill="both")

		self.presenter = Admin_presenter(self)

	def show_students(self):
		self.clear_main_frame()
		style = ttk.Style()
		style.configure("Treeview", font=("Arial", "17"))
		style.configure("Treeview.Heading", font=("Arial", "17", "bold"))
		ctk.CTkLabel(self.main_frame, text="List of students", font=("Arial", 20)).pack(pady=10)

		self.tree = ttk.Treeview(self.main_frame, columns=("ID", "Name", "Age", "Telephone", "UserID"), show="headings")
		self.tree.heading("ID", text="ID", anchor="c")
		self.tree.column("ID", width=50, anchor="c")

		self.tree.heading("Name", text="Name", anchor="c")
		self.tree.column("Name", width=240, anchor="c")

		self.tree.heading("Age", text="Age", anchor="c")
		self.tree.column("Age", width=50, anchor="c")

		self.tree.heading("Telephone", text="Telephone", anchor="c")
		self.tree.column("Telephone", width=120, anchor="c")

		self.tree.heading("UserID", text="UserID", anchor="c")
		self.tree.column("UserID", width=120, anchor="c")

		self.tree.pack(expand=True, fill="both")

		students = self_presenter.get_students()

		self.show_students_data(students)

	def show_students_data(self, students):
		self.tree.delete(*self.tree.get_children())
		print(students)
		for row in students:
			self.tree.insert("", "end", values=row)

	def show_teachers(self): pass

	def show_courses(self): pass

	def show_enrollments(self): pass

	def logout(self): pass

	def export_reports(self): pass

	def show_users(self): pass

	def clear_main_frame(self):
		for widget in self.main_frame.winfo_children():
			widget.destroy()

if __name__ == "__main__":
	app = Admin_view()
	app.mainloop()