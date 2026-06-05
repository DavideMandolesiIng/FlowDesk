import json
from pathlib import Path
from datetime import date, datetime

class BaseRepository:
    def __init__(self, filepath: Path) -> None:
        self.filepath=filepath

        if not filepath.exists():
            filepath.parent.mkdir(parents=True, exist_ok=True)
            filepath.write_text("[]")

    def _readAll(self) -> list[dict]:
        return json.loads(self.filepath.read_text())
    
    def _writeAll(self, data: list[dict]) -> None:
        self.filepath.write_text(json.dumps(data, indent=2, default=self._serialize))

    def _serialize(self, obj):
        '''Handles non-serializable by default types'''
        if isinstance(obj,(date,datetime)):
            return obj.isoformat()
        if hasattr(obj, 'value'):
            return obj.value
        raise TypeError(f"Non serializable type: {type(obj)}")