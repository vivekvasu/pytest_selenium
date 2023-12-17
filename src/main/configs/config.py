from dataclasses import dataclass
from typing import Any


@dataclass
class Config:
    url: str

    @staticmethod
    def from_dict(obj: Any) -> 'Config':
        _url = str(obj.get('url'))
        return Config(_url)
      
