"""This module defines class CreateArticleForm and SubmitArticleForm"""
from django import forms
from django.utils.translation import get_language
from article.models import Article
from tinymce.widgets import TinyMCE
from article.util import get_image_src


class CreateArticleForm(forms.ModelForm):
    """This class defines fields of the model to be rendered."""
    # content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}, mce_attrs={'height': 200, 'width': 200}))
    class Meta:
        """
            model: Name of the model
            fields: Fields of the model to be rendered.
        """
        model = Article
        fields = ["title", "content", "category"]
        widgets = {'content': TinyMCE(
            attrs={'cols': 80, 'rows': 30},
            mce_attrs={'height': '60%',
                       # 'language': get_language(),
                       # 'spellchecker_languages': get_language(),
            }
        )}
    class Media:
        """
        This class lists media files used by the form.
        """
        js = ['image_upload_handler.js']


class SubmitArticleForm(forms.ModelForm):
    """This class defines fields of the model to be validated."""

    def clean_content(self):
        """
        This method raises ValidationError if images in the content field
        is zero or greater than three.
        """
        content = self.cleaned_data.get('content')
        img_src_list = get_image_src(content)

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
