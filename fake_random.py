import random
from typing import Any, List

class FakeRandom():
    data: List
    weight: List[int]

    end_weight: List[int]
    diff_weight: List[int]
    fake_times: int

    times = 0

    def __init__(self, data: List, weight: List[int], fake_times: int) -> None:

        if len(data) != len(weight):
            raise Exception('data and weight must be same length')

        self.data = data
        self.weight = weight
        self.fake_times = fake_times

        sum_weight = sum(weight)
        self.end_weight = [2*sum_weight - i for i in self.weight]
        self.diff_weight = [(self.end_weight[i] - self.weight[i])/fake_times for i in range(len(self.weight))]
    
    def _weight_plus(self) -> None:
        if self.times <= self.fake_times:
            self.weight = [self.weight[i] + self.diff_weight[i] for i in range(len(self.weight))]
        else:
            self.weight = [1 for _ in range(len(self.weight))]
        self.times += 1
    
    def _get_int(self, number: float) -> int:
        if number%1==0:
            return int(number)
        else:
            return int(number) + self.times%2
    
    def get(self) -> Any:
        data = []
        for i in range(len(self.data)):
            for _ in range(self._get_int(self.weight[i])):
                data.append(self.data[i])
        self._weight_plus()
        return random.choice(data)
    
    def gets(self, n: int) -> List:
        data = []
        for _ in range(n):
            data.append(self.get())
        return data