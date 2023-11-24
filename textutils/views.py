#I have made this file. - Parikshit
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, "../templates/index.html")
    # return HttpResponse("<h1>Home</h1>"
def about(request):
    return HttpResponse("<h1>About</h1>")

def contact(request):
    return render(request, "../templates/contact.html")
def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')

    # checking checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcount = request.GET.get('charcount', 'off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    #check which checkbox is on
    if removepunc == 'on':
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, "../templates/analyze.html", params)

    elif fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Convert to Uppercase', 'analyzed_text': analyzed}
        return render(request, "../templates/analyze.html", params)

    elif newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n':
                analyzed += char

        params = {'purpose': 'Removed new line character', 'analyzed_text': analyzed}
        return render(request, "../templates/analyze.html", params)

    elif extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analyzed += char

        params = {'purpose': 'Removed new line character', 'analyzed_text': analyzed}
        return render(request, "../templates/analyze.html", params)

    elif charcount == 'on':
        analyzed = f"Number of character in tour text is {len(djtext)}"
        params = {'purpose': 'Removed new line character', 'analyzed_text': analyzed}
        return render(request, "../templates/analyze.html", params)

    else:
        return HttpResponse("Error! no options is checked?")


