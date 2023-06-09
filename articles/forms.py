from django import forms
from .models import Article

class ArticleForms(forms.ModelForm):
    class Meta:
        model=Article
        fields = ['title','content']
    
    def clean(self):
        data = self.cleaned_data
        print('all data',data)
        title=data.get('title')
        content=data.get('content')
        qs = Article.objects.all().filter(title__icontains=title)
        qc=Article.objects.all().filter(content__icontains=content)
        if qs.exists():
            self.add_error('title',f'{title} is already in use.')
        if qc.exists():
            self.add_error('content',f'{content} is already in use.')
        return data

class ArticleFormos(forms.Form):
    title=forms.CharField()
    content=forms.CharField()

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data
    #     print(cleaned_data)
    #     title=cleaned_data.get('title')
    #     if title.lower().strip() == "the office":
    #         raise forms.ValidationError('This title is taken.')
    #     print(title)
    #     return title
    
    def clean(self):
        cleaned_data = self.cleaned_data
        print('all data',cleaned_data)
        title=cleaned_data.get('title')
        content=cleaned_data.get('content')
        if title.lower().strip() == "the office":
            self.add_error('title','This title is taken.')
        if "office" in content or "office" in title.lower():
            self.add_error('content','Office cannot be in content')  
        return cleaned_data
    