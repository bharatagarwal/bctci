"""
# Action Log Anomalies

You are given an action log from a tech support system.

Each entry is a tuple [agent, action, ticket_number],

- ticket number is a positive integer
- agent is a string
- action is "open" or "close".

The log is sorted chronologically (time order is provided).

Your goal is to find all the tickets with anomalies, in any order. A ticket doesn't have anomalies if:
- It is opened and closed once, in that order.
- The opening and closing agent is the same.
- The agent didn't do any action for a different ticket between opening and closing.

- open count - once
- close count - once

between opening and closing, no other action taken.


Constraints:

- 0 ≤ log.length ≤ 10^5
- Each ticket_number is a positive integer less than 10^6
- Each agent is a non-empty string
- Each action is either "open" or "close"
- The log is sorted chronologically
"""

from collections import defaultdict, namedtuple

TicketAction = namedtuple("TicketAction", ["agent", "action"])
AgentAction = namedtuple("AgentAction", ["action", "ticket_no"])


def find_agent_anomalies(agent_actions):
	anomalies = []
	current_ticket_stack = []

	for agent, actions in agent_actions.items():
		for action in actions:
			activity, ticket_no = action

			if len(current_ticket_stack) == 0:
				if action == "open":
					current_ticket_stack.append(ticket_no)
				elif action == "close":
					anomalies.append(ticket_no)

			if current_ticket_stack[-1] == ticket_no:
				if action == "close":
					current_ticket_stack.pop()
				elif action == "open":
					anomalies.append(ticket_no)


def find_ticket_anomalies(ticket_actions):
	anomalies = []

	for ticket_no, actions in ticket_actions.items():
		if len(actions) != 2:
			anomalies.append(ticket_no)
			continue

		first_agent, first_action = actions[0]
		second_agent, second_action = actions[1]

		if first_action != "open" or second_action != "close":
			anomalies.append(ticket_no)

		elif first_agent != second_agent:
			anomalies.append(ticket_no)

	return anomalies


def find_anomalies(log):
	ticket_actions = defaultdict(list)
	agent_actions = defaultdict(list)

	for agent, action, ticket_no in log:
		ticket_actions[ticket_no].append(TicketAction(agent, action))
		agent_actions[agent].append(AgentAction(action, ticket_no))

	print(find_ticket_anomalies(ticket_actions))
	print(find_agent_anomalies(agent_actions))
	breakpoint()


# ------

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

# dict for every agent
# array - add for open, remove for close

# edge close:
# - close before opening: anomaly (at ticket level)
# - open another: anomaly - at agent level
# - close another: anomaly - at agent level
# - open same multiple times- anomaly at ticket level or agent level
# - what happens after anomaly? count the ticket


find_anomalies(log)  # => [2, 32, 7, 8, 36]

# Explanation:
# - 2 was closed before it was opened.
# - 32 was opened multiple times.
# - 7 was opened and closed by different agents.
# - 8 was opened and closed, but the agent did something in between.
# - 36 was not closed.

# ------

# log = [["Alice", "open", 1], ["Alice", "close", 1]]

# find_anomalies(log)  # => []

# Explanation: The ticket was opened and closed once, in order, by the same agent.

# ------

# log = [["Alice", "open", 1], ["Alice", "open", 1]]

# find_anomalies(log)  # => [1]

# Explanation: The ticket was opened multiple times.

# ------

# log = [
# 	["Drew", "open", 32],
# 	["Drew", "close", 2],
# 	["Drew", "close", 32],
# ]

find_anomalies(log)  # => [2, 32]

# Explanation:
# - 2 was closed without being opened
# - 32 was opened but Drew did another action (closing ticket 2) before closing it

# ------

log = [
	["Dwight", "close", 2],
	["Dwight", "open", 2],
	["Drew", "open", 32],
	["Drew", "open", 2],
	["Drew", "close", 32],
]

find_anomalies(log)  # => [2, 32]

# Explanation:
# - 2 was closed before being opened, and later opened by a different agent
# - 32 was opened but Drew did another action (opening ticket 2) before closing it
