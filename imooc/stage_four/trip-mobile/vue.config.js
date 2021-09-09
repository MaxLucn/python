// Node.js 里面的模块
module.exports = {
  // 设置代理的效果 
  // http://localhost:8080/api/test
  // =>
  // http://localhost:8080/test
  
  devServer: {
      proxy: {
          '/api': {
              target: 'http://django.t.mukewang.com',
              changeOrigin: true,
              pathRewrite: {
                // 需要 rewrite 重写的 URL
                // '/api': ''
              }
          }
      }
  }
}
