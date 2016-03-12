# coding: utf-8

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Photo

def single_photo(request, photo_id, hidden=False):
    """
    Try Catch 문도 쓸 수 있음
    try:
        photo = Photo.objects.get(pk=photo_id)
    except Photo.DoesNotExist:
        return HttpResponse("No Photo")
    """
    if hidden is True:
        # todo: 뭔가 은밀한 작업을 합시다.
        pass
    photo = get_object_or_404(Photo, pk=photo_id)

    response_text = '<p>{photo_id}번 사진</p>'
    response_text += '<p><image src="{photo_url}"/></p>'

    return HttpResponse(response_text.format(
        photo_id=photo_id,
        photo_url=photo.image_file.url
        )
    )

