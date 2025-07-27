"""
# Viewer Counter Class

Streamers make money based on the number of views they receive while streaming. Implement a ViewerCounter class that tracks the number of viewers within a configurable time window for a live stream event. Viewer types may be "guest", "follower", or "subscriber".

Track number of viewers within a time window

- guest
- follower
- subscriber

ViewerCounter:
	- init(window): establishes a window size ≥ 1
	- join(t, v): registers that a viewer of type v joined at time t
	- get_viewers(t, v): gets the viewer count of viewer type v within the time window of length 'window' ending at timestamp t: [t - window, t], with both endpoints included.

- initialise with window size
- join as a viewer of type v at time t
- get viewers of type v, within time window
	- falling in range (t-window, t)


order of joining matters
- three stacks, for guest, follower, subscriber

Both methods accept a timestamp t represented by an integer.

It is guaranteed that each method call receives a time that is greater than or equal to any timestamp used in previous calls to either join() or get_viewers().


Constraints:
	- The number of join and get_viewers operations is at most 10^5 -- joins will have a wider spread than window
	- 1 <= window <= 10^5
"""


class ViewerCounter:
	def __init__(self, window):
		self.window = window
		self.subscribers = list()
		self.guests = list()
		self.followers = list()

	def join(self, timestamp, type):
		match type:
			case "subscriber":
				self.subscribers.append(timestamp)
			case "follower":
				self.followers.append(timestamp)
			case "guest":
				self.guests.append(timestamp)

	def count_within_window(self, start, end, array):
		count = 0

		for index in range(len(array) - 1, -1, -1):
			if array[index] >= start and array[index] <= end:
				count += 1

			if array[index] < start:
				break

		print(count)
		return count

	def get_viewers(self, timestamp, type):
		array = list()

		match type:
			case "subscriber":
				array = self.subscribers
			case "follower":
				array = self.followers
			case "guest":
				array = self.guests

		return self.count_within_window(
			timestamp - self.window, timestamp, array
		)


counter = ViewerCounter(10)
counter.join(1, "subscriber")
counter.join(1, "guest")
counter.join(2, "follower")
counter.join(2, "follower")
counter.join(2, "follower")
counter.join(3, "follower")
counter.get_viewers(10, "subscriber")  # Returns 1
counter.get_viewers(10, "guest")  # Returns 1
counter.get_viewers(10, "follower")  # Returns 4
counter.get_viewers(13, "follower")  # Returns 1
