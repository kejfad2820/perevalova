from MVP.model.user_crud import UserCRUD
from MVP.view.admin_view import AdminVIEW


class LoginPRESENTER:
    def __init__(self, view):
        self.UserCRUD = UserCRUD()
        self.view = view
        self.attempts = {}

    def login(self, username, password):
        user = self.UserCRUD.get_user(username)

        if user:
            user_password = user[0][2]
            user_role = user[0][3]
            user_ban = user[0][4]

            if user_ban == 1:
                self.view.show_message("Вы забанены!!!")
            else:


                if user_password == password:
                    self.open_dashboard(user_role, username)
                    return True


                else:
                    if username in self.attempts:
                        self.attempts[username] += 1

                        if self.attempts[username]: self.UserCRUD.ban_user(username)

                    else: self.attempts[username] = 1

    def open_dashboard(self, role, username):
        if role == 'admin':
            admin = AdminVIEW(username, role)
            self.view.withdraw()
            admin.focus()








