class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word_list=s.split(' ')
        output=[]
        for word in word_list:
            reverse_word = word[::-1]
            output.append(reverse_word)
        return ' '.join(output)        