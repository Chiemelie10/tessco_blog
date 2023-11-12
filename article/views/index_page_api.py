"""This module defines the class IndexPageApi"""
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.http import JsonResponse
from rest_framework.views import APIView
from article.models import Article
from article.serializers import ArticleModelSerializer
from article.util import paginate_queryset


class IndexPageApi(APIView):
    """This class has a method that returns paginated articles."""
    def get(self, request):
        """
        This method paginates article queryset, returns thep
        aginated data with there current and next page values.
        """
        # pylint: disable=no-member

        page = request.GET.get('page')
        page_size = request.GET.get('page-size')

        if not page and not page_size:
            articles = Article.objects.filter(is_active=True).order_by('-created_at')
            serializer = ArticleModelSerializer(articles, many=True)
            return JsonResponse(serializer.data, status=200, safe=False)

        if page and not page_size:
            return JsonResponse({'error': 'Page size is required.'}, status=400)

        if page_size and not page:
            page = 2

        try:
            page = int(page)
            page_size = int(page_size)
        except ValueError:
            return JsonResponse({'error': 'Value of page or page size must be integer.'},
                                status=400)

        articles = Article.objects.filter(is_active=True).order_by('-created_at')
        result = paginate_queryset(articles, page, page_size)

        if isinstance(result, JsonResponse):
            return result

        paginated_data, total_pages = result
        serializer = ArticleModelSerializer(paginated_data, many=True)

        if page == 1 and page == total_pages:
            previous_page = None
            next_page = None
        elif page == 1 and page < total_pages:
            previous_page = None
            next_page = f"http://{get_current_site(request).domain}"\
                        f"{reverse('get-active-articles-api')}/?page={page + 1}&page-size={page_size}"
        if page > 1 and page < total_pages:
            previous_page = f"http://{get_current_site(request).domain}"\
                            f"{reverse('get-active-articles-api')}/?page={page - 1}"\
                            f"&page-size={page_size}"
            next_page = f"http://{get_current_site(request).domain}"\
                        f"{reverse('get-active-articles-api')}/?page={page + 1}&page-size={page_size}"
        if page > 1 and page == total_pages:
            previous_page = f"http://{get_current_site(request).domain}"\
                            f"{reverse('get-active-articles-api')}/?page={page - 1}"\
                            f"&page-size={page_size}"
            next_page = None

        data = {
            'total_articles': len(articles),
            'total_pages': total_pages,
            'previous_page': previous_page,
            'next_page': next_page,
            'articles': serializer.data
        }
        return JsonResponse(data, status=200, safe=False)
