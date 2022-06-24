from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Post, Comment
from .forms import CommentForm

# Create your views here.
def post_detail(request, category_slug, post_slug):
  post = get_object_or_404(Post, slug=post_slug)
  #comment = get_object_or_404(Comment, id=comment_id)
  
  if request.method == 'POST':
    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
      comment = comment_form.save(commit=False)
      comment.post = post
      comment.save()
      
      return redirect('post_detail', category_slug=post.category.slug, post_slug=post.slug)
  
  else:
    comment_form = CommentForm()
  
  comments = Comment.objects.all()
  
  return render(request, 'blog/post_detail.html', {'post': post, 'comment_form': comment_form, 'comments': comments})
  
  
def category_detail(request, category_slug):
  category = get_object_or_404(Category, slug=category_slug)
  return render(request, 'blog/category_detail.html', {'category': category})