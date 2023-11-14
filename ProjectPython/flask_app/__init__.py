from flask import Flask, session
DATABASE = "virtual_recipe_db"
app = Flask(__name__)
app.secret_key = "shhhh"