from wattpad import Wattpad, Story, RenderedPage

w = Wattpad(use_cache=True)
s = Story.from_partid(362914687, w)  # Owned by him
# s = Story.from_id(336166598, w)
print(s.title)
def test_takendown_story():
    another_s = Story.from_partid(1321853334, w)
    print(another_s.title)
    print(another_s.author)
    print(another_s.description)
    print(another_s.tags)

