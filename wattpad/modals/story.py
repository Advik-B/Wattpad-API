from dataclasses import dataclass
from .user import User
from .tags import Tags
from .published_part import PublishedPart
from .part import Part
from ..backend import Wattpad

@dataclass
class Story:
    id: int
    title: str
    user: User
    description: str
    cover: str
    tags: Tags
    url: str
    lastPublishedPart: PublishedPart
    parts: tuple[Part]
    isPaywalled: bool

    @staticmethod
    def from_json_story(json: dict):
        return Story(
            id=json['id'],
            title=json['title'],
            user=User.from_json(json['user']),
            description=json['description'],
            cover=json['cover'],
            tags=json['tags'],
            url=json['url'],
            lastPublishedPart=PublishedPart.from_json(json['lastPublishedPart']),
            parts=(
                Part.from_json(x)
                for x in json['parts']
            ),
            isPaywalled=json['isPaywalled']
        )

    @staticmethod
    def from_json_part(json: dict):
        json = json['group']
        return Story(

        )