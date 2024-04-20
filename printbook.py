from wattpad import Wattpad, Story

wattpad_engine = Wattpad(use_cache=True)
story = Story.from_id(336166598, wattpad_engine)

print(story.title)
print(story.description)

for part in story.parts:
    part.render_with(wattpad_engine).display()

