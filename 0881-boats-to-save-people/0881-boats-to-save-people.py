class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i=0
        boat=0
        j=len(people)-1
        print(people)
        while i<=j:
            if people[i] + people[j] <=limit:
                boat+=1
                i+=1
                j-=1
            elif people[j]<=limit:
                j-=1
                boat+=1
        return boat          
        

            