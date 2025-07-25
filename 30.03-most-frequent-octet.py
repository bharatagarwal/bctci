"""
# Most Frequent Octet

You've compiled a list of IP addresses of all the clients connected to your service. Assume all IPs are unique and follow the IPv4 format, which consists of four 8-bit numbers (called octets) separated by dots. Return the most common first octet among the connections.

octet is a representation of 2^8, max 255

This can essentially be considered a list of integers, and I have to find the most occurences of one.

I can keep a sparse array with indices 0 to 255, and make that keep count for each.

And then return the max from that array.

Example 1: ips = ["203.0.113.10", "208.51.100.5", "202.0.2.5", "203.0.113.5"]
Output: "203". 203 appears twice as the first octet.

Example 2: ips = ["10.0.0.1", "10.0.0.2", "192.168.1.1"]
Output: "10". 10 appears twice as the first octet, while 192 appears once.

Example 3: ips = []
Output: None. There are no IP addresses.

Constraints:
- The length of ips is at most 10^5
- All IPs are unique and follow the IPv4 format
- Each octet is a number between 0 and 255
"""


def find_most_common_octet(ips):
	if not ips:
		return None

	octet_record = [0] * 256

	for ip in ips:
		octet_record[int(ip.split(".")[0])] += 1

	max_count = 0
	index = 0

	for idx, record in enumerate(octet_record):
		if record > max_count:
			max_count = record
			index = idx

	return str(index)


ips = ["203.0.113.10", "208.51.100.5", "202.0.2.5", "203.0.113.5"]

print(repr(find_most_common_octet(ips)))

ips = ["10.0.0.1", "10.0.0.2", "192.168.1.1"]

print(repr(find_most_common_octet(ips)))

ips = []

print(repr(find_most_common_octet(ips)))
