from dataclasses import dataclass

@dataclass
class User:
    name: str
    avatar: str
    username: str

    @staticmethod
    def from_json(json: dict):
        if json.get("fullname"):
            return User(
                name=json["fullname"],
                avatar=json["avatar"],
                username=json["name"]
            )

        return User(
            name=json["name"],
            avatar=json["avatar"],
            username=json["username"]
        )
