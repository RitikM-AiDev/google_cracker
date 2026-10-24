class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str,arriveBob: str, leaveBob: str) -> int:
        arr={1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        a = max(arriveAlice,arriveBob)
        b = min(leaveAlice,leaveBob)
        if a > b:
            return 0
        st_days=0
        finish_days=0
        st_month,st_day = map(int,a.split('-'))
        finish_month,finish_day = map(int,b.split('-'))
        for i in range(1,st_month):
            st_days+=arr[i]
        for i in range(1,finish_month):
            finish_days+=arr[i] 
        st_days+=st_day
        finish_days+=finish_day
        return abs(st_days - finish_days) +1
