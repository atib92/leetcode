class Solution:
    def primeFac(self, num):
        # Find all prime factors > 1
        factors = []
        d = 2
        while d*d <= num:
            if num % d == 0:
                factors.append(d)
                # remove all mutiples of d (so that 2 and 4 both are not counted for num=20 sort of thing !)
                while num % d == 0:
                    num //= d
            d += 1
        if num > 1:
            # if the number left is itself a prime number
            factors.append(num)
        return factors
