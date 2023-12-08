
import subprocess


ip_address='192.168.56.101'
username='Prnelabs1'
password='networking123!'
print('')

# Define the commands
commands = [
    "echo deny ip any any option any-options!",
    "echo deny ip any 192.168.25.1 255.255.255.0"
    "echo permit ip any any"
]

# Execute the commands in cmd
for cmd in commands:
   subprocess.run(cmd,shell=True)


commands=[
    "echo configure terminal",
    "echo no ip domain lookup",
    "echo router ospf 101",
    "echo network 192.168.1.0 0.0.0.255 area 0",
    "echo end",
    "echo crypto isakmp enable",
    "echo crypto isakmp policy 10",
    "echo end",
    "echo crypto ipsec transform-set 50 esp-aes 256 esp-sha-hmc",
    "echo crypto ipsec security-association lifetime seconds 1800",
    "echo access-list 101 permit ip 192.168.1.0 0.0.0.255 192.168.3.0 0.0.0.255",
    "echo crypto map CMAP 10 ipsec-isakmp",
    "echo interface G0/0/0",
    "echo crypto map CMAP",
    "echo end"
]
# ssh_command = f'ssh {username}@{ip_address}'
for cmd in commands:
    subprocess.run(cmd, shell=True)




   