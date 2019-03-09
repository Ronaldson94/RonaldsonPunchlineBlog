from django.shortcuts import render,get_object_or_404,redirect
from .models import Punchline,Comment
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .forms import CommentForm
# Create your views here.

def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        context ={'query':q}
        template = 'punchline/result.html'

    else:
        template = 'punchline/punchline_list.html'
        context ={}
    return render(request,template,context)

    pass

def add_comment_to_punchline(request, pk):
    punchline = get_object_or_404(Punchline, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.puncline = punchline
            comment.save()
            return redirect('punchline_detail', pk=punchline.pk)
    else:
        form = CommentForm()
    return render(request, 'punchline/add_comment_to_post.html', {'form': form})

class PostListView(ListView):
    model = Punchline
    template_name = 'punchline/punchline_list.html'
    context_object_name = 'punchlines'
    ordering = ['-date_poste']
    paginate_by = 10

class PunchlineDetailView(DetailView):
    model = Punchline
