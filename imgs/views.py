# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Image, Comment
from .forms import ImageUploadForm, CommentForm
from django.contrib import messages
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
@login_required
def  img_list(req):
	images = Image.objects.all()
	return render(req, 'imgs/list.html',{'images': images})

@login_required
def image_upload(request):
	if request.method == "POST":
		form = ImageUploadForm(request.POST, request.FILES)
		if form.is_valid():
			new_item = form.save(commit=False)
			# assign current user to the item
			new_item.user = request.user
			new_item.save()
			# create_action(request.user, 'uploaded image', new_item)
			messages.success(request, 'Image uploaded successfully')
			# redirect to new created item detail view
			return redirect(new_item.get_absolute_url())
	else:
		form = ImageUploadForm()

	return render(request, 'imgs/upload.html', {'section': 'upload', 'form': form})	

def image_detail(request, id, slug):
	image = get_object_or_404(Image, id=id, slug=slug)
	print id
	initial_data = {
		'content_type': image.get_content_type,
		'object_id': image.id
	}
	form = CommentForm(request.POST or None, initial=initial_data)
	if form.is_valid():
		c_type = form.cleaned_data.get('content_type')
		content_types = ContentType.objects.filter(model=c_type)
		if content_types:
			content_type = content_types[0]
		obj_id = form.cleaned_data.get('object_id')
		content_data = form.cleaned_data.get('content')
		new_comment, created = Comment.objects.get_or_create(
								user=request.user,
								content_type=content_type,
								object_id=obj_id,
								content=content_data)
	comments = Comment.objects.filter(object_id = id)
	return render(request, 'imgs/detail.html', {'section': 'images', 'image': image, 'comments': comments,
														'comment_form': form})

@login_required
@require_POST
def image_like(request):
	print 'like'
	image_id = request.POST.get('id')
	action = request.POST.get('action')
	if image_id and action:
		try:
			image = Image.objects.get(id=image_id)
			if action == 'like':
				image.users_like.add(request.user)
				# create_action(request.user, 'likes', image)
			else:
				image.users_like.remove(request.user)
			return JsonResponse({'status': 'ok'})
		except:
			pass
	return JsonResponse({'status': 'ko'})	