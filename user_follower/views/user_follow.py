"""This module defines class UserFollowView."""
import json
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from user_follower.models import UserFollow
from app_user.models import User


class UserFollowView(LoginRequiredMixin, View):
    """
    This class defines a post method that handles
    user follow or unfollow syatem.
    """
    login_url = '/accounts/login'
    redirect_field_name = 'next'

    def post(self, request):
        """This method handles request to follow or unfollow a user."""
        # pylint: disable=no-member

        try:
            data = json.loads(request.body.decode('utf-8'))

            following = data.get('following')

            author_id = following.split(' ')
            author = User.objects.get(id=author_id[0])

            user_following, created = UserFollow.objects.get_or_create(follower=request.user,
                                                                        following=author)
            if created:
                return JsonResponse({'message': 'Following created successfully.',
                                     'new_state': 'Unfollow'
                                    }, status=200)
            else:
                user_following.delete()
                return JsonResponse({'message': 'Following deleted successfully.',
                                     'new_state': 'Follow'
                                    }, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except KeyError:
            return JsonResponse({'error': 'Key error'}, status=400)
