from django.urls import path

from order import views

urlpatterns = [
    # 3.1 订单提交接口
    path('ticket/submit/', views.TicketOrderSubmitView.as_view(), name="ticket_submit"),
]