# https://leetcode.com/problems/longest-string-chain/

class Solution:
    def longestStrChain(self, words) :
        
        
        def lcs (word1, word2):
            dp = [[0]*(len(word1)+1) for i in range (len(word2)+1)]
            
            for i in range (1,len(word2)+1):
                for j in range (1,len(word1)+1):
                    if word2[i-1]==word1[j-1]:
                        dp[i][j] = 1+ dp[i-1][j-1]
                    else:
                        dp[i][j]= max(dp[i-1][j], dp[i][j-1])
                        
            return len(word2)+len(word1)-2*(dp[-1][-1]) ==  1
        
        words.sort(key=len)
        dp = [1]*len(words)
        for end in range (1,len(words)):
            for start in range (end):
                if (len(words[end])-len(words[start])==1 and lcs(words[start], words[end])):
                    
                    dp[end]= max(dp[end], 1+dp[start])

                    
        return max(dp)
    
    
    # Time O(NlogN) for sorting,
    # Time O(NSS) for the for loop, where the second S refers to the string generation and S <= 16.
    # Space O(NS)
    
    # Runtime: 151 ms, faster than 89.30% of Python3 online submissions for Longest String Chain.
    # Memory Usage: 14.4 MB, less than 48.67% of Python3 online submissions for Longest String Chain.
                
    def longestStrChain(self, words) :

        words.sort(key=len)
        dp = {i:1 for i in words}
        for word in words:
            for pointer in range (len(word)):
                predecessor = word[:pointer]+word[pointer+1:]
                if predecessor in dp:
                    dp[word]= max(dp[word], dp[predecessor]+1)
                    
        return max(dp.values())        
            
    
    
