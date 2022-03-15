import json

from django import http
from django.db import transaction
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import FormView
from django.views.generic.detail import BaseDetailView

from order import serializers
from order.choices import OrderStatus
from order.forms import SubmitTicketOrderForm
from order.models import Order
from utils.response import BadRequestJsonResponse
from utils.views import login_required


def ticket_submit(request):
    """"""
    # 0. 验证用户是否已经登录
    # 1. 获取post数据
    # 2. 数据的验证（手机号、门票ID、库存）
    # 3. 关联用户、生成订单号、计算购买总价、生成订单（ORDER)
    # 4. 返回内容：订单ID
    pass


@method_decorator(login_required, name='dispatch')
class TicketOrderSubmitView(FormView):
    """ 3.1 门票订单提交接口 """
    form_class = SubmitTicketOrderForm
    http_method_names = ['post']

    def form_invalid(self, form):
        """ 表单未通过验证 """
        err = json.loads(form.errors.as_json())
        return BadRequestJsonResponse(err)

    def form_valid(self, form):
        obj = form.save(user=self.request.user)
        return http.JsonResponse({
            'sn': obj.sn
        }, status=201)


@method_decorator(login_required, name='dispatch')
class OrderDetail(BaseDetailView):
    slug_field = 'sn'
    slug_url_kwarg = 'sn'

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user, is_valid=True)

    def get(self, request, *args, **kwargs):
        """ GET: 订单详情 """
        order_obj = self.get_object()
        data = serializers.OrderDetailSerializer(order_obj).to_dict()
        return http.JsonResponse(data)

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        """ POST: 订单支付 """
        # 1. 选择支付方式：支付宝、微信
        # 2. 数据验证
        order_obj = self.get_object()
        if order_obj.status == OrderStatus.SUBMIT:
            # 3. 调用真实的支付（暂时省略）
            # 4. 改变订单状态
            order_obj.status = OrderStatus.PAID
            order_obj.save()
            order_obj.order_items.update(status=OrderStatus.PAID)
            return http.HttpResponse('', status=201)
        return http.HttpResponse('', status=200)

    def delete(self, request, *args, **kwargs):
        """ DELETE: 订单删除 """
        return http.JsonResponse({'result': 'delete'})

    def put(self, request, *args, **kwargs):
        """ PUT： 取消订单 """
        return http.JsonResponse({'result': 'put'})
