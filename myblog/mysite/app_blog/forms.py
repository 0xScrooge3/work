# -*- coding: utf-8 -*-
from django import forms
from multiupload.fields import MultiFileField
from .models import ArticleImage

class ArticleImageForm(forms.ModelForm):
    images = MultiFileField(min_num=1, max_num=10, max_file_size=1024*1024*5)  # налаштуйте параметри на свій розсуд

    class Meta:
        model = ArticleImage
        fields = '__all__'
        exclude = ['image']  # виключіть поле image з Meta

    def save(self, commit=True):
        instances = super(ArticleImageForm, self).save(commit=False)
        for image in self.cleaned_data['images']:
            ArticleImage.objects.create(article=instances.article, image=image)
        return instances
