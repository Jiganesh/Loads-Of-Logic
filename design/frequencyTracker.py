# https://leetcode.com/problems/frequency-tracker/

class FrequencyTracker:

    def __init__(self):
        self.number_frequency = defaultdict(int)
        self.frequency_tracker = defaultdict(int)
        

    def add(self, number: int) -> None:
        current_frequency = self.number_frequency[number]
        new_frequency = current_frequency +1
        self.number_frequency[number] = new_frequency
        self.frequency_tracker[current_frequency]-=1
        self.frequency_tracker[new_frequency]+=1

    def deleteOne(self, number: int) -> None:
        if self.number_frequency[number]:
            current_frequency = self.number_frequency[number]
            new_frequency = current_frequency - 1
            self.number_frequency[number] = new_frequency
            self.frequency_tracker[current_frequency]-=1
            self.frequency_tracker[new_frequency]+=1
        
        

    def hasFrequency(self, frequency: int) -> bool:
        return self.frequency_tracker[frequency]


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)