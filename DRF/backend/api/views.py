from django.http import JsonResponse
import json
from django.forms.models import model_to_dict

# importing the product model
from products.models import Product

# first view
def api_home(request, *args, **kwargs):
    # #various data handling in the djnago as we do in express
    # # for the json we can use request.body
    # body = request.body #assuming it is json type of data not json but type of byte string json
    # # we can use the json package to get the actual json data to the py dictionary
    # data = {}
    # try:
    #     # loads in exact json formate 
    #     data = json.loads(body)
    # except:
    #     pass
    # print(data)
    # return JsonResponse({"message": "Hi there this is your django api response"})
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data: 
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price

        # we can do this simply by model_to_dict method from django forms
        data = model_to_dict(model_data, fields=['id','title','content','price'])

    return JsonResponse(data)