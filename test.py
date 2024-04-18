from wattpad import Wattpad, Story

w = Wattpad(use_cache=True)
s = Story.from_id(362914687, w) # Owned by him
print(*[p.text_url for p in s.parts], sep='\n')