import uuid

import numpy as np
from PIL import Image, ImageDraw

from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed, FileResponse
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist

from .models import Item


#  Create item
@require_http_methods(['POST'])
def create(request):
    item = Item.objects.create(id=uuid.uuid4())
    return JsonResponse(
        {
            'msg' : 'OK',
            'id' : item.id,
        }
    )


#  Add image vector to existin item
@require_http_methods(['POST'])
def add_vector(request, id):
    try:
        item = Item.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponse('Error', content_type="text/plain")
    image = Image.open(request.FILES['file']).convert('L')
    image_array = np.asarray(image, dtype='float') / 255
    array_width = list(image_array.shape)
    item.image_width = array_width[1]
    item.image_vector = list(np.reshape(image_array, -1))
    item.save()
    return HttpResponse('Success', content_type="text/plain")


#  Get more item info
@require_http_methods(['GET'])
def information(request, id):
    try:
        item = Item.objects.get(id=id)
    except ObjectDoesNotExist:
        return JsonResponse(
            {
                'message' : 'not found',
            }
        )
    info = {}
    info['id'] = item.id
    info['created'] = item.created
    #  true - exist, false - null
    if item.image_vector:
        info['hasVector'] = 'yes'
    else:
        info['hasVector'] = 'no'
    return JsonResponse(info)


#  Show all existin items
@require_http_methods(['GET'])
def show(request):
    items_list = list(Item.objects.values_list('id', flat=True))
    return JsonResponse(
        {
            'ids' : items_list,
        }
    )


#  Download item image
@require_http_methods(['GET'])
def download_image(request, id):
    try:
        item = Item.objects.get(id=id)
    except ObjectDoesNotExist:
        return JsonResponse(
            {
                'message' : 'Item not found',
            }
        )
    if item.image_vector:
        #  get original array
        array = np.reshape(item.image_vector, (-1, item.image_width)) * 255
        image = Image.fromarray(array).convert('RGB')
        image.save('image.jpeg')
        return FileResponse(open('image.jpeg', 'rb'))
    else:
        image = Image.new("1", (200, 200))
        image.save('image.jpeg')
        return FileResponse(open('image.jpeg', 'rb'))


#  Delete item
@require_http_methods(['DELETE'])
def remove(request, id):
    try:
        item = Item.objects.get(id=id)
    except ObjectDoesNotExist:
        return JsonResponse(
            {
                'message' : 'Item not found',
            }
        )
    item.delete()
    return JsonResponse(
        {
            'message' : 'OK',
        }
    )
