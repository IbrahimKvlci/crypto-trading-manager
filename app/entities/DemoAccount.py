from __future__ import annotations
from typing import List
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.entities.User import User
    from app.entities.Cryptocurrency import Cryptocurrency

class DemoAccount:
    def __init__(self, id, user:User, balance:List[Cryptocurrency]):
        self.id = id
        self.user = user
        self.balance = balance