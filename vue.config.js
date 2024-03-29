const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave:false, //关闭eslint校验
  publicPath: '/',
  devServer: {
    proxy: {
      "/proxy_url": {           // /proxy_url 这个用来和根路径 baseURL 进行匹配
        target: 'http://61.240.140.173:8000/',  // 这个是填写跨域的请求域名+端口号，也就是要请求的URL(不包含URL路径)
        changeOrigin: true,  // 是否允许跨域请求，在本地会创建一个虚拟服务端，然后发送请求的数据，并同时接收请求的数据，这样服务端和服务端进行数据的交互就不会有跨域问题
        pathRewrite: {   // 路径重写
          '^/proxy_url': '/' // 替换target中的请求地址，原请求为 http://61.240.140.173:8000/issue/issue_analyse 实际请求为 http://61.240.140.173:8000/proxy_url/issue/issue_analyse
        }
      }
    }
  }
})
