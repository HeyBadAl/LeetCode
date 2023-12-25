# is permuatations


class Perm:
    def is_permuatations(self, str1, str2):
        if len(str1) != len(str2):
            return False

        count = {}  # dictionary to count the character in str1

        for char in str1:  # O(n), n is the lenght of str1
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        # check for str2
        for char in str2:  # O(n)
            if char in count:
                count[char] -= 1
                if count[char] < 0:
                    # if the count becomes negative, str2 has more occurence of that character in str1
                    return False

            # character in str12 is not present in str1, return  False
            else:
                return False

        # check if all counts are in the count dictionary are zero
        return all(c == 0 for c in count.values())

    # TIME: O(n)
    # SPACE: O(n)


ans = Perm()
str1 = "ab"
str2 =  "asdkasdk"
result = ans.is_permuatations(str1, str2)

if result:
    print("True")
else:
    print("False")
