from flask_app.config.mysqlconnection import connectToMySQL # import function to connect to database
from flask_app.models import user # import user model to create instances
class Friendship:
    DB = 'friendships_schema'
    def __init__(self, data) -> None:
        self.id = data['friendships.id'],
        self.user_id = data['user_id'],
        self.friend_id = data['friend_id'],
        self.created_at = data['friendships.created_at']
        self.updated_at = data['friendships.updated_at']
        self.person = None
        self.friend = None
    
    @classmethod
    def get_all_friendships(cls): # get join table of all friendships
        query = """SELECT * FROM users
                JOIN friendships ON users.id = user_id
                JOIN users AS friends ON friends.id = friend_id;"""
        results = connectToMySQL(cls.DB).query_db(query)
        friends_list = [] # empty list to hold all Friendship instances
        for row_DB in results:
            user_data = { # model data from users portion of query
                'id': row_DB['id'],
                'first_name': row_DB['first_name'],
                'last_name': row_DB['last_name'],
                'created_at': row_DB['created_at'],
                'updated_at': row_DB['updated_at']
            }
            friend_data = { # model data from friends portion of query
                'id': row_DB['friends.id'],
                'first_name': row_DB['friends.first_name'],
                'last_name': row_DB['friends.last_name'],
                'created_at': row_DB['friends.created_at'],
                'updated_at': row_DB['friends.updated_at']
            }
            current_relationship = cls(row_DB) # create instance of relationship
            current_relationship.person = user.User(user_data) # create instance of user and store in friendship
            current_relationship.friend = user.User(friend_data) # create instance of friend and store in friendship
            friends_list.append(current_relationship) # add friendship to list
        return friends_list
    @classmethod
    def add_friendship(cls, data): # query favorites table for existing relationship
        query = "SELECT * FROM friendships WHERE user_id = %(user)s AND friend_id = %(friend)s" # looks for existing relationship
        results = connectToMySQL(cls.DB).query_db(query, data)
        if data['user'] != data['friend'] and len(results) == 0: # if friendship doesn't yet exist, create it
            insert = """INSERT INTO friendships (user_id, friend_id) 
                    VALUES (%(user)s, %(friend)s)"""
            return connectToMySQL(cls.DB).query_db(insert, data)
        return False