#!/usr/bin/python

from ncclient import manager

device = manager.connect(host='a.b.c.d', port=830, username='netcfg_user', password='netconf', hostkey_verify=False, device_params={'name':'alu'}, allow_agent=False, look_for_keys=False)

print(device)

nc_get_reply = device.get_config('running')
print(nc_get_reply)
