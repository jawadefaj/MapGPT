import json

# Read JSON data from file
with open('exmple.json', 'r') as f:
    data = json.load(f)
def remove_polyline(obj):
    if isinstance(obj, dict):
        for key in list(obj.keys()):
            if key == 'polyline' or key == 'encodedPolyline':
                del obj[key]
            else:
                remove_polyline(obj[key])
    elif isinstance(obj, list):
        for item in obj:
            remove_polyline(item)
    return obj

# Remove polyline and encodedPolyline


# Convert back to JSON string
# modified_json = json.dumps(data, indent=2, ensure_ascii=False)
# print(modified_json)