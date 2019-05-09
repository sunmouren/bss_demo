from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, View

from .models import Resource
from .forms import ResourceForm


class ResourceList(ListView):
    """
    资源文件列表
    """
    model = Resource
    template_name = 'resources/list.html'


class UploadResource(LoginRequiredMixin, View):
    """
    上传文件
    """
    def get(self, request):
        form = ResourceForm()
        return render(request, 'resources/upload.html', {'form': form})

    def post(self, request):
        form = ResourceForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            try:
                new_resource = form.save(commit=False)
                new_resource.user = request.user
                new_resource.save()
                return HttpResponseRedirect(reverse('resources:resource-list'))
            except BaseException as e:
                print(e)
        return render(request, 'resources/upload.html', {
            'form': form,
            'msg': 'ko'
        })


class AddDownloadCount(LoginRequiredMixin, View):
    """
    增加文件下载次数
    """
    def post(self, request):
        rid = request.POST.get('rid', None)
        if request.is_ajax() and rid:
            try:
                resource = Resource.objects.get(id=int(rid))
                resource.download_count += 1
                resource.save()
                return JsonResponse({'msg': 'ok'})
            except BaseException as e:
                print(e)
        return JsonResponse({'msg': 'ko'})
