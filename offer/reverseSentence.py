# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        ss=s.split(' ')
        ss.reverse()
        return ' '.join(ss)

if __name__ == "__main__":
    sentence = 'I am a student.'
    solution = Solution()
    solution.ReverseSentence(sentence)