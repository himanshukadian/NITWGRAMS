from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import F, Q
from django.core.mail import send_mail,BadHeaderError
from django.views import generic
from django.contrib.auth.decorators import login_required

from users_auth.models import CustomUser
from .models import Complain
from .forms import PostForm
from reportlab.pdfgen import canvas
from io import BytesIO
from django.contrib import messages

class IndexView(generic.ListView):
    model = Complain
    template_name = 'comportal/home.html'


class AdminView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    model = Complain
    template_name = 'comportal/complain_list.html'
    context_object_name = 'complain_list'
    ordering= ['-pub_date']
    paginate_by = 3
    def get_queryset(self):
        return Complain.objects.filter(category=self.request.user.admin)

    def test_func(self):
        admin = str(self.request.user.admin)
        if admin == 'N':
            return False
            messages.error(self.request, f'You are not admin')
        return True

class UnprocessedView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    model = Complain
    template_name = 'comportal/complain_list.html'
    context_object_name = 'complain_list'
    ordering= ['-pub_date']
    paginate_by = 3
    def get_queryset(self):
        return Complain.objects.filter(category=self.request.user.admin,status=0)

    def test_func(self):
        admin = str(self.request.user.admin)
        if admin == 'N':
            return False
            messages.error(self.request, f'You are not admin')
        return True

class RecentView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    model = Complain
    template_name = 'comportal/complain_list.html'
    context_object_name = 'complain_list'
    ordering= ['-pub_date']
    paginate_by = 3
    def get_queryset(self):
        return Complain.objects.filter(category=self.request.user.admin,status=0).order_by('-pub_date')[:5]

    def test_func(self):
        admin = str(self.request.user.admin)
        if admin == 'N':
            return False
            messages.error(self.request, f'You are not admin')
        return True
class LastView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    model = Complain
    template_name = 'comportal/complain_list.html'
    context_object_name = 'complain_list'
    ordering= ['-pub_date']
    paginate_by = 3
    def get_queryset(self):
        return Complain.objects.filter(category=self.request.user.admin,status=0).order_by('pub_date')[:5]

    def test_func(self):
        admin = str(self.request.user.admin)
        if admin == 'N':
            return False
            messages.error(self.request, f'You are not admin')
        return True
class ProcessingView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    model = Complain
    template_name = 'comportal/complain_list.html'
    context_object_name = 'complain_list'
    ordering= ['-pub_date']
    paginate_by = 3
    def get_queryset(self):
        return Complain.objects.filter(status=1).order_by('-pub_date')

    def test_func(self):
        admin = str(self.request.user.admin)
        if admin == 'N':
            return False
            messages.error(self.request, f'You are not admin')
        return True
class ResolvedView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    model = Complain
    template_name = 'comportal/complain_list.html'
    context_object_name = 'complain_list'
    ordering= ['-pub_date']
    paginate_by = 3
    def get_queryset(self):
        return Complain.objects.filter(status=2).order_by('-pub_date')

    def test_func(self):
        admin = str(self.request.user.admin)
        if admin == 'N':
            return False
            messages.error(self.request, f'You are not admin')
        return True
class PriorityView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    model = Complain
    template_name = 'comportal/complain_list.html'
    context_object_name = 'complain_list'
    ordering= ['-pub_date']
    paginate_by = 3
    def get_queryset(self):
        return Complain.objects.filter(category=self.request.user.admin).order_by('priority')

    def test_func(self):
        admin = str(self.request.user.admin)
        if admin == 'N':
            return False
            messages.error(self.request, f'You are not admin')
        return True

class UserComplains(generic.ListView):
    model = Complain
    template_name = 'users_auth/complains.html'
    context_object_name = 'complain_list'
    paginate_by = 3
    def get_queryset(self):
        if(self.request.user.admin!='N'):
            user = get_object_or_404(CustomUser, username=self.kwargs.get('username'))
            return Complain.objects.filter(by=user).order_by('-pub_date')
        else:
            return  Complain.objects.filter(by=self.request.user).order_by('-pub_date')

class DetailView(generic.DetailView):
    model = Complain


class CreateComplain(LoginRequiredMixin, CreateView):
    model = Complain
    fields = ['title', 'category', 'pimage', 'description']
    def form_valid(self, form):
        user = self.request.user
        form.instance.by = user
        to_user = self.request.user.email
        from_user = 'himanshu25101998@gmail.com'
        send_mail('new Complain','Hey there you have new complain lodged',from_user,[to_user],fail_silently=False)
        try:
            send_mail('new Complain', 'Hey there you have new complain lodged', to_user,[from_user],fail_silently=False)
        except BadHeaderError:
            HttpResponse('Inavalid')
        messages.success(self.request, f'Your complaint has been lodged')

        return super(CreateComplain, self).form_valid(form)

