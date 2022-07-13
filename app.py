from flask import Flask, render_template
import time
import sqlite3
connection = sqlite3.connect("test.db")
cursor = connection.cursor()
cursor.execute("select * from comments")
table = cursor.fetchall()
i = 0
res_html = "<ul>"
while i < len(table):
    res_html = res_html + "<li>{name}:</li><li>{comment}</li>".format(name=table[i][0], comment=table[i][1])
    i = i + 1
res_html = res_html + "</ul>"


app = Flask(__name__)


user_list = ["pwy", "ybn", "hzh", "gzr", "pwy", "dxm"]


@app.route("/")
def hello_world():
    f = open("vis.txt", "a")
    localtime = time.asctime(time.localtime(time.time()))
    f.write("visited / page on " + localtime + "\n")
    return render_template("main.html", com = res_html)


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
