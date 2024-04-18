from wattpad import Wattpad, Story, RenderedPage

w = Wattpad(use_cache=True)
s = Story.from_id(362914687, w)  # Owned by him

last_part = s.parts[-1]
render: RenderedPage = last_part.render_with(w)

# print(*w.cache_obj.iterkeys(), sep='\n')

print(s.title)
print(s.url)

render.display()
