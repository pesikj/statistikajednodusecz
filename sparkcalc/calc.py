from abc import ABC, abstractmethod


class StatisticalTest(ABC):
    @abstractmethod
    def perform_test(self):
        pass

    def __init__(self, data):
        self.data = data


class ZTest(StatisticalTest):
    def perform_test(self):
        pass


TEST_LIST = [
    {
        "name": "z-test",
        "class": ZTest,
        "sample_no": 1,
        "slug": "z-test",
        "measure": "mean_value",
    }
]


class Calc:
    def __init__(self, data):
        self.data = data