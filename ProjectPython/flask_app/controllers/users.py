from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe


# Default route
@app.route('/')
def index():
    return redirect('/login')

# Renders the Login page
@app.route('/login')
def login():
    return render_template('login.html')

# Renders the register page
@app.route('/register')
def register():
    return render_template('register.html')

# Calls the Login function
@app.route('/login', methods = ['POST'])
def log():
    logged_user = User.login(request.form)
    if logged_user:
        session['id'] = logged_user.id
        return redirect('/home_page')
    else:
        return redirect('/')

# Logs the user out
@app.route('/home_page/logout')
def logout():
    session.clear()
    return redirect('/')

# Calls the register function and adds the new user to the database
@app.route('/add_user', methods = ['POST'])
def add_user():
    if User.validator(request.form):
        print("working")
        session['id'] = User.register(request.form)
        return redirect('/home_page')
    else:
        return redirect('/register')

# Renders the home page if the user's id is in session
@app.route('/home_page')
def home_page():
    if not 'id' in session:
        return redirect('/')
    user = User.get_one(session['id'])
    return render_template("home.html", user = user)





# ===== Recipe Routes ======

@app.route('/dashboard')
def dashboard():
    if not 'id' in session:
        return redirect('/')
    user = User.get_one(session['id'])
    recipes = Recipe.display_recipes()
    return render_template("dashboard.html", user = user, recipes = recipes)

# Renders the create recipe page
@app.route('/dashboard/add')
def add_recipe():
    if not 'id' in session:
        return redirect('/')
    user = User.get_one(session['id'])
    return render_template("create_recipe.html", user = user)


# Calls the add_recipe function and redirects to the home_page
@app.route('/recipe/add', methods = ['POST'])
def add_sasquatch():
    if Recipe.validate_recipe(request.form):
        recipe = Recipe.add_recipe(request.form)
        return redirect("/dashboard")
    else:
        return redirect('/dashboard/add')

# Redirects to the show recipe page
@app.route('/recipes/<int:id>/show')
def show_recipe(id):
    data = {
        "id": id
    }
    user = User.get_one(session['id'])
    recipe = Recipe.get_one(data)
    return render_template('show_recipe.html', recipe = recipe, user = user)


# Renders the edit_recipe page
@app.route('/recipes/<int:id>/edit')
def render_edit(id):
    data = {
        "id": id
    }
    user = User.get_one(session['id'])
    recipe = Recipe.get_one(data)
    return render_template('edit_recipe.html', recipe = recipe, user = user)

# # Calls the update function
@app.route('/recipes/<int:id>/update', methods=['POST'])
def update(id):
    if Recipe.validate_recipe(request.form):
        data = {
            "id": id,
            **request.form
        }
        Recipe.update(data)
        return redirect(f'/recipes/{id}/show')
    else:
        return redirect(f'/recipes/{id}/edit')

# Calls the delete function
@app.route('/recipes/<int:id>/delete')
def delete(id):
    data = {
        "id": id
    }
    Recipe.delete(data)
    print('deleted')
    return redirect('/recipes/delete/page')

# renders the delete page
@app.route('/recipes/delete/page')
def delete_page():
    return render_template('delete_page.html')

# renders the browse page
@app.route('/recipes/browse')
def browse():
    if not 'id' in session:
        return redirect('/')
    user = User.get_one(session['id'])
    recipes = Recipe.display_recipes()
    return render_template("browse.html", user = user, recipes = recipes)

