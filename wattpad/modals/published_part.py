from dataclasses import dataclass
from datetime import datetime


@dataclass
class PublishedPart:
    id: int
    createDate: datetime

    @staticmethod
    def from_json(json: dict) -> "PublishedPart":
        return PublishedPart(
            id=int(json['id']),
            createDate=datetime.strptime(json["createDate"], "%Y-%m-%dT%H:%M:%SZ")
        )
