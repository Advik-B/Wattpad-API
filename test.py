from wattpad import Wattpad, Story, RenderedPage

w = Wattpad(use_cache=True)
# s = Story.from_id(362914687, w)  # Owned by him
s = Story.from_id(336166598, w)
another_s = Story.from_partid(1321853334, w)


    
# print(*w.cache_obj.iterkeys(), sep='\n')

print(s.title)
print(s.author)
print(s.description)

print('='*80)

print(another_s.title)
print(another_s.author)
print(another_s.description)