class UpdateComplain(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Complain
    fields = ['title', 'category','pimage','description']
    def form_valid(self, form):
        form.instance.by = self.request.user
        messages.success(self.request, f'The Complain has been updated')
        return super().form_valid(form)

    def test_func(self):
        complain = self.get_object()
        user = self.request.user
        print(complain.by)
        if user == complain.by:
            return True
        messages.error(self.request, f'you are not allowed to update complain')
        return False

class DeleteComplain(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Complain
    success_url = reverse_lazy('comportal:index')

    def test_func(self):
        complain = self.get_object()
        user = (self.request.user)
        if user == complain.by:
            return True
        messages.error(self.request, f'you are not allowed to delete the complain')
        return False


class LodgedComplain(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    model = Complain
    paginate_by = 3
    def get_queryset(self):
        return Complain.objects.filter(category=self.request.user.admin).order_by('-pub_date')

    def test_func(self):
        if self.request.user.admin is not 'N':
            return True
        messages.error(self.request, f'you are not the admin')
        return False


@login_required
def process(request, pk):
    complain = get_object_or_404(Complain, id=pk)
    if complain.category == request.user.admin:
        complain.status = 1

        complain.by.notifications= complain.by.notifications+1
        messages.info(request, f'Actions are taken on the NITWGRAMS')
        complain.by.noti_messages = complain.by.noti_messages+'<li> Admin has started the action on your complain titled <a href="'+reverse('comportal:detail', kwargs={'pk': pk})+'">'+str(complain.title)+'</a>'
        complain.save()
        complain.by.save()
        return HttpResponseRedirect(reverse('comportal:detail', kwargs={'pk': pk}))
    else:
        return HttpResponse('<h1> 403 Forbidden</h1>')

@login_required
def done(request, pk):
    complain = get_object_or_404(Complain, id=pk)
    if complain.category == request.user.admin:
        complain.status = 2
        complain.by.notifications= complain.by.notifications+1
        messages.success(request, f'the complain has been resolved')
        complain.by.noti_messages = complain.by.noti_messages+'<li>Your Complain titled <a href="'+reverse('comportal:detail', kwargs={'pk': pk})+'">'+str(complain.title)+'</a> has been resolved'
        complain.save()
        complain.by.save()
        messages.success(request, f'the NITWGRAMS has been resolved')
        return HttpResponseRedirect(reverse('comportal:detail', kwargs={'pk': pk}))
    else:
        return HttpResponse('<h1> 403 Forbidden</h1>')

@login_required
def detailViewNew(request, pk):
    complain = get_object_or_404(Complain, id=pk)
    print(request.user.admin)
    if request.user == complain.by or request.user.admin == complain.category:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit = False)
                post.complain = complain
                post.by = request.user
                post.save()
                request.user.notifications =request.user.notifications+1
                request.user.noti_messages =  request.user.noti_messages+'<li>You have some unread discussions in <a href="'+reverse('comportal:detail', kwargs={'pk': pk})+'">'+str(complain.title)+'</a>'
                request.user.save()
                return HttpResponseRedirect(reverse('comportal:detail', kwargs={'pk': pk}))
        else:
            form = PostForm()
        key = str(pk)+str(request.user.id)
        value = True
        if key in request.COOKIES:
            value = False
        allow = False
        if str(request.user) == str(complain.by) or request.user.admin == complain.category:
            allow = True
        print(allow)
        return render(request, 'comportal/add_post.html', {'form':form,'complain':complain, 'priority':value, 'discuss':allow})
    return HttpResponse('<h1> 403 Forbidden</h1>')
@login_required
def prioritize(request, pk):
    complain = get_object_or_404(Complain, id=pk)
    key = str(pk)+str(request.user.id)
    if complain.by == str(request.user):
        print(complain.by)
    else:
        if key not in request.COOKIES:
            complain.priority = F('priority')+1
            messages.success(request, f'the NITWGRAMS is prioritized')
            complain.save()

    response = HttpResponseRedirect(reverse('comportal:detail', kwargs={'pk': pk}))
    response.set_cookie(key, 'TRUE')
    return response

@login_required
def statusupdate(request, pk):
    complain = get_object_or_404(Complain, id=pk)
    if complain.category == str(request.user.admin):
        complain.status = F('status')+1
        # messages.success(request, f'the status has been updated')
        complain.save()
    return HttpResponseRedirect(reverse('comportal:detail', kwargs={'pk': pk}))


def pdf(request,pk):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'
    complain = get_object_or_404(Complain, id=pk)
    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    # Start writing the PDF here
    p.setFont("Helvetica-Bold", 48)
    p.drawCentredString(300,750,"COMPLAINT")
    p.setFont("Helvetica", 24)
    p.drawCentredString(300,700,"Title : "+complain.title)
    p.setFontSize(18)
    p.drawCentredString(300,650,"By : "+complain.by.username)
    p.setFontSize(18)
    p.drawCentredString(300,600,"Date : "+(complain.pub_date.strftime(' %d, %b %Y') ))
    p.setFontSize(20)
    p.drawCentredString(100,550,"Description : ")
    p.setFontSize(20)
    textobject = p.beginText()
    textobject.setTextOrigin(100, 525)
    textobject.setFont("Helvetica-Oblique", 14)
    text = complain.description

    i=0
    while i <len(text):
        line = ''
        j = 65
        while j>0 and i<len(text):
            line=line+text[i]
            j = j-1
            i=i+1
        textobject.textLine(line)


    p.drawText(textobject)
    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response

