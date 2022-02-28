from flask.json import JSONEncoder

class CustomJSONEncoder(JSONEncoder):
    # Overwrite "default" methods
    # Change the set to list because the set type can't be coverted into JSON.
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)

        return JSONEncoder.default(self, obj)

app.json_encoder = CustomJSONEncoder