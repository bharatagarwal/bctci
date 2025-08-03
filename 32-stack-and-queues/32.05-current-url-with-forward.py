"""
# Current URL with Forward


You are implementing the back arrow functionality of a browser with an additional "forward" action. You are given a non-empty array, actions, with the actions that the user has done so far. Each element in actions consists of two elements. The first is the action type, "go", "back", or "forward".

When the action is "go", the second element is a URL string. The first action is always "go".

When the action is "back", the second element is a number ≥ 1 with the number of times we want to go back. Going back once means returning to the previous URL we went to with a "go" action. If there are no previous URLs, going back stays at the current one.

When the action is "forward", the second element is a number ≥ 1 with the number of times we want to go forward.

Going forward past the last page that we have gone to does nothing.

Return the current URL the user is on after all actions are performed.

Constraints:
- The length of actions is at most 10^5
- Each URL is a non-empty string
"""


def current_url(actions):
	record = []
	current_index = 0

	for action, payload in actions:
		if action == "go":
			if current_index != len(record) - 1:
				# clear forward history
				for _ in range(current_index + 1, len(record)):
					record.pop()

			record.append(payload)	
			current_index += 1

		elif action == "back":
			current_index = max(1, current_index - payload)
		elif action == "forward":
			current_index = min(
				len(record) - 1, current_index + payload
			)

	print(record[current_index])
	return record[current_index]


actions = [
	["go", "google.com"],
	["go", "wikipedia.com"],
	["back", 1],
	["forward", 1],
	["back", 3],
	["go", "netflix.com"],
	["forward", 3],
]

current_url(actions)  # => "netflix.com"
