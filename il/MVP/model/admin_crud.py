import sqlite3
import sys

sys.path.insert(1, 'il/MVP/')

from cogs.find_DataBase import FindDB

class AdminCRUD:
    def __init__(self, db_path = FindDB().find_database_path()):
        self.db_path = db_path

    def get_student(self):
        conn=sqlite3.connect(self.db_path)
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM students')
        result=cursor.fetchall()
        conn.close()
        return result


    def get_teachers(self):
        conn=sqlite3.connect(self.db_path)
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM teachers')
        result=cursor.fetchall()
        conn.close()
        return result

    def get_courses(self):
        conn=sqlite3.connect(self.db_path)
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM courses')
        result=cursor.fetchall()
        conn.close()
        return result

    def get_enrollments(self):
        conn=sqlite3.connect(self.db_path)
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM enrollments')
        result=cursor.fetchall()
        conn.close()
        return

    def get_user(self):
        conn=sqlite3.connect(self.db_path)
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM users')
        result=cursor.fetchall()
        conn.close()
        return result

    def create_student(self, student_id, name, age, phone, user_id):
        conn=sqlite3.connect(self.db_path)
        cursor=conn.cursor()
        cursor.execute("INSERT INTO students (student_id, name, age, phone, user_id) VALUES (student_id, name, age, phone, user_id)")
        conn.commit()
        conn.close()

    def remove_student(self, student_id):
        conn=sqlite3.connect(self.db_path)
        cursor=conn.cursor()
        cursor.execute("DELETE FROM students WHERE student_id = ? VALUES(student_id)")
        conn.commit()
        conn.close()

    def edit_student(self, student_id, name, age, phone, user_id):
        conn=sqlite3.connect(self.db_path)
        cursor=conn.cursor()
        cursor.execute("UPDATE students SET (student_id = ?, name = ?, age = ?, phone = ?, user_id = ?) VALUES(student_id, name, age, phone, user_id)")
        conn.commit()
        conn.close()