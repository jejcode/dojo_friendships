from flask import render_template, redirect, request # import flask modules to route correctly
from flask_app import app # import Flask instance for routing
from flask_app.models import friendship, user # import models to query database in routes

@app.route('/') # default route to go to /friendships
def default_route():
    return redirect('/friendships')

@app.route('/friendships') # loads friendships page
def display_friendships():
    friends_list = friendship.Friendship.get_all_friendships() # get join table of all established relationships
    user_list = user.User.get_all_users() # get users to populate form list in html
    return render_template('friendships.html', friends = friends_list, users = user_list)

@app.route('/friendships/add', methods=['POST'])
def add_friendship():
    friendship.Friendship.add_friendship(request.form) # will redirect to friendships regardless of query outcome
    return redirect('/friendships')