# DATABRICKS 
'''
An IP address is a formatted 32-bit unsigned integer where each group of 8 bits is printed as a decimal number and the dot character '.' splits the groups.

For example, the binary number 00001111 10001000 11111111 01101011 (spaces added for clarity) formatted as an IP address would be "15.136.255.107".
A CIDR block is a format used to denote a specific set of IP addresses. It is a string consisting of a base IP address, followed by a slash, followed by a prefix length k. The addresses it covers are all the IPs whose first k bits are the same as the base IP address.

For example, "123.45.67.89/20" is a CIDR block with a prefix length of 20. Any IP address whose binary representation matches 01111011 00101101 0100xxxx xxxxxxxx, where x can be either 0 or 1, is in the set covered by the CIDR block.
You are given a start IP address ip and the number of IP addresses we need to cover n. Your goal is to use as few CIDR blocks as possible to cover all the IP addresses in the inclusive range [ip, ip + n - 1] exactly. No other IP addresses outside of the range should be covered.

Return the shortest list of CIDR blocks that covers the range of IP addresses. If there are multiple answers, return any of them.

 

Example 1:

Input: ip = "255.0.0.7", n = 10
Output: ["255.0.0.7/32","255.0.0.8/29","255.0.0.16/32"]
Explanation:
The IP addresses that need to be covered are:
- 255.0.0.7  -> 11111111 00000000 00000000 00000111
- 255.0.0.8  -> 11111111 00000000 00000000 00001000
- 255.0.0.9  -> 11111111 00000000 00000000 00001001
- 255.0.0.10 -> 11111111 00000000 00000000 00001010
- 255.0.0.11 -> 11111111 00000000 00000000 00001011
- 255.0.0.12 -> 11111111 00000000 00000000 00001100
- 255.0.0.13 -> 11111111 00000000 00000000 00001101
- 255.0.0.14 -> 11111111 00000000 00000000 00001110
- 255.0.0.15 -> 11111111 00000000 00000000 00001111
- 255.0.0.16 -> 11111111 00000000 00000000 00010000
The CIDR block "255.0.0.7/32" covers the first address.
The CIDR block "255.0.0.8/29" covers the middle 8 addresses (binary format of 11111111 00000000 00000000 00001xxx).
The CIDR block "255.0.0.16/32" covers the last address.
Note that while the CIDR block "255.0.0.0/28" does cover all the addresses, it also includes addresses outside of the range, so we cannot use it.
Example 2:

Input: ip = "117.145.102.62", n = 8
Output: ["117.145.102.62/31","117.145.102.64/30","117.145.102.68/31"]
 

Constraints:

7 <= ip.length <= 15
ip is a valid IPv4 on the form "a.b.c.d" where a, b, c, and d are integers in the range [0, 255].
1 <= n <= 1000
Every implied address ip + x (for x < n) will be a valid IPv4 address.
'''

# APPROACH


'''
Intuition
The idea is pretty straight forward. We track the number of remaining IP addresses we need to generate and what is the number of IP addresses that can be generated from a given IP by forming CIDRs from it.
E.g: 1.2.3.4, if we see the binary representation it ends with '100' i,e 2 trailing zeros so at max we can generate 4 ip address using those last 2 bits 00,01,10,11.

Approach
Create utilities to convert IP from int to str and vice versa
Compute the number of trailing zeros in the starting ip address
Two cases might happen:
3a. The number of trailing zeros is not enough to create n ip addresses. So we create as many ip addresses we can and move on.
3b. The number of trailing zeros is either enough or more than enough. Eg: There are 5 trailing zeros which can create 32 ip addresses but we need only 7. In this case we need to find whats the minimum number of trailing zeros should we use. This is nothing but log2(n).
Every time we compute the number of trailing zeros we need to use, we create the corresponding CIDR and adjust the number of remaining ip addresses to create and starting ip.
Complexity
Time complexity:
O(N)
Space complexity:
O(N)
Code
'''
from typing import List
import math

class Solution:
    def to_ip_int(self, ip_str: str) -> int:
        octets = ip_str.split('.')
        return (int(octets[0]) << 24) | (int(octets[1]) << 16) | (int(octets[2]) << 8) | int(octets[3])

    def find_trailing_zeros(self, ip: int) -> int:
        zeros = 0
        if ip == 0:
            return 32
        while (ip & 1) == 0: # just check the last bit
            zeros += 1
            ip >>= 1
        return zeros

    def create_cidr(self, ip_int: int, prefix_len: int) -> str:
        # Techincally you could (ip_int & MASK) before converting to string
        # since a good practice is to use the base/first IP in cidrs
        # but this works as well.
        octets = [
            str((ip_int >> 24) & 0xFF),
            str((ip_int >> 16) & 0xFF),
            str((ip_int >> 8) & 0xFF),
            str(ip_int & 0xFF),
        ]
        return '.'.join(octets) + '/' + str(prefix_len)

    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        cidrs = []
        startIp = self.to_ip_int(ip)
        while n > 0:
            '''
            If there are k trailing zeros, we can create 2^k ip addresses with it
            Find a c s.t 2^c <= n and 2^(c+1) > n i,e so that using c bits we can
            create 2^c ip addresses.
            Basically c is floor(log2(n))
            eg. if n = 8, we need 3 bits
            '''
            trailing_zeros = self.find_trailing_zeros(startIp)
            c_max_n = n.bit_length() - 1
            #c_max_n = math.floor(math.log2(n))
            c = min(trailing_zeros, c_max_n) 
            network_size = 1 << c
            prefix_len = 32 - c
            cidrs.append(self.create_cidr(startIp, prefix_len))
            n -= network_size
            startIp += network_size
        return cidrs
