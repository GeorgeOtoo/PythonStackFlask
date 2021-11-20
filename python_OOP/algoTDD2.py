import unittest

from algoTDD import reverseList, isPalindrome, coins, factorial, fib

class reverseListTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(reverseList([1,3,5]), [5,3,1])
    def test2(self):
        return self.assertEqual(reverseList([2,4,-3]), [-3,4,2])

class isPalindromeTest(unittest.TestCase):
    def test1(self):
        return self.assertTrue(isPalindrome("racecar"))
    def test2(self):
        return self.assertFalse(isPalindrome("bingoob"))

class coinsTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(coins(87), [3,1,0,2])
    def test1(self):
        return self.assertEqual(coins(92), [3,1,1,2])

class factorialTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(factorial(5), 120)
    def test1(self):
        return self.assertNotEqual(factorial(1), 0)

class fibTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(fib(2), 2)
    def test1(self):
        return self.assertEqual(fib(1), 1)
if __name__ == "__main__":
    unittest.main()