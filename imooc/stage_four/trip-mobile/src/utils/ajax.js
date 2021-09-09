import axios from 'axios'

export const ajax = axios.create({
  headers: {
    source: 'h5',
    icode: 'J125887AB9B807279',
    'Content-Type': 'application/X-WWW-form-urlencoded'
  },
  withCredentials: true
})
ajax.interceptors.request.use(function (config) {
  // 在发送请求之前做些什么
  console.log('拦截到了请求信息')
  return config
}, function (error) {
  // 对请求错误做些什么
  return Promise.reject(error)
})

ajax.interceptors.response.use(function (response) {
  // 对响应数据做些什么
  console.log('拦截到了响应信息')
  return response
}, function (error) {
  // 对响应错误做点什么
  if (error.response.status === 401) {
    window.alert('未登录，即将跳转到登录页面')
  }
  return Promise.reject(error)
})
