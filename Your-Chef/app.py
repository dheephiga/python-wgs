from flask import Flask, render_template, request, flash

app = Flask(__name__)

class Recipe:
    def __init__(self, name, ingredients, instructions, prep_time, cook_time, total_time, cuisine):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.prep_time = prep_time
        self.cook_time = cook_time
        self.total_time = total_time
        self.cuisine = cuisine
        
cuisines = ['Indian','Italian','Japanese', 'American', 'Mexican', 'Spanish']
my_recipes = []
new_recipe = Recipe(
    name="Palak Chapathi",
    ingredients=["whole wheat flour", "spinach", "green chili", "ginger", "garlic", "cumin seeds", "salt", "water", "oil"],
    instructions=[
        "Blanch spinach leaves in boiling water for 2 minutes. Drain and rinse with cold water.",
        "Blend blanched spinach, green chili, ginger, and garlic into a smooth paste.",
        "In a mixing bowl, combine whole wheat flour, spinach paste, cumin seeds, and salt.",
        "Gradually add water and knead into a soft dough. Let it rest for 15-20 minutes.",
        "Divide the dough into equal-sized balls. Roll each ball into a thin chapathi.",
        "Heat a griddle or tawa. Cook each chapathi on both sides until golden brown spots appear, brushing with oil as needed.",
        "Serve hot with your favorite curry or chutney."
    ],
    prep_time=20,
    cook_time=20,
    total_time=40,
    cuisine="Indian"
)

@app.route('/')
def index():
    return render_template('index.html',cuisines=cuisines)

@app.route('/add_recipe')
def add_recipe():
    name = request.form['name']
    cuisine = request.form['cuisine']
    prep_time = request.form['prep_time']
    cook_time = request.form['cook_time']
    total_time = prep_time + cook_time
    ingredients = request.form['ingredients']
    instructions = request.form['instructions']
    

if __name__ == "__main__":
    app.run(debug=True)