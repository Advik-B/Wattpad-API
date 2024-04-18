from dataclasses import dataclass
from .rendered_part_skeleton import RenderedPage
from ..backend import Wattpad
from bs4 import BeautifulSoup

@dataclass
class Part:
    id: int
    title: str
    text_url: str

    @staticmethod
    def from_json(json: dict):
        return Part(
            id=int(json['id']),
            title=json['title'],
            text_url=json['text_url']['text']
        )

    def render(self, wattpad: Wattpad) -> RenderedPage:
        print(self.text_url)
