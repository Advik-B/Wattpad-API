from dataclasses import dataclass

@dataclass
class User:
    name: str
    avatar: str
    username: str

    @staticmethod
    def from_json(json: dict):
        return User(
            name=json["name"],
            avatar=json["avatar"],
            username=json["username"]
        )
