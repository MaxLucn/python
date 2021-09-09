<template>
  <div class="page-home">
    <!-- <h1>慕旅游网</h1>
    <Button type="success">成功按钮</Button>
    <v-button type="success">成功按钮</v-button> -->

    <!-- banner 图 -->
    <Banner/>
    <!-- 热门景点推荐 -->
    <Hot/>
  </div>
</template>

<script>
// @is an alias to/src
// import axios from 'axios'
// import { ajax } from '@/utils/ajax'
// // 引入组件
// import Button from 'vant/lib/button'
// // 引入组件相关的样式
// import 'vant/lib/button/style'
// banner图
import Banner from '@/components/home/Banner'
import Hot from '@/components/home/Hot'

export default {
  name: 'Home',
  components: {
    // 测试 vant 组件的
    // 'v-button': Button,
    // Button

    // banner 图
    Banner,
    // 热门景点推荐
    Hot
  },
  created () {
    // ajax.get('http://django.t.mukewang.com/api/system/slider/list/?types=11').then(resp => {
    // ajax.get('http://localhost:8080/api/system/slider/list/?types=11').then(resp => {
    //   console.log('返回的结果: ', resp)
    // }).catch(err => {
    //   console.log('请求出错: ', err)
    // })
  }
}
</script>
<style lang="less" scoped>
.page-home {
  background-color:white
}
</style>
