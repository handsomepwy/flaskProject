from flask import Flask, render_template
import time

app = Flask(__name__)


user_list = ["pwy", "ybn", "hzh", "gzr", "pwy", "dxm"]


@app.route("/")
def hello_world():
    f = open("vis.txt", "a")
    localtime = time.asctime(time.localtime(time.time()))
    f.write("visited / page on " + localtime + "\n")
    return render_template("main.html")


@app.route("/<path_name>/")
def not_found(path_name):
    f = open("vis.txt", "a")
    localtime = time.asctime(time.localtime(time.time()))
    f.write("visited " + path_name + " page on " + localtime + "\n")
    return render_template("not_found.html", path_name=path_name)


@app.route("/user/<search_name>/")
def hello(search_name):
    f = open("vis.txt", "a")
    localtime = time.asctime(time.localtime(time.time()))
    for c in user_list:
        if c == search_name:
            f.write("visited user " + search_name + " page on " + localtime + "\n")
            return render_template("user.html", search_name=search_name,
                                   return_material="oh! "+search_name+" is very smart!")
    f.write("visited user " + search_name + " page on " + localtime + "\n")
    return render_template("user.html", search_name=search_name,
                           return_material="oops, I don't have any profile of " + search_name)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
