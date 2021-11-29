import json

from django import http
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView

from system.forms import SendSmsCodeForm
from system.models import Slider
from utils.response import ServerErrorJsonResponse, BadRequestJsonResponse


def slider_list(request):
    """ 轮播图接口
    {
        "meta": {},
        "objects": []
    }
    """
    data = {
        'meta': {

        },
        'objects': []
    }
    queryset = Slider.objects.filter(is_valid=True)
    for item in queryset:
        data['objects'].append({
            'id': item.id,
            'img_url': item.img.url,
            'target_url': item.target_url,
            'name': item.name
        })
    # return HttpResponse(data)
    return http.JsonResponse(data)


def cache_set(request):
    """ 写缓存 """
    cache.set('username', 'lisi')
    # 5之后自动删除
    cache.set('password', 'password', timeout=5)
    return HttpResponse('ok')


def cache_get(request):
    """ 读缓存 """
    value = cache.get('username')
    return HttpResponse(value)


def send_sms(request):
    pass

    # 1. 拿到手机号，判断是否为真实的手机号码

    # 2. 生成验证码，并存储
    # TODO 3. 调用短信的发送接口
    # 4. 告诉用户验证码发送是否成功（会把验证码直接告诉用户）

    def clean(self):
        """验证是否为手机号码"""
        print(self.cleaned_data)
        phone_num = self.cleaned_data['phone_num']
        pattern = r'^1[0-9]{10}$'
        if not re.search(pattern, phone_num):
            raise forms.ValidationError('手机号%s输入不正确',
                                        code='invalid_phone',
                                        params=(phone_num,))
        return phone_num

    def send_sms_code(self):
        """ 生成验证码并发送短信 """
        sms_code = random.randint(100000, 999999)
        phone_num = self.cleaned_data
        # redis中的key
        key = '{}{}'.format(constants.REGISTER_SMS_CODE_KET, phone_num)
        if 300 > cache.ttl(key) > 240:
            raise Exception('60S之后再试')
        try:
            # TODO 调用发送验证码的短信接口
            # 将验证码存入redis
            timeout = 5 * 60
            cache.set(key, sms_code, timeout=timeout)
            return {
                'phone_num': phone_num,
                'sms_code': sms_code,
                'timeout': timeout
            }
        except Exception as e:
            print(e)
            return None


class SmsCodeView(FormView):
    form_class = SendSmsCodeForm

    def form_valid(self, form):
        """ 表单已经通过验证 """
        data = form.send_sms_code()
        if data is not None:
            return http.JsonResponse(data, status=201)
        return ServerErrorJsonResponse()

    def form_invalid(self, form):
        """ 表单没有通过验证 """
        err_list = json.loads(form.errors.as_json())
        return BadRequestJsonResponse(err_list)
