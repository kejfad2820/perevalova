import customtkinter as ctk
import sys

sys.path.insert(1, 'il/MVP/')

from view.admin_elements.admin_buttons import Buttons
from view.admin_elements.admin_tree import Tree


class Frames(ctk.CTk):
    def __init__(self, admin):
        ctk.set_default_color_theme('resource/theme/breeze.json')
        self.navigate_frame = ctk.CTkFrame(admin)
        self.navigate_frame.pack(side = 'left', fill = 'y', padx = 2)

        self.main_frame = ctk.CTkFrame(admin)
        self.main_frame.pack(side = 'right', fill = 'both', expand = True)

        self.action_frame = ctk.CTkFrame(self.main_frame)
        self.action_frame.pack(side = 'left', fill = 'y')
        self.action_label = ctk.CTkLabel(self.action_frame, text = 'Объект: ')
        self.action_label.pack(side = 'top', pady = 5)
        self.create_frame = ctk.CTkFrame(self.main_frame)

        self.Tree = Tree(self)
        self.Buttons = Buttons(self, self.Tree)

        
        
       