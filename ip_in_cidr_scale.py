'''
Code to check if an ipv4 address is allowed/denyed by a set of CIDR.
The normal way of ip & mask == cidr & mask doesn't work at scale since it becomes O(CIDR) and there can be many CIDRs.
The following is Binary Trie / Longest Prefix Match algorithm which is what is used in the kernel or in actual routers
'''

class TrieNode:
    def __init__(self):
        # children[0] -> bit 0
        # children[1] -> bit 1
        self.children = [None, None]
        self.is_allowed = False


class CIDRTrie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def _ip_to_int(ip: str) -> int:
        a, b, c, d = map(int, ip.split('.'))
        return (a << 24) | (b << 16) | (c << 8) | d

    def insert(self, cidr: str):
        network, prefix_str = cidr.split('/')
        prefix = int(prefix_str)

        ip_int = self._ip_to_int(network)

        node = self.root

        # Traverse MSB → LSB (The order is very important here)
        for bit_pos in range(31, 31 - prefix, -1):
            bit = (ip_int >> bit_pos) & 1

            if node.children[bit] is None:
                node.children[bit] = TrieNode()

            node = node.children[bit]

        node.is_allowed = True

    def is_allowed(self, ip: str) -> bool:
        ip_int = self._ip_to_int(ip)

        node = self.root

        for bit_pos in range(31, -1, -1):

            # A CIDR prefix ends here !!
            if node.is_allowed:
                return True

            bit = (ip_int >> bit_pos) & 1

            if node.children[bit] is None:
                return False

            node = node.children[bit]

        return node.is_allowed
