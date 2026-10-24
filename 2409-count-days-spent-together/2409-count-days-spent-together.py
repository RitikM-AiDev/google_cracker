
from datetime import datetime
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str,arriveBob: str, leaveBob: str) -> int:
        alice_arrive = datetime.strptime(arriveAlice, "%m-%d")
        alice_leave = datetime.strptime(leaveAlice, "%m-%d")
        bob_arrive = datetime.strptime(arriveBob, "%m-%d")
        bob_leave = datetime.strptime(leaveBob, "%m-%d")
        start = max(alice_arrive, bob_arrive)
        end = min(alice_leave, bob_leave)

        if start > end:
            return 0

        return (end - start).days + 1
