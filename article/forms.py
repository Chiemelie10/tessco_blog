"""This module defines class CreateArticleForm and SubmitArticleForm"""
from django import forms
# from django.utils.translation import get_language
from tinymce.widgets import TinyMCE
from article.util import get_image_src
from article.models import Article


class ArticleForm(forms.ModelForm):
    """This class defines fields of the model to be validated."""
    def __init__(self, *args, **kwargs):
        """
        This constructor method runs when a form object is created to do
        some configuration settings.
        """
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select the article's category"
        self.fields['title'].widget.attrs['placeholder'] = "Enter the article's title"

    def clean_content(self):
        """
        This method raises ValidationError if:
            1) images in the content field is zero or greater than three.
            2) Number of words is less than 150.
            3) If file path + name exceeds 200 characters also set in the Article model.
        """
        content = self.cleaned_data.get('content')
        img_src_list, num_of_words = get_image_src(content)

        # Ensure the value of len(img_src_list[0] matches value of
        # max length set in article models.py file)
        if len(img_src_list) > 0 and len(img_src_list[0]) > 200:
            raise forms.ValidationError('File name is too long.')

        if num_of_words < 10:
            raise forms.ValidationError('Number of words must be at least 150.')

        if len(img_src_list) <= 0:
            raise forms.ValidationError('Please enter a thumbnail for the article')

        if len(img_src_list) > 3:
            num_to_remove = len(img_src_list) - 3
            if num_to_remove == 1:
                raise forms.ValidationError(f'Please remove {num_to_remove} image, '\
                                             'only a maximum of 3 is accepted.')

            raise forms.ValidationError(f'Please remove {num_to_remove} images, '\
                                         'only a maximum of 3 is accepted.')
        return content, img_src_list

    class Meta:
        """
            model: Name of the model.
            fields: fields of the model to be validated.
        """
        model = Article
        fields = ["title", "content", "category"]
        widgets = {'content': TinyMCE(
            # attrs={'cols': 80, 'rows': 30},
            mce_attrs={'height': '100%',
                       'width': '100%',
                    #    'language': get_language(),
                    #    'spellchecker_languages': get_language(),
                    #    'content_css': ['static/article/css/create_article_content_field.css'],
            }
        )}
