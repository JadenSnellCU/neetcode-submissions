class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ss = len(s)
        st= len(t)
        if ss < st:
            return ""
        else:
            count = {}
            s_dict = {}
            left = 0
            min_arr = []
            have = 0
            min_len = float("inf")
            min_left = 0
            min_right = 0
            window = []
            for i in range(st):
                count[t[i]] = count.get(t[i],0)+1
            need = len(count)
            for right in range(len(s)):
                s_dict[s[right]] = s_dict.get(s[right],0)+1
                if s[right] in count and s_dict[s[right]] == count[s[right]]:
                    have +=1
                while have == need:
                    current_len = right - left + 1

                    if current_len < min_len:
                        min_len = current_len
                        min_left = left
                        min_right = right
                    if s[left] in count and s_dict[s[left]] == count[s[left]]:
                        have -= 1
                    s_dict[s[left]] -= 1
                    left += 1
        if min_len == float("inf"):
            return ""
        return s[min_left:min_right+1]
                

                
        