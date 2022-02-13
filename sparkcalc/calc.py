import base64
import io
from abc import ABC, abstractmethod
from enum import Enum
from typing import Union, Callable, Dict, Tuple

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats
import scipy.stats as stats
from colour import Color
from scipy.stats import norm


class Tail(Enum):
    TWO_TAILED = 1
    LEFT_TAILED = 2
    RIGHT_TAILED = 3


class StatisticalTest(ABC):
    data: pd.Series
    tails: Tail
    alpha: float
    probability_distribution: Callable
    inverse_distribution: Callable
    distribution_params: Dict
    plot_x_minimal_range: Tuple

    @abstractmethod
    def _perform_test(self):
        pass

    def __init__(self, data: Union[pd.Series, pd.DataFrame], test_parameters: dict):
        self.data = data
        self.test_parameters = test_parameters
        if "alternative" in self.test_parameters:
            if self.test_parameters["alternative"] == "lt":
                self.tails = Tail.LEFT_TAILED
            elif self.test_parameters["alternative"] == "gt":
                self.tails = Tail.RIGHT_TAILED
            else:
                self.tails = Tail.TWO_TAILED
        else:
            self.tails = None
        if "alpha" in self.test_parameters:
            self.alpha = float(self.test_parameters["alpha"])
        else:
            self.alpha = None

    def generate_area(self, x1, x2, color, hatch=None, edgecolor=None):
        pt1 = x1
        plt.plot([pt1, pt1], [0.0, self.probability_distribution(pt1, **self.distribution_params)], color='black')

        pt2 = x2
        plt.plot([pt2, pt2], [0.0, self.probability_distribution(pt2, **self.distribution_params)], color='black')

        ptx = np.linspace(pt1, pt2, 10)
        pty = scipy.stats.norm.pdf(ptx)

        if hatch:
            plt.fill_between(ptx, pty, facecolor=color, alpha=1.0, hatch=hatch, edgecolor=edgecolor)
        else:
            plt.fill_between(ptx, pty, color=color, alpha=1.0)

    def create_p_value_plot(self):
        self._perform_test()

        x_min = - abs(self.stat) - 0.5
        if self.plot_x_minimal_range:
            x_min = min(x_min, self.plot_x_minimal_range[0])
        y_max = 0.5

        x_max = x_min * (-1)
        if self.plot_x_minimal_range:
            x_max = max(x_max, self.plot_x_minimal_range[1])
        fig, ax = plt.subplots()

        x = np.linspace(x_min, x_max, 100)
        y = scipy.stats.norm.pdf(x)
        plt.plot(x, y, color='black')

        if self.tails == Tail.TWO_TAILED:
            self.generate_area(abs(self.stat), x_max, 'none', hatch='//////', edgecolor='#5B84B1FF')
            self.generate_area(x_min, -abs(self.stat), 'none', hatch='//////', edgecolor='#5B84B1FF')
        elif self.tails == Tail.LEFT_TAILED:
            self.generate_area(x_min, self.stat, 'none', hatch='//////', edgecolor='#5B84B1FF')
        elif self.tails == Tail.RIGHT_TAILED:
            self.generate_area(self.stat, x_max, 'none', hatch='//////', edgecolor='#5B84B1FF')

        if self.alpha:
            if self.tails == Tail.TWO_TAILED:
                self.generate_area(x_min, self.inverse_distribution(self.alpha / 2), '#FF7F50')
                self.generate_area(self.inverse_distribution(1 - self.alpha / 2), x_max, '#FF7F50')
            elif self.tails == Tail.LEFT_TAILED:
                self.generate_area(x_min, self.inverse_distribution(self.alpha), '#FF7F50')
            elif self.tails == Tail.RIGHT_TAILED:
                self.generate_area(self.inverse_distribution(1 - self.alpha), x_max, '#FF7F50')

        plt.grid()

        plt.xlim(x_min, x_max)
        plt.ylim(0, y_max)

        plt.annotate('Hodnota statistiky', xy=(self.stat, 0), xytext=(self.stat, y_max - 0.05),
                     arrowprops=dict(facecolor='black'), horizontalalignment='center')

        legend_patches = []
        plt.title('p-hodnota', fontsize=10)
        if self.alpha:
            legend_patches.append(mpatches.Patch(color='#FF7F50', label='Kritický obor'.format(self.alpha)))
            legend_patches.append(mpatches.Patch(facecolor='none', hatch='//////', edgecolor='#5B84B1FF',
                                                 label='p-hodnota'))
        plt.legend(handles=legend_patches)
        plt.xlabel('x')

        flike = io.BytesIO()
        fig.savefig(flike)
        b64 = base64.b64encode(flike.getvalue()).decode()
        return b64