print(Solution().longestStrChain(["owstxul","nba","povjfxoxbaq","sbyiewj","cvaxpamwviffnlf","hurvfq","xbgvfmsvrorw","zyyhofznugigk","jdnfohb","szcafkbnttmj","faxvah","kcvrngyustidz","enizybmmlusau","egaxc","jfayxzvpaeh","lklkfrkqaw","rgbtenobrthfh","cmmonv","buldrivxkxbubt","nbtyehq","wwbqoc","ofbq","zthmhfkpvfyshf","kktjoyqxsdpwu","nbpr","hkwdubrxuohagz","ofxbq","tguozjtzrugibs","kcvrngystz","iaflh","zqyi","jndtenfsohbia","bdhemwcqwcb","vhbyb","rgrbtenobrthfh","zenclhawjc","fpzfurrhgyb","kqmlpwwwdeuyj","biyheapfalhpxs","yoqcltwvq","wwmrioktxp","qlrxs","povjfxoxbq","vkxqxodtsrib","xxmp","bgychpbjdxhw","nmspg","wwzbqroxc","vkxqtr","fzkjva","zyozuigk","fgnvvsrclqp","fpzfurhgyb","bgychpbjdxhwr","zuryb","lcc","uvrifrpcyvnrp","rzaptyvv","zgwyrliyofualqa","szcrafkbnttmjh","xzuvnei","vrfpcyv","odkablkghrqdmcm","pqovjsfxoxbaqug","praxaheqdlym","zyofznugigk","njlbtyexhwq","eskishiqcra","xuvei","qtaeiw","rgbtenorhfh","vapmwvifnlf","imggkob","iheapflhxs","zelncflhawjc","vhbyjbvq","kkmc","praxahqdy","mdfyxioesjjasdk","bkchmmckonv","bgychpbjdxjhwr","dkhpklualh","rzaptyvhuv","vhbyjjbviq","tguozjtzrugiubs","wrivjh","dkjhpklualh","kduruogz","kkjyqxsdpwu","fgudksylu","kvrngystz","lpndxwikni","gkbrxwhji","bmeifqleh","xzuyvnei","imggob","wwzbqoc","qfwkdhixdxvahn","oklkgrmcm","zidlopquylimw","zblccsppjfie","kwdubrxuoagz","jjtfzopgekbokixx","qkxdxhn","njlbztwyexxhwq","sw","jyzykstktznr","rusmoswf","jdfh","ub","ibomekyifqleh","kduruog","ewbpsyey","edydt","rsmoswf","kqzmlpwwwdeuyj","iheaflhxs","jjtfzopgekbokxx","vhyb","kdxhn","wwmiokxp","jdfvpzit","xedydt","yeq","rpv","lvd","buldvxxbt","nmspyga","chrpogyvk","wwzbquroxc","ydudfqmuo","zeoavbkptiz","hnvyceidd","jyzykstznr","fzkjyva","lgxkdyaayi","mxhhjdlla","fvpzt","aavrcutqvlfu","hnyd","olkjz","xmetdydtq","vhbyijjbviq","wwmwrioktxp","qtapeikw","zyyhofeznugigk","wjcizltpi","kuruog","zipqyli","xswjyratwzub","nsrusmoswf","suntigywhrpmd","zgkbdrxwbhjsi","vrifrpcyvnrp","etwt","fzutmy","mfyxiojsdk","vovyrlakjpzc","xzuyvonei","suntiyhpmd","jdnfoh","dkhklualh","zthmhfkpvyshf","ofb","njlbtyehwq","ulismvkfs","zelncflhawmjc","zeoavbptz","vuovyrlavkjpzc","lwyygwgmifqwi","qfkxdxvahn","jyzykstzr","orlkjz","gurugs","airztyccghpb","zmhfksf","vapmvfnlf","buldivxkxbubt","tlfa","rv","uzgkbdrzxwbhjsi","buldvxxbubt","yjdkfvpgzadita","ydudafvqmupro","rgbtorhfh","jdenfsohba","untiyhpmd","orlakjz","rzaptyvhuvp","lvld","xnmsjppygia","hnvyceid","kdx","qfwkdhixdkxvahn","vhbyjjbvq","zencflhawjc","wjcizyltkfpi","jfaxzvaeh","pr","guztrugbs","jdf","biyheapfalhlpxs","dfvpzt","bomekifqleh","lklkfrkqaanw","xnmsjppygianbv","uzgkbdrxwbhjsi","nssrusqmoswf","mfyxijsdk","nybraprodr","befqleh","jdkfvpzita","yjdkfevpgzadita","ihkwdubrxuohagz","alnmgu","jfaxzvah","guztzrugbs","lpnwdxwikni","fpzurhgyb","cmmov","mfyxiojjasdk","mdfyxioejjasdk","xnmsjppygianv","gutrugbs","kchmmkonv","ziopquylim","fvpt","xpfufmzy","praxaheqdym","nrusmoswf","jmxhhjdlla","hy","jkfmikmbtx","sbyw","fbvm","lspnwdxwikni","v","cvaxpmwviffnlf","qtapeiw","fpzjfurrhgyb","tfaflfar","sxzclrafkbnttmjh","kktjyqxsdpwu","pfraxaheqdlymp","ba","awavrcutqpvelfu","oefbvqm","enizybmmlsau","wq","oefbvqmm","fzkojyva","kkgmcm","vrifpcyv","xbgvsvrrw","kcvrngyusytidz","ntyehq","lccpp","kdxh","klkgmcm","bkchjmmzckounv","suntiywhpmd","rfpcyv","jdenfohb","mfxijsdk","xpfufmz","ztmhfkpvshf","tfaflfa","oyrlakjz","hnvyed","untyhpm","ruog","nlbtyehwq","pfufmz","xnmsppyga","vhy","alnmwgu","pzurhgyb","hyd","fszsutmy","u","buldvxkxbubt","rfzkgojyva","chsyrlpjoogyvkge","iaflhs","dfvpzit","dkhklalh","lspvnwdxwikni","rcv","hnvyced","hkwdubrxuoagz","cvapmwvifnlf","xnmsjppyga","vhbyjb","k","lqyuvmeofezuno","wvcubd","cub","untyhpmd","chrpjoogyvke","eizbmmlsau","atyv","pqovjfxoxbaqg","chrpjogyvk","pofxxbq","tyhpm","xbgvmsvrrw","lvled","praxaheqdy","u","xxmwp","povjfxxbq","ziopqyli","zfblccsppjfie","uvrifrjpcfyvnrp","ieaflhxs","aiztycghp","kcvrngyupsygtidz","pqovjsfxoxbaqg","jjtzopgekokxx","taflfa","w","xnmspyga","xnmsjppygiav","fgudkwsylu","jkfmikmbrtx","wwzzbquhroxc","zidlopquylim","hnivyvcreidds","rfzkojyva","ydudfqmupo","jgjazb","lklkfrkqaaw","lquvoezuo","okjz","lgxkdyuaayi","xzuvei","zidlopquylimwwu","zeoavbkptz","bpr","odkalkgrqdmcm","pofxbq","rzaptyvuv","jjazb","v","qfkxdxhn","zmhfkvshf","jdkfvpgzaita","jdnfh","vrifpcyvnp","nybprod","xmedydtq","quvoeuo","au","ibomekyifqlseh","bkchjmmckounv","lqyuvmeofezuo","suntiywhrpmd","kz","ztmhfkpvyshf","aifrztyjccghpb","mp","tguozyjtzrugiubs","lccsppf","okalkgrmcm","lgxkddyuaayi","xxm","zaptyv","airztyjccghpb","vkxqxotr","awavrcutqvlfu","zmhfks","eq","kcvrngyustiz","qfkdxdxvahn","uvrifrpcfyvnrp","talfa","oqwstxul","zlioula","bkchmmkonv","zurhyb","jgjazbk","ruo","jndenfsohba","sbw","zidlopquylimwu","qfkdhxdxvahn","lwygwgmifqwi","vpt","jfayxzvaeh","lnmgu","suntigywhzrpmd","aptyv","xpfufmzzy","xxmswp","qfkxdxvhn","kcmmkonv","xbgvmsvrorw","blccsppfe","nyhbvrafprodrf","ok","kfmikmbtx","kxdxhn","vrifpcyvnrp","rv","jndenfsohbia","yhp","ziqyli","oefsbvqmmm","rfcyv","zgwyliyouala","bdhmwcqwcb","njlbtyexxhwq","chrpjogyvke","vh","hnvyd","aiztyccghpb","ydudfqmupro","lwyygwgmiflqwi","njlbztyexxhwq","rgbtnorhfh","buldvxxbbt","szcrafkbnttmj","szcafkbnttm","okz","befqeh","fgnvsrclqp","kkmcm","zaptyvv","chrpgyvk","zilopquylim","hnivyvncreidds","ayv","aifrztyjcjcghpb","eizybmmlsau","hnvycreidds","wwbq","zyoznugigk","smwf","wwmriokxp","qfkdhixdxvahn","chrpgvk","xswjuyratwzubb","iaf","rgbtenorthfh","oqwstxaul","ttfaflfar","jyzyksttznr","szcfkbnttm","znclhawjc","nybvraprodrf","wrivj","tyehq","jdkfvpgzadita","kqlpwwwdeuyj","kwduruogz","smw","lnspvnwdxwikni","gutrugs","tyeq","fzkjv","hnvyceidds","zgkbdrxwhji","lquvmoezuo","ehtwt","bkchmmckounv","tyhp","okalkgrqdmcm","rzplgw","fgudkwsyblu","sbyiw","xswjuyratwzub","szclrafkbnttmjh","hnivycreidds","jfaxvah","ofbvqm","smswf","ydudfvqmupro","jfayhxzvpaeh","huorvfq","sbyiew","lquvmeoezuo","bomeifqleh","pzurhyb","quvoezuo","fgnvvsrcelqp","ttfafalfar","voyrlakjz","quvoeo","fguksylu","egraxca","wwzbqroc","chrlpjoogyvke","beifqleh","vovyrlakjz","vovyrlavkjpzc","nybpr","vrzplgwh","mfyxioejjasdk","zblccsppfie","qlrdxs","biheapfalhxs","blccsppf","zeoavbkpdtiz","oefsbvqmm","nlbtyehq","blccsppfie","egraxc","biheapfalhpxs","e","bomekyifqleh","oklkgmcm","zgwyrliyofuala","fzsutmy","chrgvk","mfyxiojasdk","zgwyliouala","zgkbdrxwbhji","kcvrngyusygtidz","vkxqxotsri","qvoe","qttfafalfar","vrifpcyvn","rvj","kqzmnlpwwwdeuyj","wwbqc","wwq","quvoe","wwzbquhroxc","rzaptzyvhuvp","cmmkonv","jkfmikmbrtax","zmhfkshf","ehtwtm","jdenfsohb","kkqxsdpwu","pfraxaheqdlym","jjab","kwduruoagz","ieaflhs","cvapmwviffnlf","awavrcutqvelfu","lccp","uruog","povfxxbq","ziopquyli","vkxqxtr","mpg","kd","xedydtq","zgwyliyofuala","wjcizltkfpi","iafl","chyrlpjoogyvkge","chrgk","eizbmmlsa","jdkfvpzaita","uwrivjh","guzjtzrugbs","kkqxspwu","zqyli","wjcizltkpi","bgychpbjdxw","fuksylu","jdkfvpzit","vkxqxotsr","zyozugigk","tguzjtzrugibs","kktjoyqxsdpdwu","llkfrkqaw","kzj","zyyofznugigk","nybpro","rsmswf","chyrlpjoogyvke","lvlped","jja","budvxxbt","nybvrafprodrf","povjfxoxbaqg","aztycghp","nybrprod","lv","nmspyg","zyliouala","wrvj","kkyqxsdpwu","vapmwvfnlf","odkalkghrqdmcm","zwyliouala","hkqzmnlpwwwdeuyj","vkxqxotsrib","nybrprodr","lccspp","zylioula","kwdubruoagz","nybvraprodr","nssrusmoswf","ofbvm","xwnmsjppygianbv","aiztycghpb","okalkgrqmcm","vhbyjbv","guzjtzrugibs","gkbdrxwhji","lquvmeofezuo","ekishiqcra","bdhmwcqwb","chrk","jkkfmikmbrtax","utyhpm","rfcv","yooqcltwvq","kcvrngyustz","vkxqqxodtsrib","ztmhfkvshf","vovyrlakjpz","gxmetdydtq","lnshpvnwdxwikni","fukylu","pqovjsifxoxbaqug","biheapflhxs","nmpg","vrzplgw","jjtzopgekbokxx","fpzjfurrhygyb"]))

