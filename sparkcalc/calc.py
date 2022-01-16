import base64
import io
from abc import ABC, abstractmethod
from enum import Enum
from typing import Union

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

    @abstractmethod
    def perform_test(self):
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

    def create_p_value_plot(self):
        pass


class ZTest(StatisticalTest):
    def _perform_test(self) -> (float, float):
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

        def generate_area(x1, x2, color):
            pt1 = x1
            plt.plot([pt1, pt1], [0.0, scipy.stats.norm.pdf(pt1)], color='black')

            pt2 = x2
            plt.plot([pt2, pt2], [0.0, scipy.stats.norm.pdf(pt2)], color='black')

            ptx = np.linspace(pt1, pt2, 10)
            pty = scipy.stats.norm.pdf(ptx)

            plt.fill_between(ptx, pty, color=color, alpha='1.0')

        legend_patches = []
        for alpha, color in alphas_with_colors:
            if tails == Tail.TWO_TAILED:
                generate_area(x_min, norm.ppf(alpha / 2), str(color))
                generate_area(norm.ppf(1 - alpha / 2), x_max, str(color))
            elif tails == Tail.LEFT_TAILED:
                generate_area(x_min, norm.ppf(alpha), str(color))
            elif tails == Tail.RIGHT_TAILED:
                generate_area(norm.ppf(1 - alpha), x_max, str(color))
            legend_patches.append(mpatches.Patch(color=str(color), label=r'$\alpha = {:.2f} $'.format(alpha)))

        plt.legend(handles=legend_patches)

        plt.grid()

        plt.xlim(x_min, x_max)
        plt.ylim(0, y_max)

        plt.title('Kritické obory pro z-test', fontsize=10)
        plt.xlabel('x')

        plt.savefig("z_test_critical_region.png")
        plt.show()

    def create_p_value_plot(self):
        self._perform_test()

        x_min = - abs(self.stat) - 0.5
        y_max = 0.5

        x_max = x_min * (-1)
        fig, ax = plt.subplots()

        x = np.linspace(x_min, x_max, 100)
        y = scipy.stats.norm.pdf(x)
        plt.plot(x, y, color='black')

        def generate_area(x1, x2, color, hatch=None, edgecolor=None):
            pt1 = x1
            plt.plot([pt1, pt1], [0.0, scipy.stats.norm.pdf(pt1)], color='black')

            pt2 = x2
            plt.plot([pt2, pt2], [0.0, scipy.stats.norm.pdf(pt2)], color='black')

            ptx = np.linspace(pt1, pt2, 100)
            pty = scipy.stats.norm.pdf(ptx)

            plt.fill_between(ptx, pty, facecolor=color, alpha=1.0, hatch=hatch, edgecolor=edgecolor)

        if self.tails == Tail.TWO_TAILED:
            generate_area(abs(self.stat), x_max, 'none', hatch='//////', edgecolor='#5B84B1FF')
            generate_area(x_min, -abs(self.stat), 'none', hatch='//////', edgecolor='#5B84B1FF')
        elif self.tails == Tail.LEFT_TAILED:
            generate_area(x_min, self.stat, 'none', hatch='//////', edgecolor='#5B84B1FF')
        elif self.tails == Tail.RIGHT_TAILED:
            generate_area(self.stat, x_max, 'none', hatch='//////', edgecolor='#5B84B1FF')

        if self.alpha:
            if self.tails == Tail.TWO_TAILED:
                generate_area(x_min, norm.ppf(self.alpha / 2), '#FF7F50')
                generate_area(norm.ppf(1 - self.alpha / 2), x_max, '#FF7F50')
            elif self.tails == Tail.LEFT_TAILED:
                generate_area(x_min, norm.ppf(self.alpha), '#FF7F50')
            elif self.tails == Tail.RIGHT_TAILED:
                generate_area(norm.ppf(1 - self.alpha), x_max, '#FF7F50')

        plt.grid()

        plt.xlim(x_min, x_max)
        plt.ylim(0, y_max)

        plt.annotate('Hodnota statistiky', xy=(self.stat, 0), xytext=(self.stat, y_max - 0.05),
                     arrowprops=dict(facecolor='black'), horizontalalignment='center')

        legend_patches = []
        plt.title('p-hodnota z-testu', fontsize=10)
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

    def __init__(self, data: Union[pd.Series, pd.DataFrame], test_parameters: dict):
        super().__init__(data, test_parameters)


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
