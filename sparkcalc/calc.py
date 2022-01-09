from abc import ABC, abstractmethod
from typing import Union

import pandas as pd
from statsmodels.stats import weightstats
import scipy.stats as stats


class StatisticalTest(ABC):
    data: pd.Series

    @abstractmethod
    def perform_test(self):
        pass

    def __init__(self, data: Union[pd.Series, pd.DataFrame], hypothesis_params: dict, alternative: str = "neq"):
        self.data = data
        self.alternative = alternative
        self.hypothesis_params = hypothesis_params
        self.alternative = alternative


class ZTest(StatisticalTest):
    def perform_test(self) -> (float, float):
        x_bar = self.data.mean()
        if "mu" in self.hypothesis_params:
            mu = self.hypothesis_params["mu"]
        if "sigma" in self.hypothesis_params:
            sigma = self.hypothesis_params["sigma"]
        stat = (x_bar - mu) / (sigma / self.data.shape[0])
        if self.alternative == "lt":
            pvalue = min(stats.norm.cdf(stat), 1 - stats.norm.cdf(stat)) * 2
        elif self.alternative == "<":
            pvalue = stats.norm.cdf(stat)
        else:
            pvalue = 1 - stats.norm.cdf(stat)
        return stat, pvalue


TEST_LIST = [
    {
        "name": "z-test",
        "sample_no": 1,
        "slug": "z-test",
        "measure": "mean_value",
    }
]

TEST_CLASSES = {
    "z-test": ZTest,
}

TEST_PARAMS = {
    "z-test": [
        {
            "id": "mu",
            "type": "float",
            "label": "Hypotetická střední hodnota"
        },
        {
            "id": "alternative",
            "type": "alternative",
            "label": "Typ alternativní hypotézy"
        }
    ]
}


class Calc:
    test: StatisticalTest

    @staticmethod
    def _format_results(stat, pvalue):
        stat = round(stat, 3)
        pvalue = round(pvalue, 5)
        return stat, pvalue

    def perform_test(self):
        stat, pvalue = self.test.perform_test()
        stat, pvalue = self._format_results(stat, pvalue)
        return stat, pvalue

    def _get_test_class(self, test_slug) -> StatisticalTest:
        if test_slug in TEST_CLASSES:
            test_class = TEST_CLASSES[test_slug](self.data)
            return test_class

    def __init__(self, data: pd.DataFrame, test_slug: str):
        self.data = data
        self.test = self._get_test_class(test_slug)
