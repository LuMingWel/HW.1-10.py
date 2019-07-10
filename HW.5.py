class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return True if word.lower() == word or word.upper() == word or word== word.title() else False