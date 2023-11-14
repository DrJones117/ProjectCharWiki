from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app, DATABASE
from flask import flash
import re
from flask_bcrypt import Bcrypt  
bcrypt = Bcrypt(app)


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 



class User:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Validates the user's password
    @classmethod
    def validator(cls, form):
        is_valid = True
        if form['password'] != form['confirm_password']:
            flash("The passwords you entered don't match", "register_err")
            is_valid = False
        if cls.find_user(form['email']):
            flash("Email taken", "register_err")
            is_valid = False
        if not EMAIL_REGEX.match(form['email']): 
            flash("Invalid email address!", "register_err")
            is_valid = False
        if len(form['password']) < 8:
            flash("Password must be at least 8 characters long", "register_err")
            is_valid = False
        if len(form['first_name']) < 2:
            flash("First Name must be at least 2 characters long.", "register_err")
            is_valid = False
        if len(form['last_name']) < 2:
            flash("Last Name must be at least 2 characters long.", "register_err")
            is_valid = False
        return is_valid


    # Registers a new user
    @classmethod
    def register(cls, form):
        hash = bcrypt.generate_password_hash(form["password"])
        data = {
            **form,
            "password": hash
        }
        query = """
        INSERT INTO users (email, first_name, last_name, password)
        VALUES (%(email)s, %(first_name)s, %(last_name)s, %(password)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data)


    # Gets a single user by their id
    @classmethod
    def get_one(cls, id):
        query = """
        SELECT * FROM users WHERE id = %(id)s;
        """
        data = {
            "id": id
        }
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        else:
            return None


    # Finds a single user by there email
    @classmethod
    def find_user(cls, email):
        data = {
            "email": email
        }
        query = """
        SELECT * FROM users WHERE email = %(email)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        else:
            return False

    # Logs a user in by comparing the email and password they entered with one in the data base
    @classmethod
    def login(cls, form):
        user = cls.find_user(form['email'])
        if user:
            if bcrypt.check_password_hash(user.password, form['password']):
                return user
            else:
                flash("Bad Login", "login_err")
                return False
        else:
            flash("Bad Login", "login_err")
            return False
