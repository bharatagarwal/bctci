"""
# Current URL

You are implementing the back arrow functionality of a browser. You are given a non-empty array, actions, with the actions that the user has done so far. Each element in actions consists of two elements. The first is the action type, "go" or "back".

When the action is "go", the second element is a URL string. The first action is always "go".

When the action is "back", the second element is a number ≥ 1 with the number of times we want to go back. Going back once means returning to the previous URL we went to with a "go" action. If there are no previous URLs, going back stays at the current one.

Return the current URL the user is on after all actions are performed.

Constraints:
- The length of actions is at most 10^5
- Each URL is a non-empty string
"""


def current_url(actions):
	record = list()

	for action, payload in actions:
		if action == "go":
			record.append(payload)

		if action == "back":
			for _ in range(payload):
				if len(record) > 1:
					record.pop()

	print(record[-1])
	return record[-1]


actions = [
	["go", "google.com"],
	["go", "wikipedia.com"],
	["go", "amazon.com"],
	["back", 4],
	["go", "youtube.com"],
	["go", "netflix.com"],
	["back", 1],
]

current_url(actions)  # => "youtube.com"
