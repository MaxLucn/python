from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


# 复合类型
# ContentType---类容模型
# ForeignKey(ContentType)---关联复合模型
# GenericForeignKey---关联模型
# GenericRelation---反向关联
class Sight(models.Model):
    """ 景点表 """
    name = models.CharField('景点名称', max_length=64)
    address = models.CharField('景点地址', max_length=64)


class Order(models.Model):
    """ 订单表 """
    sn = models.CharField('订单号', max_length=64)
    amount = models.FloatField('订单金额')
    # 知道订单，查询相关订单评论
    comment = GenericRelation('Comment', related_query_name='order_comments')


class SightComment(models.Model):
    """ 景点评论 """
    content = models.CharField('评论内容', max_length=512)
    score = models.FloatField('评分', default=5)


class OrderComment(models.Model):
    """ 订单评论 """
    content = models.CharField('评论内容', max_length=512)
    score = models.FloatField('评分', default=5)


# class Comment(models.Model):
#     """ 景点、订单评论 """
#     sight = models.ForeignKey(Sight, null=True)
#     order = models.ForeignKey(Order)
#     content = models.CharField('评论内容', max_length=512)
#     score = models.FloatField('评分', default=5)

class Comment(models.Model):
    """ 景点、订单评论（复合类型实现） """
    # 外间关联，关联到内容模型
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # 把关联到的模型 ID 存起来
    object_id = models.PositiveIntegerField()
    # 通过评论的记录找到对应的对象
    content_object = GenericForeignKey('content_type', 'object_id')
    content = models.CharField('评论内容', max_length=512)
    score = models.FloatField('评分', default=5)