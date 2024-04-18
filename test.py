from wattpad import Wattpad, Story

w = Wattpad(use_cache=True)
s = Story.from_id(336166598, w)
print(s.tags)