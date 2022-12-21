# from django.template import loader
from django.forms import modelformset_factory
from django.forms.formsets import ORDERING_FIELD_NAME
from django.shortcuts import render, redirect
# from django.http import JsonResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.dates import ArchiveIndexView
from django.urls import reverse_lazy, reverse
from django.core import serializers
from django.core.paginator import Paginator


from .forms import BbForm
from .models import Bb, Rubric


def index(request):

    rubrics = Rubric.objects.all() 
    bbs = Bb.objects.all() 
    paginator = Paginator(bbs, 2) 
    if 'page' in request.GET:
        page_num = request.GET['page'] 
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {'rubrics': rubrics, 'page': page, 'bbs': page.object_list} 
    return render(request, 'bboard/index.html', context)

    # template = loader.get_template('bboard/index.html')
    # bbs = Bb.objects.order_by('-published')
    # context = {'bbs': bbs}
    # return HttpResponse(template.render(context, request))


# def index(request):
#     s = 'Список объявлений\r\n\r\n\r\n'
#     for bb in Bb.objects.order_by('-published'):
#         s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
#     return HttpResponse(s, content_type='text/plain; charset=utf-8')


def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    # rubric_serialized = serializers.serialize("python", rubrics.values(), ensure_ascii=False)
    # return JsonResponse(list(rubrics), safe=False)
    # return JsonResponse(rubric_serialized, safe=False)

    # json_object = {'key': "value"}
    # return JsonResponse(json_object)

    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)


def rubrics(request):
    RubricFormSet = modelformset_factory(Rubric, fields=('name',),
                                        can_order=True, can_delete=True)
    if request.method == 'POST':
        formset = RubricFormSet(request.POST) 
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    rubric = form.save(coramit=False)
                    rubric.order = form.cleaned_data[ORDERING_FIELD_NAME] 
                    rubric.save()
                    return redirect('bboard:index')
    else:
        formset = RubricFormSet()
        context = {'formset': formset}
        return render(request, 'bboard/rubrics.html', context)


class BbCreateView(CreateView):
    template_name = 'bboard/create.html/'
    form_class = BbForm
    success_url = reverse_lazy('index')

# чтобы рубрики отображались на странице ввода
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class BbDetailView(DetailView):
    model = Bb
    # template_name = 'bboard/bb_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class BbEditView(UpdateView): 
    model = Bb
    form_class = BbForm 
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs) 
        context['rubrics'] = Rubric.objects.all()
        return context


class BbDeleteView(DeleteView): 
    model = Bb
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs) 
        context['rubrics'] = Rubric.objects.all ()
        return context


class BbIndexView(ArchiveIndexView): 
    model = Bb
    date_field = 'published'
    date_list_period = 'day'
    template_name = 'bboard/index.html' 
    context_object_name = 'bbs' 
    allow_empty = True

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs) 
        context['rubrics'] = Rubric.objects.all()
        return context