# https://leetcode.com/problems/group-anagrams/


# time  = O(m*n) where m is the number of solutions and n is avg length of the string.
# space  = O(m*n)

from collections import defaultdict


def groupAnagrams(strs):

    res = defaultdict(list)  # mapping character count to list anagrams

    for s in strs:
        count = [0] * 26  # a...z
 
        for c in count:
            # We have to map a to 0 and z to 25
            # eg a = 80 -> 0, 80 -80
            #    b = 81 -> 1, 81 - a

            count[ord(c) - ord("a")] += 1

        # append the count to the hasmap
        res[tuple(count)].append(s)

    # return only values
    return res.values()


def groupAnagrams(strs):
    hashmap = defaultdict(list)

    for s in strs:

        # keys can be strings, bcz they are immutable.
        hashmap[str(sorted(s))].append(s)
    return hashmap.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
