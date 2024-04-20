from dataclasses import dataclass
from .rendered_part_skeleton import RenderedPage, HTML, HTMLtypes, HTMLword, HTMLStyle
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

    def render_with(self, wattpad_engine: Wattpad) -> RenderedPage:
        api_path = self.text_url.removeprefix(wattpad_engine.base_url)
        data = wattpad_engine.fetch(api_path, expect_json=False)
        html = BeautifulSoup(data, 'html.parser')
        stack: list[HTML] = []
        for p_tag in html.find_all('p'):
            if image := p_tag.find('img'):
                stack.append(
                    HTML(
                        data=image['src'],
                        type=HTMLtypes.image,
                    )
                )
            else:
                text_content: list[HTMLword] = []
                for element in p_tag.contents:
                    if isinstance(element, str):
                        text_content.append(HTMLword(element.strip(), style=HTMLStyle.general))
                    else:
                        if element.name == "b":
                            text_content.append(HTMLword(element.get_text(), HTMLStyle.bold))
                        elif element.name == "i":
                            text_content.append(HTMLword(element.get_text(), HTMLStyle.itialic))
                        else:
                            text_content.append(HTMLword(element.get_text(), style=HTMLStyle.general))
                stack.append(
                    HTML(
                        data=text_content,
                        type=HTMLtypes.text,
                    )
                )
        return RenderedPage(
            title=self.title,
            stack=stack
        )