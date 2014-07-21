from flask import render_template, Flask, request
from apps import app


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    # age = 24
    # gender = "Female"
    # friend = ['SUHYUNG', 'SEUNGHEE', 'HWAJUNG']

    # get = None
    # post = None

    # if request.args:
    #     get = request.args["text_get"]

    # if request.form:
    #     post = request.form["text_post"]

    # return render_template("index.html",
    #                        age=age, gender=gender, friend=friend,
    #                        input_get=get, input_post=post)

    get = None

    if request.args:
        get = request.args["text_get"]

    return render_template("index.html", query=get)
