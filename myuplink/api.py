from typing import Dict

class MyUplinkApi:
    def __init__(
        self,
        token: Dict[str, str] = None
    ):
        self.token = token

    def get_token(self):
        return self.token