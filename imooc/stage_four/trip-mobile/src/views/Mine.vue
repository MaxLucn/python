<template>
  <!-- 个人中心 -->
  <div class="page-mine">
    <!-- 标题 -->
    <van-nav-bar title="个人中心" fixed/>
    <!-- 用户基本信息：头像、昵称 -->
    <div class="user-header">
      <div class="avatar">
        <img src="/static/mine/avatar.png"/>
      </div>
      <div>
        <p>欢迎您，张三</p>
        <a class="btn-link" href="#">退出登录</a>
      </div>
    </div>
    <!-- 订单的菜单列表 -->
    <van-row class="user-links">
      <van-col span="6">
        <router-link to="/">
          <van-icon name="records"/>
          <span>全部订单</span>
        </router-link>
      </van-col>
      <van-col span="6">
        <router-link to="/">
          <van-icon name="pending-payment"/>
          <span>待支付</span>
        </router-link>
      </van-col>
      <van-col span="6">
        <router-link to="/">
          <van-icon name="tosend"/>
          <span>已完成</span>
        </router-link>
      </van-col>
      <van-col span="6">
        <router-link to="/">
          <van-icon name="logistics"/>
          <span>已取消</span>
        </router-link>
      </van-col>
    </van-row>
    <!-- 底部导航 -->
    <TripFooter/>
  </div>
</template>
<script>
import TripFooter from '@/components/common/Footer'

export default {
  components: {
    TripFooter
  }
}
</script>
<style lang="less">
.page-mine {
  .van-nav-bar--fixed {
    background-color: transparent;
  }

  .van-nav-bar__title {
    color: #fff;
  }

  .user-header {
    background: url(/static/mine/bg.jpg) no-repeat center;
    background-size: 100% auto;
    color: #fff;
    height: 200px;
    display: flex;
    flex-direction: column;
    justify-content: center;

    .avatar img {
      width: 80px;
      height: 80px;
    }
  }

  .user-links {
    padding: 15px 0;
    font-size: 12px;
    text-align: center;
    background-color: #fff;

    .van-icon {
      display: block;
      font-size: 24px;
    }
  }

  .btn-link {
    color: #fff;
  }
}
</style>
