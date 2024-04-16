from dataclasses import dataclass

from .errors import CacheLibNotFound


@dataclass
class Wattpad:
    base_url: str = "https://www.wattpad.com/api"
    use_cache: bool = True

    def __post_init__(self):
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


def main():
    wpad = Wattpad()


if __name__ == "__main__":
    main()
