from dataclasses import dataclass
from .user import User
from .tags import Tags
from .published_part import PublishedPart
from .part import Part
from ..backend import Wattpad
import json

@dataclass
class Story:
    id: int
    title: str
    author: User
    description: str
    cover: str
    url: str
    lastPublishedPart: PublishedPart
    parts: tuple[Part]
    isPaywalled: bool
    tags: Tags

    @staticmethod
    def from_json_story(json: dict):
        return Story(
            id=json['id'],
            title=json['title'],
            author=User.from_json(json['user']),
            description=json['description'],
            cover=json['cover'],
            url=json['url'],
            lastPublishedPart=PublishedPart.from_json(json['lastPublishedPart']),
            parts=[
                Part.from_json(x)
                for x in json['parts']
            ],
            isPaywalled=json['isPaywalled'],
            tags=json['tags']
        )

    @staticmethod
    def from_json_part(json: dict):
        json = json['group']
        return Story(
            id=json['id'],
            title=json['title'],
            author=User.from_json(json['user']),
            description=json['description'],
            cover=json['cover'],
            url=json['url'],
            lastPublishedPart=PublishedPart.from_json(json['lastPublishedPart']),
            parts=[
                Part.from_json(x)
                for x in json['parts']
            ],
            isPaywalled=json['isPaywalled'],
            tags=json['tags']
        )

    @staticmethod
    def from_id(id: int, wattpad_engine: Wattpad) -> 'Story':
        data = wattpad_engine.fetch(
            f"api/v3/stories/{id}",
            {
                'fields': ""
                          "id,"
                          "title,"
                          "description,"
                          "url,"
                          "cover,"
                          "user,"
                          "isPaywalled,"
                          "author(name,username,avatar),"
                          "lastPublishedPart,"
                          "parts(id,title,text_url),tags"
            },
            expect_json=True
        )
        return Story.from_json_story(data)

    @staticmethod
    def from_partid(partid: int, wattpad_engine: Wattpad) -> 'Story':
        data = wattpad_engine.fetch(
            f"api/v4/parts/{partid}",
            {
                'fields': "text_url,"
                          "group"
                          "("
                          "id,"
                          "title,"
                          "description,"
                          "isPaywalled,"
                          "url,"
                          "cover,"
                          "author(name,username,avatar),"
                          "lastPublishedPart,"
                          "parts(id,title,text_url),"
                          "tags"
                          ")"
            },
            expect_json=True
        )
        return Story.from_json_part(data)

    def __post_init__(self):
        # Process the url to remove the unnecessary shit
        self.url = self.url.rsplit('-')[0]
