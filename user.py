from dataclasses import dataclass
from enum import Enum

class Status(Enum):
    command = 0 # listen command from user
    data = 1 # get data from user


@dataclass
class User:
    id: int
    status: Status = Status.command
    data: dict = {}

users = {}

def create_user(user_id:int) -> User:
    """Create new user"""
    new_user = User(user_id)
    users[user_id] = new_user
    return new_user

def get_user(user_id: int) -> User|None:
    """Get user if exists or create new"""
    user = users.get(user_id)
    return user if user else create_user(user_id)