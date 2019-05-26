from .models import Item
import uuid
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist
import numpy as np
from PIL import Image, ImageDraw
from django.http import FileResponse

# 1
@require_http_methods(['POST'])
def create(request):
    item = Item.objects.create(id=uuid.uuid4())
    return JsonResponse({'msg' : 'OK' , 'id' : item.id})

# 2
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

# 3
@require_http_methods(['GET'])
def information(request, id):
    try:
        item = Item.objects.get(id=id)
    except ObjectDoesNotExist:
        return JsonResponse({'message' : 'not found'})
    info = {}
    info['id'] = item.id
    info['created'] = item.created
    if item.image_vector:  # true - exist, false - null
        info['hasVector'] = 'yes'
    else:
        info['hasVector'] = 'no'
    return JsonResponse(info)

# 4
@require_http_methods(['GET'])
def show(request):
        items_list = list(Item.objects.values_list('id', flat=True))
        return JsonResponse({'ids' : items_list} , safe=False)


# 5
@require_http_methods(['GET'])
def download_image(request, id):
    try:
        item = Item.objects.get(id=id)
    except ObjectDoesNotExist:
        return JsonResponse({'message' : 'Item not found'})
    if item.image_vector:
        array = np.reshape(item.image_vector, (-1, item.image_width)) * 255 # get original array
        image = Image.fromarray(array).convert('RGB')
        image.save('image.jpeg')
        return FileResponse(open('image.jpeg', 'rb'))
    else:
        image = Image.new("1", (200, 200))
        image.save('image.jpeg')
        return FileResponse(open('image.jpeg', 'rb'))


# 6
@require_http_methods(['DELETE'])
def remove(request, id):
    try:
        item = Item.objects.get(id=id)
    except ObjectDoesNotExist:
        return JsonResponse({'message' : 'Item not found'})
    item.delete()
    return JsonResponse({'message' : 'OK'})
