def minEatingSpeed(self, piles: List[int], h: int) -> int:
    if len(piles) == h:
        return max(piles)
    
    l, r = 1, max(piles)
    finalK = 0

    while l <= r:
        k = l + (r - l) // 2

        time = 0
        for i in piles:
            # print("time", time , " k:", k)
            time+= math.ceil(i / k)
        
        # print("1) finalK:",finalK)
        if time <= h:
            finalK = k
            r = k - 1
        else:
            l = k + 1
        
        # print("2) finalK:",finalK)
    
    return finalK