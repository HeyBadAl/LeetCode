class Solution:
    def reverseWords(self, s: str) -> str:
        # split
        var1 = s.split()  # multiple space or trailing space

        # reverse list of words, and join to form a string 
        rev_str = ' '.join(reversed(var1))

        return rev_str

solution = Solution() 
input_string = "the sky is blue"
ans = solution.reverseWords(input_string)
print(ans)


# split => break the input string into list of words, handles spaces
# reversed => reverse the list of words
# join => add the reversed words into a string, which are seperated by space.

# Time: O(n), where n is te lenght of the input string. split and join function both take linear time
# Space: O(n), where n is the length of the input string. -> we created a list of words, which could be same as the input string 
