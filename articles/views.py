from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

from django.shortcuts import render
from newsapi import NewsApiClient

from .models import Article
# Create your views here.



class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'


    def ArticleListView(request):
        newsApi = NewsApiClient(api_key='b8345b8ecad948eb840e8cf2b60da147')
        headLines = newsApi.get_top_headlines(sources='vice-news')
        print(headLines)
        articles = headLines['articles']
        description = []
        news = []
        image = []

        for i in range(len(articles)):
            article = article[i]
            description.append(article['description'])
            news.append(article['title'])
            description.append(article['urlToImage'])
        news_list = zip(description, news, image)

        return render(request, 'article_list.html', context={'news_list': news_list})


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body','author')
    # login_url = '/login/'
    # redirect_field_name = 'redirect_to'
    
    # See line 183 of Django source code django/docs/topics/class-based-views/generic-editing.txt: articles is auto set to signed in user
    def from_valid(self,form): 
        form.instance.author = self.request.author
        return super().form_valid(form)