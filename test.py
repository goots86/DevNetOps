from netmiko import ConnectHandler

ers = {
    'device_type': 'extreme_ers',
    'ip':   '10.210.209.243',
    'username': 'RW',
    'password': 'securepasswd',
    #'port' : 8022,          # optional, defaults to 22
    #'secret': 'secret',     # optional, defaults to ''
    #'verbose': False,       # optional, defaults to False
}

net_connect = ConnectHandler(**ers)

output = net_connect.send_command('show interfaces')
print(output)

config_commands = [ 'interface ethernet 2',
                    'shutdown']

output = net_connect.send_config_set(config_commands)
print(output)

output = net_connect.send_command('show interfaces')
print(output)