class ZTest(StatisticalTest):
    probability_distribution = scipy.stats.norm.pdf
    inverse_distribution = scipy.stats.norm.ppf
    plot_x_minimal_range = (-2, 2)

    def _perform_test(self):
        x_bar = self.data.mean()
        mu = self.test_parameters["mean_value"]
        sigma = self.test_parameters["variance"]
        self.stat = (x_bar - mu) / (sigma / self.data.shape[0])
        if self.tails == Tail.TWO_TAILED:
            self.pvalue = min(stats.norm.cdf(self.stat), 1 - stats.norm.cdf(self.stat)) * 2
        elif self.tails == Tail.LEFT_TAILED:
            self.pvalue = stats.norm.cdf(self.stat)
        else:
            self.pvalue = 1 - stats.norm.cdf(self.stat)

    def perform_test(self) -> (float, float):
        self._perform_test()
        return self.stat, self.pvalue

    def create_critical_region_plot(self, alphas=(0.05,), tails=Tail.TWO_TAILED, x_min=-3, y_max=0.5):
        alphas = sorted(alphas, reverse=True)
        x_max = x_min * (-1)

        red = Color("#FF7F50")
        colors = list(red.range_to(Color("white"), len(alphas) + 1))
        alphas_with_colors = [(alphas[i], colors[-i - 2]) for i in range(0, len(alphas))]

        x = np.linspace(x_min, x_max, 100)
        y = scipy.stats.norm.pdf(x)
        plt.plot(x, y, color='black')

        legend_patches = []
        for alpha, color in alphas_with_colors:
            if tails == Tail.TWO_TAILED:
                ZTest.generate_area(x_min, norm.ppf(alpha / 2), str(color))
                ZTest.generate_area(norm.ppf(1 - alpha / 2), x_max, str(color))
            elif tails == Tail.LEFT_TAILED:
                ZTest.generate_area(x_min, norm.ppf(alpha), str(color))
            elif tails == Tail.RIGHT_TAILED:
                ZTest.generate_area(norm.ppf(1 - alpha), x_max, str(color))
            legend_patches.append(mpatches.Patch(color=str(color), label=r'$\alpha = {:.2f} $'.format(alpha)))

        plt.legend(handles=legend_patches)

        plt.grid()

        plt.xlim(x_min, x_max)
        plt.ylim(0, y_max)

        plt.title('Kritické obory', fontsize=10)
        plt.xlabel('x')

        # plt.savefig("z_test_critical_region.png")
        plt.show()

    def __init__(self, data: Union[pd.Series, pd.DataFrame], test_parameters: dict):
        super().__init__(data, test_parameters)
        self.distribution_params = {"loc": 1, "scale": 0}


class StudentTTest(StatisticalTest):
    probability_distribution = scipy.stats.t.pdf
    inverse_distribution = scipy.stats.t.ppf
    plot_x_minimal_range = (-2, 2)

    def _perform_test(self):
        self.stat, self.pvalue = scipy.stats.ttest_1samp(self.data, self.test_parameters["mean_value"])

    def perform_test(self) -> (float, float):
        self._perform_test()
        return self.stat, self.pvalue

    def create_critical_region_plot(self, alphas=(0.05,), tails=Tail.TWO_TAILED, x_min=-3, y_max=0.5):
        alphas = sorted(alphas, reverse=True)
        x_max = x_min * (-1)

        red = Color("#FF7F50")
        colors = list(red.range_to(Color("white"), len(alphas) + 1))
        alphas_with_colors = [(alphas[i], colors[-i - 2]) for i in range(0, len(alphas))]

        x = np.linspace(x_min, x_max, 100)
        y = scipy.stats.norm.pdf(x)
        plt.plot(x, y, color='black')

        legend_patches = []
        for alpha, color in alphas_with_colors:
            if tails == Tail.TWO_TAILED:
                ZTest.generate_area(x_min, norm.ppf(alpha / 2), str(color))
                ZTest.generate_area(norm.ppf(1 - alpha / 2), x_max, str(color))
            elif tails == Tail.LEFT_TAILED:
                ZTest.generate_area(x_min, norm.ppf(alpha), str(color))
            elif tails == Tail.RIGHT_TAILED:
                ZTest.generate_area(norm.ppf(1 - alpha), x_max, str(color))
            legend_patches.append(mpatches.Patch(color=str(color), label=r'$\alpha = {:.2f} $'.format(alpha)))

        plt.legend(handles=legend_patches)

        plt.grid()

        plt.xlim(x_min, x_max)
        plt.ylim(0, y_max)

        plt.title('Kritické obory', fontsize=10)
        plt.xlabel('x')

        # plt.savefig("z_test_critical_region.png")
        plt.show()

    def __init__(self, data: Union[pd.Series, pd.DataFrame], test_parameters: dict):
        super().__init__(data, test_parameters)
        self.distribution_params = {"df": self.data.shape[0] - 1}


TEST_LIST = [
    {
        "name": "z-test",
        "sample_no": 1,
        "slug": "z-test",
        "measure": "mean_value",
    },
    {
        "name": "t-test",
        "sample_no": 1,
        "slug": "t-test",
        "measure": "mean_value",
    }
]

TEST_CLASSES = {
    "z-test": ZTest,
    "t-test": StudentTTest,
}

TEST_PARAMS = {
    "z-test": [
        {
            "id": "mean_value",
            "type": "float",
            "label": "Hypotetická střední hodnota"
        },
        {
            "id": "variance",
            "type": "float",
            "label": "Rozptyl"
        },
        {
            "id": "alternative",
            "type": "alternative",
            "label": "Typ alternativní hypotézy"
        }
    ],
    "t-test": [
        {
            "id": "mean_value",
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
        stat = round(stat, 5)
        pvalue = round(pvalue, 5)
        return stat, pvalue

    def perform_test(self):
        stat, pvalue = self.test.perform_test()
        stat, pvalue = self._format_results(stat, pvalue)
        pvalue_plot = self.test.create_p_value_plot()
        return stat, pvalue, pvalue_plot

    def _get_test_class(self, test_slug) -> StatisticalTest:
        if test_slug in TEST_CLASSES:
            test_class = TEST_CLASSES[test_slug]
            return test_class

    def __init__(self, data: pd.DataFrame, test_slug: str, test_parameters: dict):
        self.data = data
        test_class: StatisticalTest = self._get_test_class(test_slug)
        self.test = test_class(data, test_parameters)
