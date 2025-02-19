#		Login UI

import customkinter as ctk
from customkinter import set_default_color_theme, set_appearance_mode

from presenter.login_presenter import User_presenter

class login_view(ctk.CTK):
	def __init__(self):
		set_default_color_theme("green")
		set_appearance_mode("dark")
		self.title("Login")
		self.geometry("800x600")

		self.columnconfigure(0, weight = 1)
		self.columnconfigure(1, weight = 2)

		self.username_entry = ctk.CTkEntry(self, placeholder_text="Username/Mail")
		self.username_entry.grid(row=0, column=0, padx=5, pady=5)

		self.password_entry = ctk.CTkEntry(self, placeholder_text="Password")
		self.password_entry.grid(row=0, column=0, padx=5, pady=5)

		self.button_auth = ctk.CTkButton(self, text="Authorization")
		self.button_auth.grid(row=0, column=0, padx=5, pady=5)

		user_presenter = User_presenter(self)

		def login(self):
			username = self.username_entry.get()
			password = self.password_entry.get()
			self.presenter.login(username, password)

		def show_message(self, message):
			CTkMessagebox(title="SUCCESS", message=message, icon="check")

		def show_error(self, message):
			CTkMessagebox(title="ERROR", message=message, icon="cancel")