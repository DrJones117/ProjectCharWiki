from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app, DATABASE
from flask import flash
from flask_app.models.user import User


class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.time = data['time']
        self.category = data['category']
        self.ingredients = data['ingredients']
        self.instructions = data['instructions']
        self.user_id = data['user_id']


# Posts a recipe to the logged in user
    @classmethod
    def add_recipe(cls, form):
        query = """
        INSERT INTO recipes (name, time, category, ingredients, instructions, user_id)
        VALUES (%(name)s, %(time)s, %(category)s, %(ingredients)s, %(instructions)s, %(user_id)s);
        """
        return connectToMySQL(DATABASE).query_db(query, form)

# Gets all the recipes from the logged in user
    @classmethod
    def display_recipes(cls):
        query = """
        SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        recipes = []
        if results:
            for row in results:
                recipe = cls(row)
                user_data = {
                    'id': row['id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'email': row['email'],
                    'password': row['password'],
                    'created_at': row['created_at'],
                    'updated_at': row['updated_at']
                }
                recipe.user = User(user_data)
                recipes.append(recipe)
            return recipes
        return recipes

# Validates the input when the user creates a recipe 
    @classmethod
    def validate_recipe(cls, form):
        is_valid = True
        if len(form['name']) < 2:
            flash("Please provide a recipe name.", "add_err")
            is_valid = False
        if len(form['time']) == 0:
            flash("Please give the time to make.", "add_err")
            is_valid = False
        if len(form['category']) < 2:
            flash("Please provide a category for the dish.", "add_err")
            is_valid = False
        if len(form['ingredients']) < 5:
            flash("Please give an ingredients list with measurements", "add_err")
            is_valid = False
        if len(form['instructions']) < 10:
            flash("Please provide detailed instructions", "add_err")
            is_valid = False
        return is_valid

# Gets one recipe by it's id with the data of the creator
    @classmethod
    def get_one(cls, data):
        query = """
        SELECT * FROM recipes
        JOIN users ON recipes.user_id = users.id
        WHERE recipes.id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        recipe_data = results[0]
        recipe = cls(recipe_data)
        user_data = {
            'id': recipe_data['id'],
            'first_name': recipe_data['first_name'],
            'last_name': recipe_data['last_name'],
            'email': recipe_data['email'],
            'password': recipe_data['password'],
            'created_at': recipe_data['created_at'],
            'updated_at': recipe_data['updated_at']
        }
        recipe.user = User(user_data)
        return recipe


# Updates a recipe using a given id
    @classmethod
    def update(cls, data):
        query = """
        UPDATE recipes SET 
        name = %(name)s,
        time = %(time)s,
        category = %(category)s,
        ingredients = %(ingredients)s,
        instructions = %(instructions)s
        WHERE id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results

# Deletes a recipe
    @classmethod
    def delete(cls, data):
        query = """
        DELETE FROM recipes WHERE id = %(id)s
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results


