from django.views import View
from .models import Client
from django.http import JsonResponse
from django.forms import model_to_dict

class ClientListView(View):
    def get(self, request):
        if('name' in request.GET):
            c_list = Client.objects.filter(name__contains=request.GET['name'])
        else:
            c_list = Client.objects.all()

        return JsonResponse(list(c_list.values()), safe=False)

class ClientDetailView(View):
    def get(self, request, pk):
        client = Client.objects.get(pk=pk)

        return JsonResponse(model_to_dict(client))
