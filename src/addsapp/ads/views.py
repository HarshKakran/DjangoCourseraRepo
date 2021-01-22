#imports
from .owner import OwnerListView, OwnerCreateView, OwnerDeleteView,OwnerDetailView,OwnerUpdateView
from .models import Ad
from django.views import View
from django.shortcuts import render

# Create your views here.
class AdListView(OwnerListView):
    model = Ad
    def get_context_data(self, *args, **kwargs):
        context = super(AdListView,
             self).get_context_data(*args, **kwargs)
        # add extra field
        context["ads"] = Ad.objects.all()
        return context

class AdDetailView(OwnerDetailView):
    template_name = 'ads/ad_detail.html'
    model = Ad


class AdCreateView(OwnerCreateView):
    model = Ad
    fields = ['title', 'price','text']

class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'price', 'text']

class AdDeleteView(OwnerDeleteView):
    model = Ad
    template_name = 'ads/ad_confirm_delete.html'