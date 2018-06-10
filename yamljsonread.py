#!/usr/bin/env python

import yaml
import json
from pprint import pprint as pp

with open('yaml.yml') as yamlfile:
    yaml_list = yaml.load(yamlfile)
    pp(yaml_list)

with open('json.json') as jsonfile:
    json_list = json.load(jsonfile)
    pp(json_list)
