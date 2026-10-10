class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            for ch in string:
                encoded_string = encoded_string + chr(ord(ch)+2) 
            encoded_string = encoded_string + '!'
        return encoded_string
    
    def decode(self, s: str) -> List[str]:
        decoded_list = []
        temp_string = ""
        for ch in s:
            if ch != '!':
                temp_string = temp_string + chr(ord(ch)-2)
            else:
                decoded_list.append(temp_string)
                temp_string = ""
        return decoded_list