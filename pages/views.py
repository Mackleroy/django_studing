from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View


class PageView(View):
    def get(self, request):
        return HttpResponse('Hi')
