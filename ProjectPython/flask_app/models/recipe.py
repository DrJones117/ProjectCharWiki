from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app, DATABASE
from flask import flash
from flask_app.models.user import User


class Recipe:
    def _init_(self, data):
        self.id = data['id']
        self.name = data['name']
        self.time = data['time']
        self.ingredients = data['ingredients']
        self.instructions = data['instructions']
        self.user_id = data['user_id']
        self.user_like_id['user_like_id']


#     # Posts a recipe to the logged in user
#     @classmethod
#     def add_sasquatch(cls, form):
#         query = """
#         INSERT INTO sasquatches (location, date_sighted, number_of, notes, user_id)
#         VALUES (%(location)s, %(date_sighted)s, %(number_of)s, %(notes)s, %(user_id)s);
#         """
#         return connectToMySQL(DATABASE).query_db(query, form)

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

#     # Gets one sasquatch by it's id with the data of the creator
#     @classmethod
#     def get_one(cls, data):
#         query = """
#         SELECT * FROM sasquatches
#         JOIN users ON sasquatches.user_id = users.id
#         WHERE sasquatches.id = %(id)s;
#         """
#         results = connectToMySQL(DATABASE).query_db(query, data)
#         sasquatch_data = results[0]
#         sasquatch = cls(sasquatch_data)
            
#         user_data = {
#             'id': sasquatch_data['id'],
#             'first_name': sasquatch_data['first_name'],
#             'last_name': sasquatch_data['last_name'],
#             'email': sasquatch_data['email'],
#             'password': sasquatch_data['password'],
#             'created_at': sasquatch_data['created_at'],
#             'updated_at': sasquatch_data['updated_at']
#         }
#         sasquatch.user = User(user_data)
#         return sasquatch


# # Updates a sasquatch using a given id
#     @classmethod
#     def update(cls, data):
#         query = """
#         UPDATE sasquatches SET 
#         location = %(location)s,
#         date_sighted = %(date_sighted)s,
#         number_of = %(number_of)s
#         WHERE id = %(id)s;
#         """
#         results = connectToMySQL(DATABASE).query_db(query, data)
#         return results

# # Deletes a sasquatch
#     @classmethod
#     def delete(cls, data):
#         query = """
#         DELETE FROM sasquatches WHERE id = %(id)s
#         """
#         results = connectToMySQL(DATABASE).query_db(query, data)
#         return results


#     @classmethod
#     def validate_sasquatch(cls, form):
#         is_valid = True
#         if len(form['location']) < 2:
#             flash("Please provide a name.", "add_err")
#             is_valid = False
#         if len(form['date_sighted']) == 0:
#             flash("Please provide a date.", "add_err")
#             is_valid = False
#         if len(form['number_of']) < 1:
#             flash("Please provide a number of sasquatches.", "add_err")
#             is_valid = False
#         if len(form['notes']) < 10:
#             flash("Please provide a few notes on the sighting", "add_err")
#             is_valid = False
#         if len(form['notes']) > 50:
#             flash("Notes are too long.", "add_err")
#             is_valid = False
#         return is_valid

