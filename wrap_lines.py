"""
 Connecting words with '-' as blank spaces, no exceeds maxLength
 
 input: ["1p3acres", "is", "a", "good", "place", "to", "communicate"], 12
 output: {"1p3acres-is", "a-good-place", "to", "communicate"}



-- Algorithm --

string_builder = "1p3acres"
result = []

- Iterate over the words
- If we don't have any words, add it to our builder
- Otherwise, if len(string_builder)+1+len(new_word) <= maxLength, we add
the new word with a dash.
- Else, in the case we cannot add the new word, we save the current builder
in our result
and add the word to the new builder
- When we reach the last word, we might have a string builder left, so
we have to remember to add what is left in the result in case its length
is not zero

Time Complexity: O(n)
Space Complexity: O(n)
"""

def wrap_lines(input_list, maxLength):
    string_builder = ""
    res = []
    for word in input_list:
        if len(string_builder) == 0:
            string_builder += (word)
        elif len(string_builder) + len('-' + word) <= maxLength:
            string_builder += '-' + (word) 
        else:
            res.append(string_builder)
            string_builder = word

    res.append(string_builder)

    print(res)
    return res

# wrap_lines(["1p3acres", "is", "a", "good", "place", "to", "communicate"], 12)

'''
Pt.2 Require every line to be "balanced".

Input: String[] lines, ["the way it moves like me", "another sentence example",...], int maxLength.
Output: List lines.

e.g. ["123 45 67 8901234 5678", "12345 8 9 0 1 23"], 10 => {"123--45-67", "8901234", "5678-12345", "8-9-0-1-23"}
["123 45 67 8901234 5678", "12345 8 9 0 1 23"], 15 => {"123----45----67", "8901234----5678", "12345---8--9--0", "23"}
'''
def wrap_lines_balanced(input_list, maxLength):
    string_builder = ""
    unbalanced = []
    for word in input_list:
        if len(string_builder) == 0:
            string_builder += (word)
        elif len(string_builder) + len('-' + word) <= maxLength:
            string_builder += '-' + (word) 
        else:
            unbalanced.append(string_builder)
            string_builder = word

    unbalanced.append(string_builder)

    print(unbalanced)

    balanced = []

    for string in unbalanced:
        diff = maxLength - len(string)
        if '-' not in string:
            balanced.append(string)
        else:
            idx = string.index('-')
            string_start = string[:idx + 1]
            string_end = string[idx + 1:]
            string_mid = ''
            while diff > 0:
                string_mid += '-'
                diff -= 1
            final_string = string_start + string_mid + string_end
            balanced.append(final_string)
    
    print(balanced)
    return balanced
    

wrap_lines_balanced(["123", "45", "67", "8901234", "5678", "12345", "8" ,"9", "0", "1", "23"], 10)
wrap_lines_balanced(["123", "45", "67", "8901234", "5678", "12345", "8" ,"9", "0", "1", "23"], 15)
# wrap_lines_balanced(["1p3acres", "is", "a", "good", "place", "to", "communicate"], 12)