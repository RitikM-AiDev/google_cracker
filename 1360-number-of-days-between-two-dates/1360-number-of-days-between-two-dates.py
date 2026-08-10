class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        y1,m1,d1 = map(int,date1.split('-'))
        y2,m2,d2 = map(int,date2.split('-'))
        month_days = [31, 28, 31, 30, 31, 30,
                      31, 31, 30, 31, 30, 31]
        day1 = ((y1-1)*365) + \
         ((y1-1) // 4 - (y1-1) // 100 + (y1-1) // 400)
        day2 = ((y2-1)*365) +  \
        ((y2-1) // 4 - (y2-1) // 100 + (y2-1) // 400)
        day1+=sum(month_days[:m1-1])
        day2+=sum(month_days[:m2-1])
        if m1>2 and (y1 % 4 == 0 and (y1 % 100 != 0 or y1 % 400 == 0)):
            day1+=1
        if m2>2 and (y2 % 4 == 0 and (y2 % 100 != 0 or y2 % 400 == 0)):
            day2+=1
        day1+=d1
        day2+=d2
        return abs(day2 - day1)

