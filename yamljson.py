#!/usr/bin/env python

import yaml
import json

list = range(9)
list.append('route')
list.append('switch')
list.append({'vendor': 'cisco', 'platform': 'NX-OS'})

with open('yaml.yml', 'w') as yamlfile:
    yamlfile.write(yaml.dump(list, default_flow_style = False))

with open('json.js', 'w') as jsonfile:
    json.dump(list, jsonfile)
