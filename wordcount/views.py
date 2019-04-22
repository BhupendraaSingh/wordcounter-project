
from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def brand(request):
    return render(request, 'brand.html', {'people':'folks'})

def about(request):
    return render(request, 'about.html')

def hi(request):
    return HttpResponse('<h2>Hi I am word counter</h2>')

def count(request):
    full_text = request.GET['fulltext']
    allchar_len = len(full_text)
    special_char_list =   [' ', '!', '#', '$', '%', '&', "'", '(', ')', '*',
    '+', ',','--', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@',
    '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

    words_dict = {}
    spec_char = 0

    if len(full_text) == 0:
        message = 'You have entered nothing.'
    else:
        message = 'Great you have entered something.'

    # Counting words
    for word in full_text.split():
        if word in special_char_list:
            spec_char += 1
        else:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1

    # getting spec_char form words like people,
    for word in words_dict:
        for c in word:
            if c in special_char_list:
                spec_char += 1


    sorted_list = sorted(words_dict.items(), key=operator.itemgetter(1),
        reverse = True)

    return render(request, 'count.html',
        {'fulltext': full_text, 'how_many_words' : len(full_text.split()),
        'words_dict': sorted_list, 'message': message,
        'full_len': allchar_len,
        'spec_char': spec_char
        })
