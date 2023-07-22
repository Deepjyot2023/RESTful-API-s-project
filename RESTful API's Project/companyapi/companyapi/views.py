
from django.http import HttpResponse, JsonResponse

# # 1. function based views
# # 2. class based views

# #----------------------------------------------------


# # 1. function-based views;


def home_page(request):
    print("Home Page requested...!")
    friends = [
        'Ankit',
        'Manoj',
        'Kamlesh'
    ]
    # return HttpResponse("<h1>This is HomePage...!</h1>")
    return JsonResponse(friends, safe=False)


























