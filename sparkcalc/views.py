import pandas as pd
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from . import calc
from .calc import TEST_PARAMS


class CalcView(View):
    template_name = "calc.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request):
        form_data = request.POST.copy()
        error_dict = {}
        if "test" in form_data:
            test_slug = form_data["test"]
        else:
            error_dict["test"] = "Je třeba vybrat statistický test."
        if "data_1" in form_data:
            data_1 = form_data["data_1"].replace(",", ".").replace("\r", "").split("\n")
            data_1 = list(filter(lambda x: x.isnumeric(), data_1))
            if len(data_1) > 1:
                data_1 = [float(x) for x in data_1]
                data_1 = pd.Series(data_1)
                data = data_1
            else:
                error_dict["data_1"] = "Je zadáno příliš málo číselných dat."
        test_parameters = {}
        for param in TEST_PARAMS[test_slug]:
            if f"param_{param['id']}" in form_data:
                if param["type"] == "float":
                    test_parameters[param['id']] = float(form_data[f"param_{param['id']}"])
                elif param["type"] in ("str", "alternative"):
                    test_parameters[param['id']] = form_data[f"param_{param['id']}"]
        if len(error_dict) == 0:
            calc_obj = calc.Calc(data, test_slug, test_parameters)
            stat, pvalue, pvalue_plot = calc_obj.perform_test()
            results = {"stat": stat, "pvalue": pvalue, "pvalue_plot": pvalue_plot}
            return render(request, self.template_name, {"results":  results})
        else:
            return render(request, self.template_name)


class TestList(View):
    def get(self, request):
        test_list = [test for test in calc.TEST_LIST]
        get_parameters = request.GET
        if "sample_no" in get_parameters and get_parameters["sample_no"].isdecimal():
            test_list = [test for test in test_list if test["sample_no"] == int(get_parameters["sample_no"])]
        if "measure" in get_parameters:
            test_list = [test for test in test_list if test["measure"] == get_parameters["measure"]]
        response = {"test_list": test_list}
        return JsonResponse(response)


class TestParamList(View):
    def get(self, request, slug):
        if slug in calc.TEST_PARAMS:
            response = calc.TEST_PARAMS[slug]
            response = {"test_parameters": response}
            return JsonResponse(response)
        else:
            return JsonResponse({"test_parameters": {}})
