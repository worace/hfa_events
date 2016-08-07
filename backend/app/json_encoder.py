from flask.json import JSONEncoder
from decimal import Decimal

class DecimalSafeJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        else:
            return JSONEncoder.default(self, obj)
