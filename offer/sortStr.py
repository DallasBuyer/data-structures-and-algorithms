
class Solution:
    def Permutation(self, ss):
        if len(ss) <= 0:
            return []
        result = list()
        self.perm(ss, result, '')
        uniq = list(set(result))
        return sorted(uniq)
    def perm(self, ss, result, path):
        if ss == '':
            result.append(path)
        else:
            for i in range(len(ss)):
                self.perm(ss[:i] + ss[i+1:], result, path+ss[i])

if __name__ == "__main__":
    ss = 'abc'
    solution = Solution()
    results = solution.Permutation(ss)
    print(results)
 