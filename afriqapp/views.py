from django.shortcuts import render
from .models import Members
from django . views . generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.
#def index(request):
    #profiles = Members.objects.all()
    #return render(request, 'afriqapp/index.html', {'profiles':profiles})
class MemberListview(ListView):
    model = Members
    template_name = 'afriqapp/index.html'
    context_object_name = 'profiles'
    odering = ['name']
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Members.objects.filter(name__icontains=query)
        else:
            return  Members.objects.all()

class MembersCreateView(CreateView):
        model = Members
        fields = '__all__'
class MembersUpdateView(UpdateView):
    model = Members
    fields = '__all__'
class MembersDeleteView(DeleteView):
    model = Members
    success_url = '/'


