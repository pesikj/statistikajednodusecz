from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

from . import calc


class CalcView(TemplateView):
    template_name = "calc.html"


class TestList(View):
    def get(self, request):
        response = [{"name": test["name"]} for test in calc.TEST_LIST]
        response = {"test_list": response}
        return JsonResponse(response)
