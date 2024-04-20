from wattpad import Wattpad, Story, RenderedPage
from random import choice

w = Wattpad(use_cache=True)
# s = Story.from_id(362914687, w)  # Owned by him
s = Story.from_id(336166598, w)
# s = Story.from_id(1321853334, w)


    
random_part = choice(s.parts)
random_render: RenderedPage = random_part.render_with(w)

# print(*w.cache_obj.iterkeys(), sep='\n')

print(s.title)
print(s.url)

random_render.display()
