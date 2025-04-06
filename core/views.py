from django.shortcuts import render
from core.models import *

def home(request):
    stories = Story.objects.order_by('-id')[:4]
    recent_story = stories.first()
    categories = Category.objects.all()
    holiday_stories = Story.objects.filter(category__title='Holiday')
    context = {
        'stories': stories,
        'recent_story': recent_story,
        'categories': categories,
        'holiday_stories': holiday_stories,
    }
    return render(request, 'index.html', context=context)


def story_detail(request, id):
    story = Story.objects.get(id=id)
    categories = Category.objects.all()
    recent_stories = Story.objects.order_by('-id')[:3]
    tag = Tag.objects.all()
    context = {
        'data': story,
        'categories': categories,
        'recent_stories': recent_stories,
        'tags':tag
    }
    return render(request, 'single.html', context=context)


def stories(request):
    stories = Story.objects.all()
    categories = Category.objects.all()
    context = {
        'stories': stories,
        'categories': categories,
    }
    return render(request, 'stories.html', context=context)
