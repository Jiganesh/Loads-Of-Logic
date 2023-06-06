# https://leetcode.com/problems/most-popular-video-creator/


from collections import defaultdict
from typing import List

class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        popularity = defaultdict(int)
        views_videos = {}
        for creator, idc, view in zip(creators, ids, views):
            popularity[creator]+=view
            if creator not in views_videos:
                views_videos[creator] = (-view, idc)
            else:
                current_view, current_id = views_videos[creator]
                if -view < current_view:
                    views_videos[creator] = (-view, idc)
                elif -view == current_view:
                    views_videos[creator] = (-view, min(idc, current_id))
        
        maximum = max(popularity.values())
        result = []
        
        for key, value in popularity.items():
            if value == maximum:
                result.append([key, views_videos[key][-1]])
        return result
            