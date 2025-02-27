import customtkinter as ctk
import tkinter.ttk as ttk
import sys

sys.path.insert(1, 'il/MVP/')

from presenter.admin_presenter import AdminPRESENTER
from view.admin_elements.admin_frames import Frames


class AdminVIEW(ctk.CTk):
    def __init__(self, username, role):
        super().__init__()
        self.frames = Frames(self)

        self.adminPRESENTER = AdminPRESENTER()

        self.geometry('900x450')
        self.title(f"Пользователь: {username} Доступ: {role}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('resource/theme/breeze.json')


    def on_closing(self):
        self.quit()