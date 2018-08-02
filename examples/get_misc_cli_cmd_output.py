#!/usr/bin/python

from ncclient import manager

device = manager.connect(host='a.b.c.d', port=830, username='netcfg_user', password='netconf', hostkey_verify=False, device_params={}, allow_agent=False, look_for_keys=False)

print(device)

get_filter = """
   <oper-data-format-cli-block>
      <cli-show>router interface "system"</cli-show>
      <cli-show>system security ssh</cli-show>
      <cli-show>router route-table</cli-show>
   </oper-data-format-cli-block>
"""

nc_get_reply = device.get(('subtree', get_filter))
print(nc_get_reply)
