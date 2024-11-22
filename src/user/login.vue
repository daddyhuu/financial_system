<template>
  <div class="login-container" >
    <el-form ref="loginForm" :model="loginForm" :rules="loginRules" class="login-form" auto-complete="on" label-position="left">

      <div class="title-container">
        <h3 class="title">欢迎使用</h3>
      </div>

      <el-form-item prop="userName">
        <span class="svg-container">
<!--          <svg-icon icon-class="user" />-->
        </span>
        <el-input
          ref="userName"
          v-model="loginForm.userName"
          placeholder="账号"
          name="userName"
          type="text"
          tabindex="1"
          auto-complete="on"
          @keyup.enter.native="handleLogin"
          @submit.native.prevent
        />
      </el-form-item>

      <el-form-item prop="password">
        <span class="svg-container">
<!--          <svg-icon icon-class="password" />-->
        </span>
        <el-input
          :key="passwordType"
          ref="password"
          v-model="loginForm.password"
          :type="passwordType"
          placeholder="密码"
          name="password"
          tabindex="2"
          auto-complete="on"
          @keyup.enter.native="handleLogin"
        />
        <span class="show-pwd" @click="showPwd">
<!--          <svg-icon :icon-class="passwordType === 'password' ? 'eye' : 'eye-open'" />-->
        </span>
      </el-form-item>
      <el-button :loading="loading" type="primary" style="width:100%;margin-bottom:30px;" @click.native.prevent="handleLogin">登录</el-button>
<!--      <p class="tips">-->
<!--        <a href="/user" type="primary" @click="toRegister">还没有帐号？立即注册</a>-->
<!--      </p>-->
      <router-link to="/register" style="color: white">还没有帐号？立即注册</router-link>
    </el-form>
  </div>
</template>

<script>
import axios from "axios";
import http from "@/utils/request";
export default {
  name: 'login',
  data() {
    return {
      loginForm: {
        userName: '',
        password: ''
      },
      loginRules: {
        userName: [{ type: 'email', required: true, trigger: 'blur', message: '请输入账号' }],
        password: [{
          required: true,
          message: '输入密码',
          trigger: 'blur'
        }]
          // { pattern: /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,15}$/, message: '密码必须同时包含数字与字母,且长度为 6-15位' }]
      },
      loading: false,
      passwordType: 'password',
      redirect: undefined
    }
  },
  watch: {
    $route: {
      handler: function(route) {
        this.redirect = route.query && route.query.redirect
      },
      immediate: true
    }
  },
  methods: {
    toRegister(){
      this.$router.push('/user')
    },
    showPwd() {
      if (this.passwordType === 'password') {
        this.passwordType = ''
      } else {
        this.passwordType = 'password'
      }
      this.$nextTick(() => {
        this.$refs.password.focus()
      })
    },
    handleLogin() {
      this.$refs.loginForm.validate(valid => {
        this.loading = true;
        // 使用 axios 发送 POST 请求
        axios({
          method: 'post',
          url: 'http://61.240.140.173:8000/users/login/',
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          },
          data: {
            username: this.loginForm.userName,
            password: this.loginForm.password
          }
        })
        .then((res) => {
          if (res.data.message === 1) {
            this.loading = false;
            let user = { token: res.data.data, name: this.loginForm.userName, stats: res.data.stats };
            this.$store.commit('login', user);
            this.$router.push('/systematic_risk');
          } else {
            this.$message({
              showClose: true,
              message: res.data.data,
              type: 'warning'
            });
            this.loading = false;
          }
        })
        .catch((error) => {
          console.log(error);
          this.loading = false;
          alert('登陆失败');
        });
      });
    }
  },
  computed:{
    isLogin(){
      return this.$store.state.isLogin
    }
  },
}
</script>

<style lang="scss">
/* 修复input 背景不协调 和光标变色 */
/* Detail see https://github.com/PanJiaChen/vue-element-admin/pull/927 */

$bg:#283443;
$light_gray:#fff;
$cursor: #fff;

@supports (-webkit-mask: none) and (not (cater-color: $cursor)) {
  .login-container .el-input input {
    color: $cursor;
  }
}

/* reset element-ui css */
.login-container {
  .el-input {
    display: inline-block;
    height: 47px;
    width: 85%;

    input {
      background: transparent;
      border: 0px;
      -webkit-appearance: none;
      border-radius: 0px;
      padding: 12px 5px 12px 15px;
      color: $light_gray;
      height: 47px;
      caret-color: $cursor;

      &:-webkit-autofill {
        box-shadow: 0 0 0px 1000px $bg inset !important;
        -webkit-text-fill-color: $cursor !important;
      }
    }
  }

  .el-form-item {
    border: 1px solid rgba(255, 255, 255, 0.1);
    background: rgba(0, 0, 0, 0.1);
    border-radius: 5px;
    color: #454545;
  }
}
</style>

<style lang="scss" scoped>
$bg:#2d3a4b;
$dark_gray:#889aa4;
$light_gray:#eee;

.router-link-active {
  text-decoration: none;
  color: #fff;
}
a {
  text-decoration: none;
  color: #fff;
}

.login-container {
  min-height: 100vh;
  width: 100%;
  background-color: $bg;
  overflow: hidden;

  .login-form {
    position: relative;
    width: 520px;
    max-width: 100%;
    padding: 160px 35px 0;
    margin: 0 auto;
    overflow: hidden;
  }

  .tips {
    float: right;
    font-size: 14px;
    color: #fff;
    margin-bottom: 10px;

    span {
      &:first-of-type {
        margin-right: 16px;
      }
    }
  }

  .svg-container {
    padding: 6px 5px 6px 15px;
    color: $dark_gray;
    vertical-align: middle;
    width: 30px;
    display: inline-block;
  }

  .title-container {
    position: relative;

    .title {
      font-size: 26px;
      color: $light_gray;
      margin: 0px auto 40px auto;
      text-align: center;
      font-weight: bold;
    }
  }

  .show-pwd {
    position: absolute;
    right: 10px;
    top: 7px;
    font-size: 16px;
    color: $dark_gray;
    cursor: pointer;
    user-select: none;
  }
}
</style>

<style scoped>
/* 修改验证器样式 */
::v-deep .el-form-item.is-error .el-input__inner {
  border-color: #889aa4;
}
::v-deep .el-form-item.is-error .el-input__validateIcon {
  color: #889aa4;
}
::v-deep .el-form-item__error {
  color: #e6a23c;
}
</style>
