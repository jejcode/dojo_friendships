from flask_app.config.mysqlconnection import connectToMySQL # import function to connect to database

class User:
    DB = "friendships_schema"
    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_user(cls, data): # query to get one user
        query = "SELECT * FROM users WHERE id = %(id)s" # get all users by this id
        results = connectToMySQL(cls.DB).query_db(query, data) # results is a list of 1
        return results[0] # only return first item in the list...there's only 1
    @classmethod
    def get_all_users(cls): # query to get all users from users table
        query = "SELECT * FROM users"
        results = connectToMySQL(cls.DB).query_db(query) # results are a list of db_rows
        all_users = [] # empty list that will store a class instance of each db_row
        for row_db in results:
            all_users.append(cls(row_db)) # create an instance of User and store in all_users list
        return all_users
    @classmethod
    def add_user(cls, data): # insert user into users table
        query = """INSERT INTO users (first_name, last_name)
                VALUES (%(fname)s, %(lname)s)"""
        return connectToMySQL(cls.DB).query_db(query, data)