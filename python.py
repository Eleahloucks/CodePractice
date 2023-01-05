#724 Find pivot index

# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
# Return the leftmost pivot index. If no such index exists, return -1.

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums) #22
        for index, num in enumerate(nums):
            #we dont want compare current num
            right -= num

            if left != right:
                left += num
            else:
                return index
        return -1

"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)



def get_all_evens(nums):
    for num in nums:
        if num % 2 == 0:
            return num


def get_odd_indices(items):
    result =[]
    for i in range(len(items)):
        if i % 2 != 0:
            result.append(i)
    return result


def print_as_numbered_list(items):
    i = 1
    for item in items:
        print(f'{i}. {item}')
        i += 1




def get_range(start, stop):
    nums=[]

    for i in range(start, stop):
        nums.append(i)

    return nums



## get longest string

def get_longest(strings):
    longest = ""

    for s in strings:
        if len(s) > len(longest):
            longest = s

    return longest

## QUEUE PRACTICE

class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        """Add `item` to the queue. Runtime: O(1)."""

        self.data.append(item)

    def dequeue(self):
        """Remove and return first item in queue. Runtime: O(n)."""

        if self.is_empty():
            return None
        return self.data.pop(0)

    def is_empty(self):
        """Returns True if queue is empty. Runtime: O(1)."""

        return self.data == []
# Better solution using a deque:

from collections import deque


class BetterQueue:
    def __init__(self):
        self.data = deque()

    def enqueue(self, item):
        """Add `item` to the queue. Runtime: O(1)."""

        self.data.append(item)

    def dequeue(self):
        """Remove and return first item in queue. Runtime: O(1)."""

        if self.is_empty():
            return None
        return self.data.popleft()

    def is_empty(self):
        """Returns True if queue is empty. Runtime: O(1)."""

        if self.data:
            return False
        else: