from urllib.parse import unquote

class CacheLibNotFound(Exception):
    """
    Cache library (diskcache) not found in the current python runtime
    Install it using `pip install diskcache`
    """


class APIerror(Exception): pass

class NotJsonError(Exception):
    def __init__(self, data: str):
        super.__init__("Could not decode the response as JSON")
        self.add_note("Response: " + data)


class NotFoundError(APIerror):
    def __init__(self, url: str):
        self.url = url
        super().__init__(f"[404] The requested URL was not found")
        self.add_note(f"Requested URL: {unquote(url)}")
        self.add_note("The requested URL has been unquoted for better readability")