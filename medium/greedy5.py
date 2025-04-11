from typing import Counter, List


class NStraightHand:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()

        cnt = Counter(hand)
        for n in hand:
            if cnt[n] == 0:
                continue
            start = n
            while cnt[start-1] != 0:
                start -= 1
            for i in range(start, start+groupSize):
                if cnt[i] == 0:
                    return False
                cnt[i] -= 1

        return True
        
