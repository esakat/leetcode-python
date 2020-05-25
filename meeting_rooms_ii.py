from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # imos method
        time_table = [0] * 1000000
        end_time = 0
        for v in intervals:
            s, e = v[0], v[1]
            time_table[s] += 1
            time_table[e] -= 1
            end_time = max(end_time, e)

        required_rooms = [0] * 1000001

        required_rooms_count = 0
        for i, v in enumerate(time_table):
            if i > end_time:
                break
            if v >= 0:
                required_rooms[i] += v
            else:
                required_rooms[i+1] += v
            required_rooms[i+1] += required_rooms[i]
            required_rooms_count = max(required_rooms_count, required_rooms[i+1])

        return required_rooms_count
