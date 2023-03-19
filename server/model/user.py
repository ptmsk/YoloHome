import config
from database import User
from error import *

class UserModel():
    def __init__(self, database) -> None:
        self._database = database

    def get_user(self, user_id=None, username=None):
        query = {}
        if user_id:
            query["_id"] = user_id
        if username:
            query["username"] = username
        
        try:
            user_list = self._database.fetch_data(config.database.DOC_USER_LIST, query)
        except:
            if user_id:
                raise RecordFindError(user_id)
            else:
                raise RecordFindError(username)
        
        if user_id and len(user_list) < 1:
            raise RecordNotFound(user_id)
        
        if username and len(user_list) < 1:
            raise RecordNotFound(username)
        
        return user_list

    def add_user(self, record):
        try:
            username = record['username']
            password = record['password']
        except:
            raise LackRequestData()
        user = User(username=username, password=password)
        try:
            self._database.add_data(user)
        except:
            raise RecordInsertError(record)
        
        return user

    def delete_user(self, user_id):
        try:
            user_list = self.get_user(user_id)
            if len(user_list) < 1:
                raise RecordNotFound(user_id)
            user = user_list[0]
            self._database.remove_data(user)
        except:
            raise RecordDeleteError(user_id)
        
        return user
    