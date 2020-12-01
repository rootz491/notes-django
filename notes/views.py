from django.shortcuts import render, reverse, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
# from django.template import loader
from .models import note
from uuid import uuid4 as uuid

# Create your views here.


def index(request):
        notes = note.objects.all()
        context = {'notes': notes}
        template_name = 'notes/view.html'
        return render(request, template_name, context=context)
        # template = loader.get_template('notes/view.html')
        # return HttpResponse(template.render(context, request))



def search(request):
        template_name = 'notes/search.html'

        if request.method == 'GET':
                return render(request, template_name)

        elif request.method == 'POST':
                query = request.POST['search']
                notes = note.objects.filter(title=query)
                print(notes)
                if notes:
                        context = {
                                'notes': notes
                        }
                        return render(request, template_name, context=context)
                else:
                        context = {
                                'error_message': 'Note not available'
                        }
                        return render(request, template_name, context=context)



def logout(request):
        pass




def bookmarked(request):
        notes = note.objects.filter(is_bookmarked=True)
        context = {'notes': notes}
        template_name = 'notes/bookmarked.html'
        return render(request, template_name, context=context)




def bookmark(request, id):
        thatNote = get_object_or_404(note, pk=id)
        # bookmark the note
        print(thatNote.title)
        thatNote.is_bookmarked = not thatNote.is_bookmarked
        thatNote.save()
        return HttpResponseRedirect(reverse('note:index'))




def create(request):
        template_name = 'notes/create.html'

        if request.method == 'GET':
                return render(request, template_name)

        if request.method == 'POST':
                newNote = note()
                newNote.title = request.POST['title']
                newNote.content = request.POST['content']
                newNote.id = key()
                newNote.save()

                print(newNote.title)
                print(newNote.content)

                return HttpResponseRedirect(reverse('note:index'))





def delete(request, id):
        thatNote = get_object_or_404(note, pk=id)
        thatNote.delete()
        return HttpResponseRedirect(reverse('note:index'))





# generate random primary key
def key():
        return uuid().hex