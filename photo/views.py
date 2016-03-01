# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse

def single_photo(request, photo_id):
    return HttpResponse('{0}번 사진을 보여드릴게요.'.format(photo_id))
