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
        input_data = {}
        param_data = {}
        if "test" in form_data:
            test_slug = form_data["test"]
            input_data["test"] = form_data["test"]
        else:
            error_dict["test"] = "Je třeba vybrat statistický test."
        data_set_keys = filter(lambda x: "data_" in x, form_data.keys())
        for key in data_set_keys:
            input_data[key] = form_data[key]
            data = form_data[key].replace(",", ".").replace("\r", "").split("\n")
            data = list(filter(lambda x: x.isdecimal(), data))
            if len(data) > 1:
                data = [float(x) for x in data]
                data = pd.Series(data)
                data = data
            else:
                error_dict[key] = "Je zadáno příliš málo číselných dat."
        test_parameters = {}
        for param in TEST_PARAMS[test_slug]:
            data_key = f"param_{param['id']}"
            if data_key in form_data:
                param_data[data_key] = form_data[data_key]
                if param["type"] == "float":
                    if not form_data[data_key].isnumeric():
                        error_dict[data_key] = "Parametr musí být číslo"
                    else:
                        test_parameters[param['id']] = float(form_data[data_key])
                elif param["type"] in ("str", "alternative"):
                    test_parameters[param['id']] = form_data[data_key]
        if len(error_dict) == 0:
            calc_obj = calc.Calc(data, test_slug, test_parameters)
            stat, pvalue, pvalue_plot = calc_obj.perform_test()
            results = {"stat": stat, "pvalue": pvalue, "pvalue_plot": pvalue_plot}
            return render(request, self.template_name, {"results":  results, "input_data": input_data,
                                                        "param_data": param_data})
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
