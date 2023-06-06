from typing import List

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        
        
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.8 + 32.00
        
        return [round(kelvin, 5), round(fahrenheit, 5)]
