"""This module defines class SubmitArticle."""
import os
import logging
from django.conf import settings
# from django.core.files.base import ContentFile
from django.views import View
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from article.forms import ArticleForm
from article.models import Article
from image.models import Image


class CreateArticleView(LoginRequiredMixin, View):
    """This class defines methods that handles creating of articles."""
    login_url = '/accounts/login'
    redirect_field_name = 'next'
    template_name = "article/create_article.html"

    def get(self, request):
        """This method renders the page for creating new articles."""
        form = ArticleForm()
        return render(request, self.template_name, {'form': form}, status=200)

    def post(self, request):
        """This method validates articles and saves to the database."""
        # pylint: disable=no-member
        # pylint: disable=broad-exception-caught

        form = ArticleForm(request.POST)

        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['user'] = request.user
            article = Article(**cleaned_data)

            _, image_src_list = cleaned_data.get('content')
            user_img_without_articles = Image.objects.filter(article_id=None, user=request.user)

            thumbnail_url_path = image_src_list[0]

            for unlinked_image in user_img_without_articles:
                unlinked_image_path = str(unlinked_image.file)
                if thumbnail_url_path.endswith(unlinked_image_path):
                    # filename = unlinked_image.file.name.split('/')[-1]

                    # image_copy = ContentFile(content=unlinked_image.file.read(), name=filename)
                    # article.thumbnail.save(filename, image_copy, save=False)
                    article.thumbnail = thumbnail_url_path

                    break

            article.save()

            for unlinked_img in user_img_without_articles:
                for img in image_src_list:
                    unlinked_image_path = str(unlinked_img.file)
                    if img.endswith(unlinked_image_path):
                        unlinked_img.article = article
                        unlinked_img.save()

            if len(image_src_list) != len(user_img_without_articles):
                for unlinked_img in user_img_without_articles:
                    if unlinked_img.article_id is None:
                        rel_path = str(unlinked_img.file)
                        abs_path = os.path.join(settings.MEDIA_ROOT, rel_path)

                        try:
                            unlinked_img.delete()
                            os.remove(abs_path)
                        except FileNotFoundError:
                            logging.error('Image for %s was not found in %s.',
                                        {request.user.username}, {abs_path})
                            unlinked_img.delete()
                            article.delete()
                            messages.error(request, 'Unknown server error.')
                            return render(request, self.template_name, {'form': form})
                        except PermissionError:
                            logging.error('You might not have the required '\
                                        'permission to delete the image.')
                            unlinked_img.delete()
                            article.delete()
                            messages.error(request, 'Unknown server error.')
                            return render(request, self.template_name, {'form': form})
                        except Exception as e:
                            logging.error(str(e))
                            unlinked_img.delete()
                            article.delete()
                            messages.error(request, 'Unknown server error.')
                            return render(request, self.template_name, {'form': form})

            messages.success(request, 'Article was submitted successfully.')
            return redirect(reverse('get-home-page'))

        return render(request, self.template_name, {'form': form}, status=400)
