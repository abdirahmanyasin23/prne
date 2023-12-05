# Import required modules/packages/library
from pprint import pprint
import re

# Create regular expression to match Gigabit interface names
gig_pattern = re.compile(r'(GigabitEthernet)(\d\/\d\/\d\/\d)')

# Create a directory to hold the count of routes
# forwarded out each interface
routes = {}

# Read all lines of IP routing information
file = open('ip-routes.txt', 'r')
for line in file:

        # Match for Gigabit Ethernet
        match = gig_pattern.search(line)

        # Check to see if we matched the Gig Ethernet string
        if match:
            intf = match.group(2)  # get the interface from the match
            routes[intf] = routes[intf]+1 if intf in routes else 1

# Display heading
print('')
print('Number of routes per interface')
print('------------------------------')

# Display the routes per Gigabit interface
pprint(routes)

# Display a blank line to make easier to read
print('')

# Close the file
file.close()

