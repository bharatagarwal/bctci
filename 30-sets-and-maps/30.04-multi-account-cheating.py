"""
# Multi-Account Cheating

Our company runs an online game where the terms of service state that each person can only have one account.

We have a list of usernames and the (unordered) list of IP addresses that they have ever connected from. We say two users are suspected of belonging to the same person if the list of IPs is the same. Return whether any two lists contain the exact same set of IPs.

Each person can only have one account.

- unordered list of IP addresses
- same person if the list is the same

Example 1: users = [
  ("mike", ["203.0.3.10", "208.51.0.5", "52.0.2.5"]),
  ("bob", ["111.0.0.10", "222.0.0.5", "222.0.0.8"]),
  ("bob2", ["222.0.0.5", "222.0.0.8", "111.0.0.10"])
]

Output: True. Users "bob" and "bob2" have the same IPs.


Example 2: users = [
  ("alice", ["1.1.1.1"]),
  ("bob", ["2.2.2.2"])
]

Max 10 IPs

Output: False. No two users have the same IPs.

For each user, keep track of their IP address,
	- by iterating over their IP addresses and storing in a set

Using a two pointer approach, start with the first user and compare their IP address with the remaining users

Then move pointer to send user, comparing with remaining users

if any matches, then we're looking at someone having multiple accounts.

Example 3: users = []
Output: False. There are no users.


Constraints:

- The length of users is at most 10^5
- Each username is non-empty and unique
- Each list of IPs has between 1 and 10 IPs
- All IPs are unique and follow the IPv4 format
- Each octet is a number between 0 and 255
"""


def any_cheating_users(ip_details):
	if not ip_details:
		return False

	ip_sets = []

	for user_tuple in ip_details:
		ip_sets.append(set(user_tuple[1]))

	for i in range(len(ip_sets)):
		for j in range(i + 1, len(ip_sets)):
			if ip_sets[i] == ip_sets[j]:
				return True

	return False


users = [
	("mike", ["203.0.3.10", "208.51.0.5", "52.0.2.5"]),
	("bob", ["111.0.0.10", "222.0.0.5", "222.0.0.8"]),
	("bob2", ["222.0.0.5", "222.0.0.8", "111.0.0.10"]),
]

print(any_cheating_users(users))  # => True

users = [("alice", ["1.1.1.1"]), ("bob", ["2.2.2.2"])]

print(any_cheating_users(users))  # => False

users = []
print(any_cheating_users(users))  # => False
