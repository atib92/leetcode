"""
Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

AllOne() Initializes the object of the data structure.
inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
Note that each function must run in O(1) average time complexity.

 

Example 1:

Input
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
Output
[null, null, null, "hello", "hello", null, "hello", "leet"]

Explanation
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "hello"
allOne.inc("leet");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "leet"
 

Constraints:

1 <= key.length <= 10
key consists of lowercase English letters.
It is guaranteed that for each call to dec, key is existing in the data structure.
At most 5 * 104 calls will be made to inc, dec, getMaxKey, and getMinKey.
"""
class DLLNode:
    def __init__(self, count=-1):
        self.count = count
        self.next = None
        self.prev = None
        self.keys = set()
class AllOne:
    def __init__(self):
        """
        1. Maintain a map of keys -> Nodes
        2. Each node has count and keeps all keys with that count
        3. Create sentiel head and tail nodes for easy linked list manipulations, create utility for inserting/deleting nodes before/after specific nodes.
        """
        self.map = {}
        self.head = DLLNode()
        self.tail = DLLNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    def _debug(self):
        """
        node = self.head
        s = ''
        while(node is not self.tail):
            s += f'{node}{node.count}({node.keys}->)'
            node = node.next
        print(s)
        """
        pass
    def _insert_after(self, new_node:DLLNode, after:DLLNode):
        after.next.prev = new_node
        new_node.next = after.next
        after.next = new_node
        new_node.prev = after
    def _insert_before(self, new_node:DLLNode, before:DLLNode):
        before.prev.next = new_node
        new_node.prev = before.prev
        new_node.next = before
        before.prev = new_node
    def _delete(self, node:DLLNode):
        node.prev.next = node.next
        node.next.prev = node.prev
    def _nodes(self):
        return not self.head.next is self.tail
    def inc(self, key: str) -> None:
        node = self.map.get(key)
        if node is None:
            # New key
            if self.head.next.count == 1:
                self.head.next.keys.add(key)
                self.map[key] = self.head.next
            else:
                new_node = DLLNode(1)
                new_node.keys.add(key)
                self.map[key] = new_node
                self._insert_after(new_node, self.head)
        else:
            # Key already exists
            node.keys.remove(key)
            if node.next.count == node.count + 1:
                node.next.keys.add(key)
                self.map[key] = node.next
            else:
                new_node = DLLNode(node.count + 1)
                new_node.keys.add(key)
                self.map[key] = new_node
                self._insert_after(new_node, node)
            if not node.keys:
                self._delete(node)
        self._debug()
    def dec(self, key: str) -> None:
        node = self.map.get(key)
        node.keys.remove(key)
        if node.count > 1:
            if node.prev.count == node.count - 1:
                node.prev.keys.add(key)
                self.map[key] = node.prev
            else:
                new_node = DLLNode(node.count - 1)
                self.map[key] = new_node
                new_node.keys.add(key)
                self._insert_before(new_node, node)
        else:
            del self.map[key]
        if not node.keys:
            self._delete(node)
        self._debug()
    def getMaxKey(self) -> str:
        if self._nodes():
            return next(iter(self.tail.prev.keys))
        else:
            return ""
    def getMinKey(self) -> str:
        if self._nodes():
            return next(iter(self.head.next.keys))
        else:
            return ""

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
