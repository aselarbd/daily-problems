"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network
and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

You are not allowed to solve the problem using any serialize methods (such as eval).



Example 1:

Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]
Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);

Example 2:

Input: dummy_input = [""]
Output: [""]


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] contains any possible characters out of 256 valid ASCII characters.


Follow up: Could you write a generalized algorithm to work on any possible set of characters?
"""


# Solution 1
class Codec:
    SPACE = '@###@'

    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        strs_updated = [Codec.SPACE if s == "" else s for s in strs]

        word_list = []
        for s in strs_updated:
            word = ":".join([str(ord(c)) for c in s])
            word_list.append(word)

        return " ".join(word_list)

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings.
        """
        raw_encode = []
        for word in s.split(' '):
            raw_encode.append(''.join(chr(int(c)) for c in word.split(':')))

        return ["" if raw == Codec.SPACE else raw for raw in raw_encode]


# Solution 2
class Codec:
    DELI = '#'

    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string.
        """

        return "".join([str(len(s)) + Codec.DELI + s for s in strs])

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        current_str = s
        result = []

        while i < len(s):
            index = current_str.find(Codec.DELI)

            length = int(current_str[:index])
            if length == 0:
                result.append("")
                current_str = current_str[index + 1:]
            else:
                result.append(current_str[index + 1:index + 1 + length])
                current_str = current_str[index + 1 + length:]

            i = i + (index + 1 + length)

        return result
