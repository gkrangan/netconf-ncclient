#!/usr/bin/python

from ncclient import manager

device = manager.connect(host='a.b.c.d', port=830, username='netcfg_user', password='netconf', hostkey_verify=False, device_params={'name':'alu'}, allow_agent=False, look_for_keys=False)

print(device)

cfg = """
 <config>
        <configure xmlns="urn:alcatel-lucent.com:sros:ns:yang:conf-r13">
            <router>
                <router-name>Base</router-name>
                <interface>
                    <interface-name>test</interface-name>
                    <address>
                        <ip-address-mask>40.40.40.40/32</ip-address-mask>
                    </address>
                    <loopback>true</loopback>
                    <shutdown>false</shutdown>
                </interface>
            </router>
        </configure>

 </config>
"""
nc_set_reply = device.edit_config(target='running', config=cfg)

print(nc_set_reply)
