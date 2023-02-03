class Solution(object):
    def totalFruit(self, fruits):
        max_len = 0
        ptr = 0
        types = []
        while ptr < len(fruits):
            if fruits[ptr] not in types:
                if len(set(types)) == 2:
                    max_len = max(max_len, len(types))
                    i, tmp = len(types) - 1, types[-1]
                    while types[i] == tmp:
                        i-=1
                    types = types[i+1:]               
            types.append(fruits[ptr])
            ptr += 1
        max_len = max(max_len, len(types))
        return max_len
