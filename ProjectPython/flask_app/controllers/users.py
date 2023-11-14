from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe


# Renders the Login page
@app.route('/')
def index():
    return redirect('/login')

@app.route('/login')
def login():
    return render_template('login.html')

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










# ===== Sasqutch Routes ======

# # Add sasquatch route
# @app.route('/sasquatches')
# def sasquatch():
#     if not 'id' in session:
#         return redirect('/')
#     user = User.get_one(session['id'])
#     return render_template("report_sasquatch.html", user = user)


# # Calls the add_sasquatch function and redirects to the home_page
# @app.route('/sasquatches/add', methods = ['POST'])
# def add_sasquatch():
#     if Sasquatch.validate_sasquatch(request.form):
#         sasquatch = Sasquatch.add_sasquatch(request.form)
#         return redirect("/home_page")
#     else:
#         return redirect('/sasquatches')

# # Renders the edit_sasquatch page
# @app.route('/sasquatches/<int:id>/edit')
# def render_edit(id):
#     data = {
#         "id": id
#     }
#     user = User.get_one(session['id'])
#     sasquatch = Sasquatch.get_one(data)
#     return render_template('edit_sasquatch.html', sasquatch = sasquatch, user = user)

# # Calls the update function
# @app.route('/sasquatches/<int:id>/update', methods=['POST'])
# def update(id):
#     if Sasquatch.validate_sasquatch(request.form):
#         data = {
#             "id": id,
#             **request.form
#         }
#         Sasquatch.update(data)
#         return redirect(f'/sasquatches/{id}/show')
#     else:
#         return redirect(f'/sasquatches/{id}/edit')

# # Calls the delete function
# @app.route('/sasquatches/<int:id>/delete')
# def delete(id):
#     data = {
#         "id": id
#     }
#     Sasquatch.delete(data)
#     print('deleted')
#     return redirect('/home_page')

# # Redirects to the show recipe page
# @app.route('/sasquatches/<int:id>/show')
# def show_sasquatch(id):
#     data = {
#         "id": id
#     }
#     user = User.get_one(session['id'])
#     sasquatch = Sasquatch.get_one(data)
#     return render_template('show_sasquatch.html', sasquatch = sasquatch, user = user)

