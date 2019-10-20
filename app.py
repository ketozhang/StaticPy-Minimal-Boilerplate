import sys
from flask import render_template
from staticpy import app, log, build_all, BASE_CONFIG, get_config

########################
# CUSTOM ROUTES
########################
@app.route("/")
def home():
    """Renders the home page."""
    return render_template("home.html"), **home_config)


@app.route("/notes")
def notes_page():
    context = BASE_CONFIG["contexts"]["notes"]
    return render_template("notes/index.html", **context)


@app.route("/posts")
def posts_page():
    return render_template("posts/index.html")


if __name__ == "__main__":
    args = sys.argv[1:]
    log.setLevel("INFO")
    if len(args) == 0:
        app.run(debug=True, port=8081, local=True)
    if "build" in args:
        elapsed_time = build_all()
        print(f"Building templates finished in {elapsed_time:.2f}secs")
    else:
        raise ValueError("Invalid command. Use `python app.py [build]`")
