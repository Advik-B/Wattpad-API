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
            tags=json['tag'],
            url=json['url'],
            lastPublishedPart=PublishedPart.from_json(json['lastPublishedPart']),
            parts=[
                Part.from_json(x)
                for x in json['parts']
            ],
            isPaywalled=json['isPaywalled']
        )

    @staticmethod
    def from_id(id: int, wattpad_engine: Wattpad):
        data = wattpad_engine.fetch(
            f"api/v3/stories/{id}",
            {
                'fields':""
                  "id,"
                  "title,"
                  "description,"
                  "url,"
                  "cover,"
                  "isPaywalled,"
                  "user(name,username,avatar),"
                  "lastPublishedPart,"
                  "parts(id,title,text_url),"
                  "tag"
             },
            expect_json=True
        )
        return Story.from_json_story(data)


    def __post_init__(self):
        # Process the url to remove the unnecessary shit
        self.url = self.url.rsplit('-')[0]
