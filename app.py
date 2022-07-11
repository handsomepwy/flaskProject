from flask import Flask, render_template

app = Flask(__name__)


user_list = ["pwy", "ybn", "hzh", "gzr", "pwy", "dxm"]


@app.route("/")
def hello_world():
    return render_template("main.html")


@app.route("/test",methods=['POST', 'GET'])
def test():
    stri = "1234567890"
    with open('data.txt', 'w') as f:
        f.write(stri)
    return "欢迎来到test页面"


professional = "wer"

@app.route("/<path_name>/")
def not_found(path_name):
    return render_template("not_found.html", path_name=path_name)


@app.route("/user/<search_name>/")
def hello(search_name):
    for c in user_list:
        if c == search_name:
            return render_template("user.html", search_name=search_name, return_material="oh! " + search_name + "is "
                                                                                                                "very"
                                                                                                                "smart!"
                                   )
    else:
        return render_template("user.html", search_name=search_name, return_material="oops, I don't have any profile "
                                                                                     "of " + search_name)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
