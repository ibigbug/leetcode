# Link: https://oj.leetcode.com/problems/simplify-path/
class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        isAbs = path[0] == '/'
#        traillingSlash = path[-1] == '/'

        arr = filter(lambda p: p != '', path.split('/'))

        ret = []
        for p in arr:
            if p == '..':
                if len(ret):
                    ret.pop()
            elif p == '.':
                continue
            else:
                ret.append(p)
        ret = '/'.join(ret)

        if not ret and not isAbs:
            ret = '.'
#        if ret and traillingSlash:
#            ret += '/'

        return '/' + ret if isAbs else ret
