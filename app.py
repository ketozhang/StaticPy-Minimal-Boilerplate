import sys
from flask import render_template
from staticpy import app, log, build_all, BASE_CONFIG

########################
# CUSTOM ROUTES
########################


@app.route("/notes")
def notes_page():
    context = BASE_CONFIG['contexts']['notes']
    return render_template("notes/index.html", **context)


@app.route("/posts")
def posts_page():
    return render_template("posts/index.html")


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 0:
        log.setLevel("INFO")
        app.run(debug=True, port=8080, local=True)
    elif "build" in args:
        log.setLevel("INFO")
        elapsed_time = build_all()
        print(f"Building templates finished in {elapsed_time:.2f}secs")
    else:
        raise ValueError("Invalid command. Use `python app.py [build]`")
