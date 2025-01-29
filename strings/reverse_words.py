class ReverseWords:

    def reverse(words, ptr1, ptr2):
        while ptr1 < ptr2:
            words[ptr1], words[ptr2] = words[ptr2], words[ptr1]
            ptr1 += 1
            ptr2 -= 1

    def format_string(words):
        n = len(words)
        ptr1 = 0
        result = ''
        while ptr1 < n:
            while ptr1 < n and words[ptr1] != ' ':
                result += words[ptr1]
                ptr1 += 1
            result = result + ' ' if ptr1 < n - 1 else result
            while ptr1 < n and words[ptr1] == ' ':
                ptr1 += 1
        return result.strip()
                

    def reverseWords(s: str) -> str:
        ptr1, ptr2 = 0, len(s) - 1
        words = list(s)
        self.reverse(words, ptr1, ptr2)
        ptr1, ptr2 = 0, 0
        while ptr1 < len(words):
            ptr2 = ptr1
            while ptr2 < len(words) and words[ptr2] != ' ':
                ptr2 += 1
            self.reverse(words, ptr1, ptr2-1)
            ptr1 = ptr2
            while ptr1 < len(words) and words[ptr1] == ' ':
                ptr1 += 1
        return self.format_string(words)

# test the function
rs = ReverseWords()
s = "the sky is blue"
print(rs.reverseWords(s)) # expected output: "blue is sky the"