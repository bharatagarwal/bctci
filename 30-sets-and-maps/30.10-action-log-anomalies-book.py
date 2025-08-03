"""
# Action Log Anomalies

You are given an action log, log, from a tech support system. Each entry is a tuple [agent, action, ticket_number], where the ticket number is a positive integer, the agent is a string, and the action is "open" or "close". The log is sorted chronologically.
Your goal is to find all the tickets with anomalies, in any order. A ticket doesn't have anomalies if:
It is opened and closed once, in that order.
The opening and closing agent is the same.
The agent didn't do any action for a different ticket between opening and closing.


Constraints:
- 0 ≤ log.length ≤ 10^5
- Each ticket_number is a positive integer less than 10^6
- Each agent is a non-empty string
- Each action is either "open" or "close"
- The log is sorted chronologically
- Acknowledgements: Thanks to a reader for Examples 4 and 5."""

# map of open tickets -> agent who opened them
# set of already seen tickets
# map from agents to ticket they are currently working on
# set for solution, to avoid duplication

# For each log entry:
# 	- Check if the agent is working on another ticket, and if so, mark that ticket as anomalous
# 	- Skip further processing if the current ticket is already known to be anomalous
# 	- If opening a ticket:
# 		- If already seen, mark as anomalous (opened multiple times)
# 		- Record the agent as working on this ticket
# 	- If closing a ticket:
# 		- If not opened or opened by different agent, mark as anomalous
# 		- Remove the ticket from opened and agent from working
# At the end, any tickets still open are anomalous

# COMMENT FROM BHARAT: This solution systematically works through ticket lifecycle


def find_anomalies(log):
	opened = dict()
	working_on = dict()
	seen = set()
	anomalies = set()

	for agent, action, ticket in log:
		if ticket in anomalies:
			continue

		if action == "open":
			if ticket in seen:
				anomalies.add(ticket)
				continue

			if agent in working_on:
				anomalies.add(working_on[agent])

			opened[ticket] = agent
			working_on[agent] = ticket
			seen.add(ticket)

		else:
			if ticket not in opened or opened[ticket] != agent:
				anomalies.add(ticket)
				continue

			if agent not in working_on or working_on[agent] != ticket:
				anomalies.add(ticket)
				continue

			del working_on[agent]
			del opened[ticket]

	anomalies.update(opened.keys())
	return list(anomalies)


log = [
	["Dwight", "close", 2],
	["Dwight", "open", 2],
	["Drew", "open", 32],
	["Drew", "close", 32],
	["Drew", "open", 32],
	["Drew", "close", 32],
	["Susa", "open", 7],
	["Jo", "close", 7],
	["Susa", "open", 33],
	["Jo", "open", 8],
	["Jo", "open", 36],
	["Jo", "close", 8],
	["Susa", "close", 33],
]

print(find_anomalies(log))  # => [2, 32, 7, 8, 36]

# Explanation:
# - 2 was closed before it was opened.
# - 32 was opened multiple times.
# - 7 was opened and closed by different agents.
# - 8 was opened and closed, but the agent did something in between.
# - 36 was not closed.

log = [["Alice", "open", 1], ["Alice", "close", 1]]

print(find_anomalies(log))  # => []

# Explanation: The ticket was opened and closed once, in order, by the same
# agent.

log = [["Alice", "open", 1], ["Alice", "open", 1]]

print(find_anomalies(log))  # => [1]

# Explanation: The ticket was opened multiple times.

log = [
	["Drew", "open", 32],
	["Drew", "close", 2],
	["Drew", "close", 32],
]

print(find_anomalies(log))  # => [2, 32]

# Explanation:
# - 2 was closed without being opened
# - 32 was opened but Drew did another action (closing ticket 2) before closing
# it

log = [
	["Dwight", "close", 2],
	["Dwight", "open", 2],
	["Drew", "open", 32],
	["Drew", "open", 2],
	["Drew", "close", 32],
]

print(find_anomalies(log))  # => [2, 32]

# Explanation:
# - 2 was closed before being opened, and later opened by a different agent
# - 32 was opened but Drew did another action (opening ticket 2) before closing
# it
