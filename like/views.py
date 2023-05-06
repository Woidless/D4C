from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import LikeCommentHighway

@login_required
def toggle_like(request):
    # Получаем ID объекта, который пользователь лайкнул
    object_id = request.POST.get('object_id')

    # Проверяем, есть ли уже лайк от этого пользователя
    try:
        like = LikeCommentHighway.objects.get(user=request.user, liked_object_id=object_id)
        like.delete()
        liked = False
    except LikeCommentHighway.DoesNotExist:
        like = LikeCommentHighway.objects.create(user=request.user, liked_object_id=object_id)
        liked = True

    # Возвращаем JSON-ответ
    return JsonResponse({'liked': liked})