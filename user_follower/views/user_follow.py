"""This module defines class UserFollowView."""
import json
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.sites.shortcuts import get_current_site
from user_follower.models import UserFollow
from app_user.models import User


class UserFollowView(APIView):
    """
    This class defines a post method that handles
    user follow or unfollow syatem.
    """
    def post(self, request):
        """This method handles request to follow or unfollow a user."""
        # pylint: disable=no-member

        try:
            # data = json.loads(request.body.decode('utf-8'))
            data = request.data

            if not request.user.is_authenticated:
                redirect_return_path = data.get('pathname')
                current_site = get_current_site(request)

                if str(current_site) == 'http://127.0.0.1:8000':
                    current_site = 'http://localhost:8000'

                login_url = f"{current_site}{reverse('account_login')}"\
                            f"?next={redirect_return_path}"

                return redirect(login_url)

            following = data.get('following')

            if following is None:
                return Response({'error': 'following is required.'},
                                status=status.HTTP_400_BAD_REQUEST)

            author_id = following.split(' ')
            author = User.objects.get(id=author_id[0])

            user_following, created = UserFollow.objects.get_or_create(follower=request.user,
                                                                        following=author)
            if created:
                return Response({'message': 'Following created successfully.',
                                 'new_state': 'Unfollow'}, status=status.HTTP_200_OK)
            else:
                user_following.delete()
                return Response({'message': 'Following deleted successfully.',
                                     'new_state': 'Follow'
                                    }, status=status.HTTP_200_OK)
        except json.JSONDecodeError:
            return Response({'error': 'Invalid JSON'}, status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response({'error': 'Key error'}, status=status.HTTP_400_BAD_REQUEST)
