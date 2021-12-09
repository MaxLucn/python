<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld/>
    <my-component-name/>
  </div>
</template>

<script>
import Vue from 'vue'

// 第二步：导入创建的全局组件
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'


Vue.component('my-component-name', {
  template: '<h3>我的第一个局部组件</h3>'
})

// 第三步：注册该组件
export default {
  name: 'Home',
  components: {
    HelloWorld
  }
}
</script>
