from dataclasses import dataclass
from .user import User
from .tags import Tags
from .published_part import PublishedPart
@dataclass
class Story:
    text_url: str
    id: int
    title: str
    user: User
    description: str
    cover: str
    tags: Tags
    url: str
    lastPublishedPart: PublishedPart
    