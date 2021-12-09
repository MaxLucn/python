import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false

// 注册一个全局过滤器
Vue.filter('priceFormat2', function(price) {
  if (price === undefined || price === null || isNaN(price)) {
    return price
  }
  return '¥' + price.toFixed(2)
})

new Vue({
  // 路由的配置
  router,
  // Vuex, 状态管理
  store,
  render: h => h(App)
}).$mount('#app')
