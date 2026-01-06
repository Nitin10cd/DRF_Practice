from django.http import JsonResponse
import json

# first view
def api_home(request, *args, **kwargs):
    #various data handling in the djnago as we do in express
    # for the json we can use request.body
    body = request.body #assuming it is json type of data not json but type of byte string json
    # we can use the json package to get the actual json data to the py dictionary
    data = {}
    try:
        # loads in exact json formate 
        data = json.loads(body)
    except:
        pass
    print(data)
    return JsonResponse({"message": "Hi there this is your django api response"})