# Import Flask framework and helper functions
from flask import Flask, request, render_template_string

# Create a Flask application instance
app = Flask(__name__)

# Define a small dictionary of valid words for the game
dictionary = {"cat", "cot", "dot", "dog"}

# HTML template for the game page (inline for simplicity)
html_template = """
<!doctype html>
<title>Word Ladder Game</title>
<h2>Word Ladder: CAT → DOG</h2>
<form method="post">
  <input type="text" name="word" placeholder="Enter next word">
  <input type="submit" value="Submit">
</form>
<p>{{ message }}</p>
"""

# Track the current word in the game (starting point)
current_word = "cat"

# Define the main route (homepage) for the game
@app.route("/", methods=["GET", "POST"])
def game():
    global current_word  # Use the global variable to track progress
    message = f"Current word: {current_word}"  # Default message

    # Handle form submission
    if request.method == "POST":
        guess = request.form["word"].lower()  # Get user input and lowercase it

        # Check if the guess is in the dictionary
        if guess not in dictionary:
            message = "Not a valid word!"
        # Check if only one letter is different
        elif sum(a != b for a, b in zip(current_word, guess)) == 1:
            current_word = guess  # Update current word
            if current_word == "dog":  # Check if target reached
                message = "🎉 Congratulations! You reached DOG!"
            else:
                message = f"Good move! Current word: {current_word}"
        else:
            message = "You must change only one letter!"

    # Render the HTML template with the message
    return render_template_string(html_template, message=message)

# Run the app on port 5000, accessible from all network interfaces
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
