from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = "KEY"


class Recipe:
    unique_names = set()

    def __init__(
        self, name, ingredients, instructions, prep_time, cook_time, total_time, cuisine
    ):
        if name in Recipe.unique_names:
            raise ValueError(f"Recipe name '{name}' already exists.")

        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.prep_time = prep_time
        self.cook_time = cook_time
        self.total_time = total_time
        self.cuisine = cuisine

        Recipe.unique_names.add(name)
        
def get_user_role():
    if "username" in session:
        username = session["username"]
        return users[username]["role"]
    return None

cuisines = ["Indian", "Italian", "Japanese", "American", "Mexican", "Spanish"]
my_recipes = {}
users = {
    "user1": {"username": "user1", "password": "123", "role": "user"},
    "admin": {"username": "admin", "password": "admin", "role": "admin"},
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/home")
def index():
    user_role = get_user_role()
    return render_template(
        "index.html",
        cuisines=cuisines,
        my_recipes=my_recipes,
        user_role=user_role
    )


@app.route("/add_recipe", methods=["POST"])
def add_recipe():
    if get_user_role() != "admin":
        return redirect(url_for("index"))

    name = request.form["name"]
    cuisine = request.form["cuisine"]
    prep_time = request.form["prep_time"]
    cook_time = request.form["cook_time"]
    total_time = int(prep_time) + int(cook_time)
    ingredients = request.form["ingredients"].split(",")
    instructions = request.form["instructions"].split(".")

    try:
        new_recipe = Recipe(
            name=name,
            ingredients=ingredients,
            instructions=instructions,
            prep_time=prep_time,
            cook_time=cook_time,
            total_time=total_time,
            cuisine=cuisine,
        )

        my_recipes[name] = new_recipe
        flash(f"Recipe: {name} added successfully", "success")
        return redirect(url_for("index"))

    except ValueError as e:
        return str(e)

@app.route('/update_recipe/<name>', methods=['GET', 'POST'])
def update_recipe(name):
    if get_user_role() != "admin":
        return redirect(url_for("index"))
    
    if request.method == 'POST':
        ingredients = request.form['ingredients'].split(',')
        instructions = request.form['instructions'].split('.')
        cuisine = request.form['cuisine']
        prep_time = request.form['prep_time']
        cook_time = request.form['cook_time']
        total_time = int(prep_time) + int(cook_time)
        
        to_update_recipe = my_recipes.get(name)
        if to_update_recipe:
            to_update_recipe.ingredients = ingredients
            to_update_recipe.instructions = instructions
            to_update_recipe.cuisine = cuisine
            to_update_recipe.prep_time = prep_time
            to_update_recipe.cook_time = cook_time
            to_update_recipe.total_time = total_time
            flash(f'Recipe: {name} updated successfully', 'success')
            return redirect(url_for('index'))
        else:
             flash(f'Recipe: {name} not found', 'error')
             return redirect(url_for('index'))
    else:
        to_update_recipe = my_recipes.get(name)
        if to_update_recipe:
            return render_template('index.html', name=name, my_recipes=my_recipes, recipe=to_update_recipe)
        else:
            flash(f'Recipe: {name} not found', 'error')
            return redirect(url_for('index'))
        
@app.route('/view_recipe/<name>')
def view_recipe(name):
    recipe = my_recipes.get(name)
    if recipe:
        user_role = get_user_role()
        return render_template('recipe.html', recipe=recipe, cuisines=cuisines,user_role=user_role)
    else:
        flash(f'Recipe: {name} not found', 'error')
        return redirect(url_for('index'))
       
    
@app.route('/delete/<name>')
def delete_recipe(name):
    if get_user_role() != "admin":
        return redirect(url_for("index"))
    del my_recipes[name]
    flash(f'Recipe: {name} deleted successfully', 'success')
    return redirect(url_for('index'))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in users and users[username]["password"] == password:
            session["username"] = username 
            flash("Successful login", "success")
            return redirect(url_for("index"))
        else:
            flash("Login failed. Please check your username and password.", "error")
            return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        cpassword = request.form["cpassword"]
        role = "user"

        if username in users:
            flash("Username already exists")
            return redirect(url_for("login"))

        if password == cpassword:
            users[username] = {"username": username, "password": password, "role": role}
            flash("Signup Successful!")
            return redirect(url_for("login"))
        else:
            flash("Passwords doesn't match", "error")

    return render_template("signup.html")





if __name__ == "__main__":
    app.run(debug=True)
