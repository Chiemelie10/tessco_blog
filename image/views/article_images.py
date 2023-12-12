"""This module defines class ImageUploadView."""
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.sites.shortcuts import get_current_site
from image.models import Image
from image.serializers import ImageModelSerializer


class ImageUploadView(APIView):
    """This class defines a post method that handles image upload to the server."""

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, FileUploadParser]


    def post(self, request):
        """This method saves an image in the 'media' directory on the server."""
        # pylint: disable=no-member
        serializer = ImageModelSerializer(data=request.data)

        if serializer.is_valid():
            validated_data = serializer.validated_data
            validated_data['user'] = request.user

            image = Image(**validated_data)
            image.save()

            serializer = ImageModelSerializer(image)
            path = serializer.data.get('file')
            current_domain = get_current_site(request)
            url = f'{current_domain}{path}'
            print(url)

            return Response({'location': url }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
