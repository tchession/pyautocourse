#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

config = CiscoConfParse("cisco_cfg.txt")

crypto_map = config.find_objects(r"^crypto map CRYPTO")

for map in crypto_map:
    print(map.text)
    for cmap_config in map.children:
        print(cmap_config.text)
