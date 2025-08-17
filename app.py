from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# Mood-specific recipe data
mood_data = {
    "happy": {
        "addons": [
            "with a Sunny Lemon Dressing",
            "Sprinkled with Joyful Confetti",
            "Drenched in Smiles Sauce"
        ],
        "ingredients": [
            "2 cups of laughter-infused sugar",
            "1 teaspoon of sunny zest",
            "a handful of rainbow sprinkles",
            "3 giggles of whipped cream",
            "a splash of sparkling happiness"
        ],
        "steps": [
            "Mix with bursts of laughter.",
            "Dance while whisking until joyous.",
            "Sunbathe dough in warm smiles.",
            "Serve with a grin wider than the plate."
        ],
        "image": "/static/images/happy.jpg"
    },
    "fucked_up": {
        "addons": [
            "with a Hint of Pure Chaos",
            "Served in an Upside-Down Plate",
            "Exploding with Anarchy Sauce"
        ],
        "ingredients": [
            "a fistful of unidentified crumbs",
            "3 tablespoons of pure confusion",
            "a splash of questionable liquid",
            "half of something you found yesterday",
            "dust scraped from the toaster"
        ],
        "steps": [
            "Throw everything in a bowl and hope for the best.",
            "Ignore all known cooking laws.",
            "Season aggressively with regret.",
            "Serve immediately... or never."
        ],
        "image": "/static/images/fkedup.jpg"
    },
    "sad": {
        "addons": [
            "with a Sprinkle of Melancholy",
            "Served Under a Grey Sky",
            "Resting in a Puddle of Tears"
        ],
        "ingredients": [
            "2 cups of salty tears",
            "1 teaspoon of gloomy gravy",
            "a handful of soggy croutons",
            "half-melted ice cream of regret",
            "3 drops of cloudy broth"
        ],
        "steps": [
            "Sigh deeply before starting.",
            "Stir slowly while staring out the window.",
            "Season with whispers of lost dreams.",
            "Serve with tissues on the side."
        ],
        "image": "/static/images/sad.jpg"
    },
    "romantic": {
        "addons": [
            "with a Kiss of Chocolate Affection",
            "Served on a Bed of Rose Petals",
            "Drizzled in Love Sauce"
        ],
        "ingredients": [
            "1 dozen hand-picked love berries",
            "2 cups of passion-whipped cream",
            "a sprinkle of heart-shaped sugar",
            "melted chocolate of eternal devotion",
            "a pinch of romantic spice"
        ],
        "steps": [
            "Whisper sweet nothings to the ingredients.",
            "Mix slowly while gazing into the distance.",
            "Garnish with rose petals in the shape of a heart.",
            "Serve under candlelight with soulful music."
        ],
        "image": "/static/images/romantic.jpg"
    }
}

# Default mood if none selected
default_mood = "happy"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate_recipe", methods=["POST"])
def generate_recipe():
    data = request.get_json()
    food_name = data.get("foodName", "Mystery Dish").strip()
    mood = data.get("mood", default_mood).lower()

    # Replace spaces or special chars with safe key format
    mood_key = mood.replace(" ", "_")
    mood_content = mood_data.get(mood_key, mood_data[default_mood])

    recipe_name = f"{food_name} {random.choice(mood_content['addons'])}"
    ing = random.sample(mood_content["ingredients"], min(4, len(mood_content["ingredients"])))
    step = random.sample(mood_content["steps"], min(4, len(mood_content["steps"])))
    image_url = mood_content["image"]

    return jsonify({
        "name": recipe_name,
        "ingredients": ing,
        "steps": step,
        "image": image_url
    })

if __name__ == "__main__":
    app.run(debug=True)
