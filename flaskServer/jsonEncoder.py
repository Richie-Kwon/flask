from flask.json import JSONEncoder

class CustomJSONEncoder(JSONEncoder):
    # Overwrite "default" methods
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)

        return JSONEncoder.default(self, obj)

app.json_encoder = CustomJSONEncoder