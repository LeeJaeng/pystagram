# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse

def single_photo(request):
    return HttpResponse('3번 사진')
