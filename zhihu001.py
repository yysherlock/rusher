"""
Given an array A,
max(A[i], A[j]), i < j
"""
import unittest

def main1(A):
    """
    Divide and Conquer:
        O(NlogN)
    """
    if len(A)==1: return -float('Inf')
    if len(A)==2:
        return A[0] - A[1]
    left = 0
    right = len(A)
    mid = (left + right) / 2
    
    left_max = main1(A[left:mid+1])
    right_max = main1(A[mid+1:right])
    inter_max = max(A[left:mid+1]) - min(A[mid+1:right])

    return max(left_max, right_max, inter_max)

def main2(A):
    """
    Dynamic : O(N)
    """
    pass

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main1([1,2]), -1)
        self.assertEqual(main1([8,9,10,1]), 9)
        self.assertEqual(main1([1,2,4,2,7,-3]), 10)
if __name__=="__main__":
    unittest.main()
