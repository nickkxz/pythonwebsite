from flask import Flask, render_template
# from flask_script import Manager

app = Flask(__name__)
# manager = Manager(app)


@app.route("/")
def index():
    headline = "hello, variables!"
    return render_template("index.html", headline=headline)


# if __name__ == "__main__":
#     manager.run()
