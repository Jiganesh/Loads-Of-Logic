# https://leetcode.com/problems/number-of-music-playlists/

class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:


        MOD = 10**9+7

        dp = {}

        def solve(current_song, used_songs):

            # if goal is completed and all songs are played at least once
            if current_song == goal:
                return used_songs == n
            
            # DP 
            if (current_song, used_songs) in dp:
                return dp[(current_song, used_songs)]

            # Number of ways a used song can be played
            usedsongways = solve(current_song+1, used_songs) * max(0, used_songs-k)

            # Number of ways a new song can be played
            newsongways = solve(current_song +1, used_songs+1) * (n - used_songs)


            ans = (usedsongways + newsongways) % MOD
            dp[(current_song, used_songs)] = ans
            return ans


        return solve(0, 0)
        