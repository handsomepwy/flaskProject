from flask import Flask, render_template, request
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


user_list = ["pwy", "ybn", "hzh", "gzr"]


@app.route("/")
def hello_world():
    localtime = time.asctime(time.localtime(time.time()))
    f = open("vis.txt", "a")
    ip = request.remote_addr
    f.write("{ip} visited {path} page on {vis_time}\n".format(ip=ip, path="index", vis_time=localtime))
    return render_template("main.html", com=res_html)


@app.route("/<path_name>/")
def not_found(path_name):
    localtime = time.asctime(time.localtime(time.time()))
    f = open("vis.txt", "a")
    ip = request.remote_addr
    f.write("{ip} visited {path} page on {vis_time}\n".format(ip=ip, path=path_name, vis_time=localtime))
    return render_template("not_found.html", path_name=path_name)


@app.route("/user/<search_name>/")
def hello(search_name):
    localtime = time.asctime(time.localtime(time.time()))
    f = open("vis.txt", "a")
    ip = request.remote_addr
    f.write("{ip} visited user {username} page on {vis_time}\n".format(ip=ip, username=search_name, vis_time=localtime))
    for c in user_list:
        if c == search_name:
            return render_template("user.html", search_name=search_name,
                                   return_material="oh! "+search_name+" is very smart!")
    return render_template("user.html", search_name=search_name, return_material="oops, I don't have any profile of " + search_name)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
