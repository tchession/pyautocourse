#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

config = CiscoConfParse("cisco_config.txt")

pfs_group_2 = config.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec = r"pfs group2")

print(pfs_group_2.text)
