#!/usr/bin/python

from ncclient import manager

device = manager.connect(host='a.b.c.d', port=830, username='netcfg_user', password='netconf', hostkey_verify=False, device_params={'name':'alu'}, allow_agent=False, look_for_keys=False)

print(device)

get_filter = """
<filter>
  <configure>
    <router>
      <interface>
         <interface-name>"system"</interface-name>
      </interface>
    </router>
  </configure>
</filter>
"""
nc_get_reply = device.get_config('running',get_filter)
print(nc_get_reply)
