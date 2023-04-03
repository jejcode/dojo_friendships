from flask import render_template, redirect, request # import flask modules to route correctly
from flask_app import app # import Flask instance for routing
from flask_app.models import friendship, user # import models to query database in routes

@app.route('/user/add', methods=['POST'])
def add_user():
    user.User.add_user(request.form) # query to add user
    return redirect('/friendships') # will redirect to friendships