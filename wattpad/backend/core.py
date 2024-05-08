from dataclasses import dataclass
from ..errors import CacheLibNotFound, APIerror, NotJsonError, NotFoundError
from requests import get
from requests.exceptions import  JSONDecodeError
from urllib.parse import urljoin
from .query_builder import BASE_URL

@dataclass
class Wattpad:
    base_url: str = BASE_URL
    use_cache: bool = True
    user_agent: str = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/123.0.0.0 Safari/537.36"
    )

    def __post_init__(self) -> None:
        if self.use_cache:
            try:
                from diskcache import Cache
                self.cache_obj = Cache("capacitor")
            except (ImportError, ModuleNotFoundError) as e:
                print("😂🫵🏻", flush=False)
                raise CacheLibNotFound(
                    "diskcache not found in the current python interpreter\n"
                    "either install it using pip or set use_cache=False"
                ) from e

    def _fetch(self, path: str, query: dict, jayson=True) -> dict | str:
        response = get(
            urljoin(self.base_url, path),
            verify=True,
            headers={"User-Agent": self.user_agent},
            params=query
        )
        if response.status_code == 404:
            raise NotFoundError(response.url)
        if jayson:
            try:
                return response.json()
            except JSONDecodeError as e:
                raise NotJsonError(response.content.decode('utf-8')) from e
        else:
            return response.text

    def fetch(self, path: str, query: dict = None, expect_json=True) -> dict | str:
        if path.startswith('/'):
            path = path.removeprefix('/')

        if query is None:
            query = {}
        
        def handle_response(response: dict | str) -> dict:
            if type(response) != dict: # Don't fuck with other stuff    
                return response
            if response.get('error_code', None):
                this = APIerror(response)
                this.add_note("Raised due to API response handler")
                raise this
            return response
        
        if not self.use_cache:
            response = self._fetch(path, query, jayson=expect_json)
            return handle_response(response)
        response: dict  # for type checking
        if response := self.cache_obj.get(path):
            return handle_response(response)

        response = self._fetch(path, query, jayson=expect_json)
        self.cache_obj[path] = response
        return handle_response(response)

    def clear_cache(self):
        if self.use_cache:
            self.cache_obj.clear()
