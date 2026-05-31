from flask import Flask, request, render_template_string

app = Flask(__name__)

# Dictionary of valid words
dictionary = {"cat", "cot", "dot", "dog"}

# HTML template with instructions and CSS styling
html_template = """
<!doctype html>
<html>
<head>
  <title>Word Ladder Game</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f4f6f9;
      color: #333;
      text-align: center;
      padding: 40px;
    }
    h1 {
      color: #2c3e50;
    }
    .instructions {
      background: #ecf0f1;
      border: 1px solid #bdc3c7;
      padding: 15px;
      margin: 20px auto;
      width: 60%;
      border-radius: 8px;
    }
    form {
      margin-top: 20px;
    }
    input[type=text] {
      padding: 10px;
      width: 200px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    input[type=submit] {
      padding: 10px 20px;
      background: #3498db;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    input[type=submit]:hover {
      background: #2980b9;
    }
    .message {
      margin-top: 20px;
      font-weight: bold;
      color: #27ae60;
    }
  </style>
</head>
<body>
  <h1>🪜 Word Ladder Game</h1>
  <div class="instructions">
    <p><strong>Goal:</strong> Transform <b>CAT</b> into <b>DOG</b>.</p>
    <ul style="text-align:left; display:inline-block;">
      <li>Change only <b>one letter</b at a time.</li>
      <li>Each step must be a valid word.</li>
      <li>Reach the target word to win 🎉.</li>
    </ul>
  </div>
  <form method="post">
    <input type="text" name="word" placeholder="Enter next word">
    <input type="submit" value="Submit">
  </form>
  <div class="message">{{ message }}</div>
</body>
</html>
"""

current_word = "cat"

@app.route("/", methods=["GET", "POST"])
def game():
    global current_word
    message = f"Current word: {current_word}"
    if request.method == "POST":
        guess = request.form["word"].lower()
        if guess not in dictionary:
            message = "❌ Not a valid word!"
        elif sum(a != b for a, b in zip(current_word, guess)) == 1:
            current_word = guess
            if current_word == "dog":
                message = "🎉 Congratulations! You reached DOG!"
            else:
                message = f"✅ Good move! Current word: {current_word}"
        else:
            message = "⚠️ You must change only one letter!"
    return render_template_string(html_template, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
