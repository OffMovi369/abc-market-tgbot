from dataclasses import dataclass
from enum import Enum

class Status(Enum):
    command = 0 # listen command from user
    data = 1 # get data from user


@dataclass
class User:
    id: int
    status: Status = Status.command
    current_page: str = "main"
    previous_page: str = None
    data_name: str = None


class UserHandle:
    __users = {}

    @classmethod
    def create_user(cls, user_id:int) -> User:
        """Create a new User dataclass and add to __users dict"""
        new_user = User(user_id)
        cls.__users[user_id] = new_user
        return cls.__users[user_id]
    
    @classmethod
    def get_user(cls, user_id:int) -> User:
        "Get user by id if exists or create and return new"
        user = cls.__users.get(user_id)
        return user if user else cls.create_user(user_id)