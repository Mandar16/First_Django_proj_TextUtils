# I created this file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("<h2>Home</h2>")


def analyze(request):
    # Get the text analyze the text.
    djtext = request.POST.get('text', 'default')
    # Checking checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    lst = [removepunc, fullcaps, newlineremover, extraspaceremover]

    # Check which checkbox is on
    if removepunc == "on":
        # removepunc(request, djtext)
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed += char
            else:
                pass
        params = {'purpose': 'remove punctuatuions', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze2.html', params)

    if fullcaps == 'on':
        analyzed = ""
        analyzed = djtext.upper()
        params = {'purpose': 'Capitalized all the characters', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze2.html', params)

    if newlineremover == 'on':
        analyzed = ""
        for i in djtext:
            if i != '\n' and i != '\r':
                analyzed += i

        params = {'purpose': 'New Lines are Removed', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze2.html', params)

    if extraspaceremover == 'on':
        analyzed = ""
        for idx, char in enumerate(djtext):
            if djtext[idx] == ' ' and djtext[idx + 1] == ' ':
                pass
            else:
                analyzed += char
        params = {'purpose': 'New Lines are Removed', 'analyzed_text': analyzed}

    if removepunc != 'on' and extraspaceremover != 'on' and newlineremover != 'on' and fullcaps != 'on':
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)


def about(request):
    return render(request, 'about.html')
