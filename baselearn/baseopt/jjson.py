import json
import os

with open(data.json, 'w') as f:
    json.dump(data, f)
with open(data.json, 'r') as f:
    json.load(data, f)
