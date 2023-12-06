# Import required modules/packages/library
import pexpect
from pprint import pprint
import re

# Display heading
print('')
print('Interface, routes list, routes details')
print('--------------------------------------')

# Create regular expressions to match interfaces and OSPF
OSPF_pattern = re.compile(r'0.+')
intf_pattern = re.compile(r'(GigabitEthernet)(\d)')

# Create regular expressions to match prefix and routes
prefix_pattern = re.compile(r'(\d(1,3)\.\d(1,3)\.\d(1,3)\.\d(1,3)\/?\d?\d?)')
route_pattern = re.compile(r'via (\d(1,3))\.\d(1,3)\.\d(1,3))')

# Connect to device and run 'show ip route' command
print('--- connecting telnet 192.168.56.101 with prne/cisco123')

session = pexpect.spawn('telnet 192.168.56.101', encoding='utf-8',timeout=20)
result = session.expect(['Username:', pexpect.TIMEOUT, pexpect.EOF])

# Check for failure
if result != 0:
    print('Timeout or unexpected reply from device')
    exit()

# Enter username
session.sendline('prne')
result = session.expect('Password')

# Enter password
session.sendline('cisco123!')
result = session.expect('>')

# Must set terminal length to zero for long replies, no pauses
print('--- setting terminal length to 0')
session.sendline('terminal lenth 0')
result = session.expect('>')

# Run the 'show ip route' command on device
print('--- successfully logged into device, running show ip route command')
session.sendline('show ip route')
result = session.expect('>')

# Display the output of the command, for comparison
print('--- show ip route output:')
show ip route_output = session.before
print(show_ip_route_output)

# Get the output from the command into a list of lines from the output
routes_list = show_ip_route_output.splitlines()

# Create dictionary to hold number of routes per interface
intf_routes = {}

# Go through the list of routes to get routes per interface
for route in routes_list:

    OSPF_match = OSPF_pattern.search(route)
    if OSPF_match:

        # Match for GigabitEthernet interfaces string
        intf_match = intf_pattern.search(route)

        # Check to see if we matched the GigabitEthernet interfaces string
        if intf_match:

            # Get the interface from the match
            intf = intf_match.group(2)

            # If route list not yet created, do so now
            if intf not in intf_routes:
                intf_routes[intf] = []
            
            

            # Extract the route
            route_match = route_match
                

        


