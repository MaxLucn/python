import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
// import * as filters from './utils/filters'
// 在不熟悉 Vant 插件的时候，避免频繁的找组件浪费时间，把所有的 VantUI 组件库引入
import Vant from 'vant'
import 'vant/lib/index.css'

// 把 VantUI 当作一个插件，在 Vue 中使用
Vue.use(Vant)

Vue.config.productionTip = false

// 注册过滤器
// Objects.keys(filters).forEach(k => Vue.filters(k, filters[k]))

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
