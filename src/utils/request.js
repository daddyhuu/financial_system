// axios二次封装
import axios from 'axios'

//
const http = axios.create({
    //通用请求
    // baseURL:'http://61.240.140.173:8000/',//后端的地址前缀
    baseURL:'http://127.0.0.1:5000/',//后端的地址前缀
    // withCredentials:truenpm run serve
    // async:true,
    // timeout:'10000',//10s 超时时间
    // headers:{token:sessionStorage.getItem('token')?sessionStorage.getItem('token'):'null'}

})


http.interceptors.request.use(
    function(config) {
        // 在请求发送之前，为 headers 添加 token
        const token =sessionStorage.getItem('token')?sessionStorage.getItem('token'):'null';
        const name =sessionStorage.getItem('user')?sessionStorage.getItem('user'):'null';

        config.headers['token'] = token
        // config.headers['user_name']=name


        return config;
    },
    function(error) {
        return Promise.reject(error);
    }
);

// // 添加请求拦截器
// http.interceptors.request.use(function (config) {
//     // 在发送请求之前做些什么
//     return config;
//   }, function (error) {
//     // 对请求错误做些什么
//     return Promise.reject(error);
//   });

// // 添加响应拦截器
// http.interceptors.response.use(function (response) {
//     // 对响应数据做点什么
//     return response;
//   }, function (error) {
//     // 对响应错误做点什么
//     return Promise.reject(error);
//   });


export default http//将实例对外暴露

