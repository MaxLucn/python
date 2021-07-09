from django import template

register = template.Library()


@register.filter()
def f_name(value):
    """ 自定义过滤器：格式化用户名称 """
    return '{}***'.format(value[0])


# # 方式一：注册过滤器
# register.filter('f_name', f_name)
