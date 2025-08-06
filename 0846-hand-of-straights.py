# Leetcode 846 - Hand of Straights
# https://leetcode.com/problems/hand-of-straights/

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False

        hand = sorted(hand)

        while len(hand) != 0:
            start = hand[0]
            for i in range(1, groupSize):
                if start + i in hand:
                    hand.remove(start + i)
                else:
                    return False
                    
            hand.remove(start)
        
        return True
    
"""
Time complexity: O(n^2)
- hand = sorted(hand) takes O(nlgn) time
- in the worst ase, the loop runs n / groupSize times
- .remove() and in on a list are O(n) operstions
- each iteration of the for loop could take O(n) time, and it's done up to n times

Space complexity: O(n)
- hand = sorted(hand) creates a new list, so it's aO(n) extra space

Aproach:
- brute force greedy
- sorting the hand list
- take the smallest card and try to form a group of size groupSize starting from the card
- remove each of these card from the list
- returning True if all cards can be grouped correctly; False if fail to form a full group
"""

# TODO: optimize time complexity

