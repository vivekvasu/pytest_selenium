from dataclasses import dataclass
from typing import Any


@dataclass
class Config:
    url: str
    db: str

    @staticmethod
    def from_dict(obj: Any) -> 'Config':
        _url = str(obj.get('url'))
        _db = str(obj.get('db'))
        return Config(_url, _db)
      
