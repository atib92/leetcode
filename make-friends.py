"""
Input: N = 4, arr[] = {{0, 1, 2}, {1, 2, 3}, {2, 3, 4}}
Output: 4
Explanation: Initially, the number of people are 4, i.e, {0}, {1}, {2}, {3}.


At time = 2, {0} and {1} became friends. Therefore, the group of acquainted people becomes {0, 1}, {2}, {3}.
At time = 3, {1} and {2} became friends. Therefore, the group of acquainted people becomes {0, 1, 2}, {3}.
At time = 4, {2} and {3} became friends. Therefore, the group of acquainted people becomes {0, 1, 2, 3}.

Hence, at time = 4, every person became acquainted with each other.


Input: N = 6, arr[] = {{0, 1, 4}, {3, 4, 5}, {2, 3, 14}, {1, 5, 24}, {2, 4, 12}, {0, 3, 42}, {1, 2, 41}, {4, 5, 11}}
Output: 24

Source: https://www.geeksforgeeks.org/the-earliest-moment-when-everyone-become-friends/
"""

def friend_to_set(friend, all_sets):
    for index, _set in enumerate(all_sets):
        if friend in _set:
            return index, _set
    print(f'ERROR friend {friend} not in {all_sets}')
    exit(1)

def make_friends(N, data):
    # Sort data based on timestamp
    data = sorted(data, key=lambda x:x[2])
    # Initially there will be N sets with each friend in their own set.
    all_sets = [{friend} for friend in range(N)]
    for friendship in data:
        friendA, friendB, timestamp = friendship[0], friendship[1], friendship[2]
        indexA, setA = friend_to_set(friendA, all_sets)
        indexB, setB = friend_to_set(friendB, all_sets)
        # This allows easy update of the all_sets list. You can rmeove the larger indexed set from the list w/o chaning the position of other sets. See [1]
        if indexA > indexB:
            index_small, index_large = indexB, indexA
        elif indexA < indexB:
            index_small, index_large = indexA, indexB
        else:
            # Already in same set
            continue
        union_set = set.union(setA, setB)
        # [1]
        all_sets.pop(index_large)
        all_sets[index_small] = union_set
        if len(all_sets) == 1:
            return timestamp
    return +100000



if __name__ == "__main__":
    N = 4
    data = [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
    print(make_friends(N, data))
    N = 6
    data = [[0, 1, 4], [3, 4, 5], [2, 3, 14], [1, 5, 24], [2, 4, 12], [0, 3, 42], [1, 2, 41], [4, 5, 11]]
    print(make_friends(N, data))

"""
Output
(env) atib$ python make-friends.py 
4
24
"""
