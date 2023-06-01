
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Account, Ledger
from .serializers import AccountSerializer
from .permissions import IsOwnerOrNoAccess

from .forms import TransferForm

# class AccountList(generics.ListCreateAPIView):
   
#     queryset = Account.objects.all()
#     serializer_class = AccountSerializer
   
#     def get_queryset(self):
#         queryset = Account.objects.filter(user=self.request.user)
#         return queryset

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Account.objects.all()
#     serializer_class = AccountSerializer


# class LedgerList(generics.ListCreateAPIView):
   
#     queryset = Ledger.objects.all()
#     serializer_class = AccountSerializer
   
#     def get_queryset(self):
#         queryset = Account.objects.filter(user=self.request.user)
#         return queryset

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# @api_view(['POST'])
# def snippet_list(request):

#     if request.method == 'POST':
#         form_data = TransferForm(request.POST)
        
#         # Check if the form data is valid
#         if form_data.is_valid():
#             # If the form is valid, process the data and return an OK response
#             processed_data = process_data(form_data.cleaned_data)
#             response_data = {
#                 'message': 'API request successful',
#                 'data': processed_data
#             }
#             return JsonResponse(response_data, status=200)
#         else:
#             # If the form is not valid, return an error response
#             response_data = {
#                 'message': 'Invalid form data',
#                 'errors': form_data.errors
#             }
#             return JsonResponse(response_data, status=400)

# class Transfer(View):

#     def post(self, request, *args, **kwargs):
#         # Get the form data from the request
#         form_data = TransferForm(request.POST)
        
#         # Check if the form data is valid
#         if form_data.is_valid():
#             # If the form is valid, process the data and return an OK response
#             processed_data = process_data(form_data.cleaned_data)
#             response_data = {
#                 'message': 'API request successful',
#                 'data': processed_data
#             }
#             return JsonResponse(response_data, status=200)
#         else:
#             # If the form is not valid, return an error response
#             response_data = {
#                 'message': 'Invalid form data',
#                 'errors': form_data.errors
#             }
#             return JsonResponse(response_data, status=400)