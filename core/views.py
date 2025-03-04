from django.shortcuts import render
from core.models import *

def home(request):
    stories = Story.objects.order_by('-id')
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