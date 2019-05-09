from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post, Topic
from .forms import PostForm


class PostDetail(View):
    """
    帖子详情
    """
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=int(post_id))
        post.view_count += 1
        post.save()
        reviews = post.get_review_list()
        return render(request, 'posts/detail.html', {
            'post': post,
            'reviews': reviews
        })


class LikePost(LoginRequiredMixin, View):
    """
    点赞帖子
    """
    def post(self, request):
        post_id = request.POST.get('postId', None)
        action = request.POST.get('action', None)
        if request.is_ajax() and post_id and action:
            try:
                post = Post.objects.get(id=int(post_id))
                if action == 'like':
                    post.like_users.add(request.user)
                else:
                    post.like_users.remove(request.user)
                return JsonResponse({'msg': 'ok'})
            except Post.DoesNotExist:
                return JsonResponse({'msg': 'ko'})
        return JsonResponse({'msg': 'ko'})


class AddPost(LoginRequiredMixin, View):
    """
    发布帖子
    """
    def get(self, request):
        form = PostForm()
        return render(request, 'posts/add.html', {'form': form})

    def post(self, request):
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            try:
                new_post = form.save(commit=False)
                new_post.user = request.user
                new_post.save()
                return HttpResponseRedirect(request.user.get_absolute_url())
            except BaseException as e:
                print(e)
        return render(request, 'posts/add.html', {
            'form': form,
            'msg': 'ko'
        })


class TopicDetail(View):
    """
    板块详情
    """
    def get(self, request, topic_id):
        topic = get_object_or_404(Topic, id=int(topic_id))
        posts = topic.topic_posts.order_by('-is_sticky')
        return render(request, 'posts/topic-detail.html', {
            'topic': topic,
            'posts': posts,
            'topic_id': topic.id
        })


class StickyPost(LoginRequiredMixin, View):
    """
    顶置帖子(默认只有管理员可以顶置帖子）
    """
    def post(self, request):
        post_id = request.POST.get('pid', None)
        action = request.POST.get('action', None)

        if request.is_ajax() and post_id and action:
            try:
                post = get_object_or_404(Post, id=int(post_id))
                if action == 'sticky':
                    post.is_sticky = True
                else:
                    post.is_sticky = False
                post.save()
                return JsonResponse({'msg': 'ok'})
            except BaseException as e:
                print(e)
        return JsonResponse({'msg': 'ko'})


class DeletePost(LoginRequiredMixin, View):
    """
    管理员和版主删除帖子
    """
    def post(self, request):
        post_id = request.POST.get('id', None)
        if request.is_ajax() and post_id:
            try:
                post = Post.objects.get(id=int(post_id))
                if request.user.is_staff or request.user == post.topic.user:
                    post.delete()
                    return JsonResponse({'msg': 'ok'})
            except BaseException as e:
                print(e)
        return JsonResponse({'msg': 'ko'})


class TopicBanned(LoginRequiredMixin, View):
    """
    版块禁言
    """
    pass
