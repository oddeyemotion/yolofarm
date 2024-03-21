from flask import Flask, render_template, request, redirect, url_for

# Create the Flask app
app = Flask(__name__)

# Define a route
@app.route('/')
def hello_world():
    return render_template("index.html")

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5500)