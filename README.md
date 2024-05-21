# Wattpad API

This is a no-compromise Wattpad API wrapper for python.
This project is still in development, and is not yet ready for production use.
It also speeds up the process by using disk caching, It will cache the response from the API and will only make a new request if the request is not cached.

This, of course can be disabled by setting the cache to False.

## Features

- Simple and easy to use
- Caches responses from the API to disk for faster response times
- Allows direct access to the API via the `fetch` method
- Allows exporting of the objects to DICT, JSON, or YAML
- Can directly parse a manifest file from a curseforge modpack

## Installation

```bash
pip install wattpad-api
```

## Usage

```python
from wattpad import Wattpad, Story

engine = Wattpad()
wounded_love = Story.from_id(336166598, engine)

print(wounded_love.title)
print(wounded_love.author)
```

## TODO

- [x] Implement the export methods
- [x] Implement the cache
- [x] Implement the fetch method
- [ ] Implement the search method
- [ ] Wrap the ENTIRE API

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
