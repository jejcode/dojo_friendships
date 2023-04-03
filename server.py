from flask_app import app

# import routes
from flask_app.controllers import friendships
from flask_app.controllers import users


if __name__ == '__main__':
    app.run(debug = True, port = 5001)