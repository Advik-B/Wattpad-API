from dataclasses import dataclass

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