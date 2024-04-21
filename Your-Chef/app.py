from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "KEY"

class Recipe:
    unique_names = set()

    def __init__(self, name, ingredients, instructions, prep_time, cook_time, total_time, cuisine):
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

    def remove_name(self):
        Recipe.unique_names.remove(self.name)

cuisines = ['Indian', 'Italian', 'Japanese', 'American', 'Mexican', 'Spanish']
my_recipes = {}

@app.route('/')
def index():
    return render_template('index.html', cuisines=cuisines, my_recipes=my_recipes)

@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    name = request.form['name']
    cuisine = request.form['cuisine']
    prep_time = request.form['prep_time']
    cook_time = request.form['cook_time']
    total_time = int(prep_time) + int(cook_time)
    ingredients = request.form['ingredients'].split(',')
    instructions = request.form['instructions'].split('.')
    
    try:
        new_recipe = Recipe(
            name=name, 
            ingredients=ingredients, 
            instructions=instructions, 
            prep_time=prep_time, 
            cook_time=cook_time, 
            total_time=total_time, 
            cuisine=cuisine
        )
        
        my_recipes[name] = new_recipe          
        print(type(new_recipe))
        print(my_recipes.items())
        flash(f'Recipe: {name} added successfully', 'success')
        return redirect(url_for('index'))
        
    except ValueError as e:
        return str(e)

@app.route('/update_recipe/<name>', methods=['GET', 'POST'])
def update_recipe(name):
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
            return 'Recipe not found'
@app.route('/view_recipe/<name>')
def view_recipe(name):
    recipe = my_recipes.get(name)
    if recipe:
        return render_template('recipe.html', recipe=recipe, cuisines=cuisines)
    else:
        return 'Recipe not found'
@app.route('/delete/<name>')
def delete_recipe(name):
    del my_recipes[name]
    flash(f'Recipe: {name} deleted successfully', 'success')
    return redirect(url_for('index'))
    

if __name__ == "__main__":
    app.run(debug=True)
