from django.shortcuts import render
from django.http import HttpResponse
from blog.models import PostForms

def postform(request):
    if request.method == 'POST':
        title_p = request.POST.get('title')
        name_p = request.POST.get('name')
        lt = request.POST.get('ls')
        gq = request.POST.get('question')
        presentation_p = request.POST.get('presentation')
        background_p = request.POST.get('background')
        pt = request.POST.get('perfTask')
        quiz_p = request.POST.get('quiz')
        vocab_p = request.POST.get('vocab')
        wiki_p = request.POST.get('wiki')

        p = PostForms(title=title_p, name=name_p, ls=lt, question=gq, presentation=presentation_p,
        background=background_p, perfTask=pt, quiz=quiz_p, vocab=vocab_p, wiki=wiki_p)
        p.save()

        return(render(request, 'blog/postform.html'))
    else:
        return(render(request, 'blog/postform.html'))
