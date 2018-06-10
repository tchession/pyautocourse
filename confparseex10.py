#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse
import re

config = CiscoConfParse('cisco_cfg.txt')

no_aes = config.find_objects_wo_child(parentspec=r'crypto map CRYPTO', childspec=r'AES')

for map in no_aes:
    print(map.text)
    for transform_set in map.children:
        if 'transform' in transform_set.text:
            match = re.search(r"set transform-set (.*)$", transform_set.text)
            encryption = match.group(1)
    print("    {} >>> {}".format(map.text.strip(), encryption))
