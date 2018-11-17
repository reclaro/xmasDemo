from flask import Flask
app = Flask(__name__)

@app.route("/")
def homepage():
     return """
    <h1>Hello world!</h1>

    <iframe src="https://www.youtube.com/embed/yXQViqx6GMY?autoplay=1" width="853" height="480" frameborder="0" allowfullscreen></iframe>
    """

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
  
