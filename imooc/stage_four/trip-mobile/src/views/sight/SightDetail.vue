<template>
  <!-- 景点详情 -->
  <div class="page-sight-detail">
    <!-- 页面头部 -->
    <van-nav-bar
    left-text="返回"
    left-arrow
    fixed
    @click-left="goBack"
  />
    <!-- // 页面头部 -->

    <!-- 景点大图 -->
    <div class="sight-banner">
      <van-image src="/static/home/hot/h1_max.jpg" width="100%" height="100%"/>
      <div class="tips">
        <router-link class="pic-sts" :to="{name: 'SightImage', params: {id: 123}}">
          <van-icon name="video-o"/>
          <span>10 张图片</span>
        </router-link>
        <div class="title">景点标题</div>
      </div>
    </div>
    <!-- // 景点大图 -->

    <!-- 评分、景点介绍 -->
    <!-- // 评分、景点介绍 -->

    <!-- 地址信息 -->
    <!-- // 地址信息 -->

    <!-- 门票列表 -->
    <!-- // 门票列表 -->

    <!-- 用户评价列表 -->
    <!-- // 用户评价列表 -->
  </div>
</template>
<script>
export default {
  methods: {
    goBack () {
      this.$router.go(-1)
    }
  }
}
</script>
<style lang="less">
.page-sight-detail {
  // 景点大图
  .sight-banner {
    position: relative;
    .tips {
      position: absolute;
      left: 10px;
      bottom: 10px;
      font-size: 16px;
      color: #fff;

      .pic-sts {
        color: #fff;
        border-radius: 30px;
        font-size: 14px;
        background-color: rgba(0,0,0,0.4);
      }
    }
  }
}
</style>
