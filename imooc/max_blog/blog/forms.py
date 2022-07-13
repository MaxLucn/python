from django import forms
from .models import Blog, BlogCategory

# 把已经有的分类展示在添加博客页面的分类选项中
# choices = [('测试分类', '测试分类'), ('python', 'python'), ('赛车', '赛车'), ('音乐', '音乐'), ('足球', '足球')]
choices = BlogCategory.objects.all().values_list('name', 'name')

# 新建一个列表，通过循环把所有新建的分类添加进列表中，为了所有分类都能正常显示
choices_list = []

for item in choices:
    choices_list.append(item)


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        # fields = ('id', 'title', 'title_tag', 'content', 'author', 'category_id')
        fields = ('title', 'title_tag', 'content', 'author', 'category')

        widgets = {
            # 'id': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices_list, attrs={'class': 'form-control'}),
        }
