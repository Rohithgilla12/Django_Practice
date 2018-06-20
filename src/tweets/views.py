from django import forms
from django.forms.utils import ErrorList
from django.shortcuts import render,get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from .mixins import UserOwnerMixin
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
# Create your views here.


# Create

class TweetCreateView(FormUserNeededMixin,CreateView):
    # queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = "tweets/create_view.html"
    # success_url = reverse_lazy("tweet:detail") #"/tweet/"
    login_url = '/admin'
    # fields = ['user', 'content']

    # def form_valid(self, form):
    #     if self.request.user.is_authenticated:
    #         form.instance.user = self.request.user
    #         return super(TweetCreateView,self).form_valid(form)
    #     else:
    #         form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["Please Login to continue !"])
    #         return self.form_invalid(form)


# def tweet_create_view(request):
#     form = TweetModelForm(request.POST or None)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.user = request.user
#         instance.save()
#     context ={
#         "form":form
#     }
#     return render(request, 'tweets/create_view.html', context)

# Retrieve
class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()

    # def get_object(self):
    #     print(self.kwargs)
    #     pk = self.kwargs.get("pk")
    #     obj = get_object_or_404(Tweet, pk=pk)
    #     print(pk)
    #     return Tweet.objects.get(id=pk)


class TweetListView(ListView):
    def get_queryset(self, *args, **kwargs):
        queryset = Tweet.objects.all()
        print(self.request.GET)
        query = self.request.GET.get("q",None)
        if query is not None:
            queryset = queryset.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        # context["Another"] = Tweet.objects.all() Way fo adding context
        return context


# def tweet_detail_view(request, id=1):
#     obj = Tweet.objects.get(id=id)  # GET from database
#     print(obj)
#     context = {
#         "object": obj
#     }
#     return render(request, "tweets/detail_view.html", context)
#
#
# def tweet_list_view(request):
#     queryset = Tweet.objects.all()
#     for obj in queryset:
#         print(obj.content)
#     context = {
#         "object_list": queryset
#     }
#     return render(request, "tweets/list_view.html", context)
# Update
class TweetUpdateView(UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = "tweets/update_view.html"
    # success_url = "/tweet/"
# Delete


class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    success_url = reverse_lazy("tweet:list")
    template_name = "tweets/delete_confirm.html"
