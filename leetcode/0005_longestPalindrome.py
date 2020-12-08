class Solution:
    def longestPalindrome(self, s: str) -> str:
        ret = ''
        for i in range(len(s)):
            ret = self.getPalindrome(ret, i, s)
            #print(i, ret)
        #print(len(ret))
        return ret

    def getPalindrome(self, ret, i, s):
        if i < int((len(ret) + 1) / 2):
            return ret
        left = i - 1
        right = i + 1
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            left -= 1
            right += 1
        if (right - 1 - left) > len(ret):
            ret = s[left + 1:right]
        left = i
        right = i + 1
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            left -= 1
            right += 1
        if (right - 1 - left) > len(ret):
            ret = s[left + 1:right]
        return ret

st = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
so = Solution()
print(so.longestPalindrome('yfikrcvmuegdciuqahlsjesplljlswxaejgdzhubzqkiroxyhtjvazcwcnsvdzjiainmiyobyfclyugttaswlntwukkfbebcdaxdpaxwqenkxxphxdcgrnpruoaetvunwyskswvvmjmltncsdukwzlpfodhgxkjvzppwpvmqlfbojgbdiryleskemhjfoxxzjqihcykpgzhaugwwbqtddjzpmrgdncgzsttqenmbnnavfjkiennwxtguywoaiuungqpyfcffzmljfianapawiayywuvazrnxouvndzqbmmyntkkdyykgodjbeojtpnsyhfrltuazgznddaaibupephvgrcjpzvjttmhtnydwvrpgijselaukwrcosxpcbptebalkheymuyblffahvbszotmutmmqhlgoskuoejvavlprvgyozpylsnqhqrnqpabgbwzwxyibpmsauxcfnbtwwbosksuzqzmobijytxxtyjibomzqzusksobwwtbnfcxuasmpbiyxwzwbgbapqnrqhqnslypzoygvrplvavjeouksoglhqmmtumtozsbvhafflbyumyehklabetpbcpxsocrwkualesjigprvwdynthmttjvzpjcrgvhpepubiaaddnzgzautlrfhysnptjoebjdogkyydkktnymmbqzdnvuoxnrzavuwyyaiwapanaifjlmzffcfypqgnuuiaowyugtxwnneikjfvannbmneqttszgcndgrmpzjddtqbwwguahzgpkychiqjzxxofjhmekselyridbgjobflqmvpwppzvjkxghdofplzwkudscntlmjmvvwsksywnuvteaourpnrgcdxhpxxkneqwxapdxadcbebfkkuwtnlwsattguylcfyboyimniaijzdvsncwczavjthyxorikqzbuhzdgjeaxwsljllpsejslhaquicdgeumvcrkify'))