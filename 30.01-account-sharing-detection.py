"""
You've compiled a list of IP addresses of all the clients connected to your service and the username associated with each one. Assume all IPs are unique and username lengths are between 1 and 30. We say a username is being shared if it appears in two connections. If usernames are being shared, return an IP of any of them. Otherwise, return an empty string.

Example 1: connections = [("203.0.113.10", "mike"), ("298.51.100.25", "bob"),
("292.0.2.5", "mike"), ("203.0.113.15", "bob2")]
Output: "203.0.113.10". User "mike" is connected from that IP and "292.0.2.5",
so "292.0.2.5" would also be a valid output.

Example 2: connections = [("111.0.0.0", "mike"), ("111.0.0.1", "mike"),
("111.0.0.2", "bob"), ("111.0.0.3", "bob")]
Output: "111.0.0.0". Any of the IPs would be a valid output.

Example 3: connections = [("111.0.0.0", "mike"), ("111.0.0.1", "mike2"),
("111.0.0.2", "mike3"), ("111.0.0.3", "mike4")]
Output: ""

Constraints:

- The length of connections is at most 10^5 -- this indicates an expected time complexity. I don't have the figures in mind, but roughly around O(n)
- All IPs are unique -- no edge cases
- Username lengths are between 1 and 30 characters -- constant time hashing
- All usernames contain only lowercase letters -- no validation
"""

from collections import defaultdict

connections = [
	("203.0.113.10", "mike"),
	("298.51.100.25", "bob"),
	("292.0.2.5", "mike"),
	("203.0.113.15", "bob2"),
]

connections_2 = [
	("111.0.0.0", "mike"),
	("111.0.0.1", "mike"),
	("111.0.0.2", "bob"),
	("111.0.0.3", "bob"),
]

connections_3 = [
	("111.0.0.0", "mike"),
	("111.0.0.1", "mike2"),
	("111.0.0.2", "mike3"),
	("111.0.0.3", "mike4"),
]


def identify_shared_ip(connections):
	seen = set()

	for address, username in connections:
		if username in seen:
			return address

		seen.add(username)

	return ""


print(repr(identify_shared_ip(connections)))
print(repr(identify_shared_ip(connections_2)))
print(repr(identify_shared_ip(connections_3)))

# How can I optimise my solution for a 100,000 long list of connections
# Since all IP addresses are unique, a duplicate username would also imply a shared connection.

# First solution
# Time complexity: O(n)
# Space complexity: O(users) + 1

# Second solution
# Time complexity: O(n)
# Space complexity: O(users)
