import json
from datetime import datetime
from json import JSONEncoder


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat().replace("T", " ")
        return json.JSONEncoder.default(self, o)


class CustomEncoder(JSONEncoder):
    def default(self, obj):
        if {'quantize', 'year'}.intersection(dir(obj)):
            return str(obj)
        elif hasattr(obj, 'next'):
            return list(obj)
        return JSONEncoder.default(self, obj)
