"""This module contains functions utilised in the app"""
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from bs4 import BeautifulSoup


def paginate_queryset(queryset, page, page_size):
    """
    This function defines the number of adverts to be returned
    per page.
    """
    paginator = Paginator(queryset, per_page=page_size, orphans=0)
    try:
        paginated_data = paginator.page(page)
        total_pages = paginator.num_pages
        return paginated_data, total_pages
    except EmptyPage:
        return JsonResponse({'error': 'Page not found.'}, status=404)
    except PageNotAnInteger:
        return JsonResponse({'error': 'Page number must be an integer.'}, status=400)


def get_image_src(html_field):
    """This method counts the number of "img" tags in tinymce HTMLField."""
    soup = BeautifulSoup(html_field, 'lxml')
    img_tags = soup.find_all('img')

    img_src = []

    for img_tag in img_tags:
        src = img_tag.get('src')
        if src:
            img_src.append(src)

    return img_src
