<template>
  <div class="login">
    <h2>登录</h2>
    <form @submit.prevent="loginUser">
      <div>
        <label for="email">邮箱</label>
        <input type="email" v-model="email" required />
      </div>
      <div>
        <label for="password">密码</label>
        <input type="password" v-model="password" required />
      </div>
      <button type="submit">登录</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LoginPage',  // 确保名称已改为多词形式
  data() {
    return {
      email: '',
      password: ''
    };
  },
  methods: {
    loginUser() {
      axios.post('http://localhost:5000/api/login', {
        email: this.email,
        password: this.password
      })
      .then(response => {
        console.log('登录成功', response.data);
        // 登录成功后跳转到首页
        this.$router.push('/');
      })
      .catch(error => {
        console.error('登录失败', error);
      });
    }
  }
};
</script>

<style scoped>
.login {
  max-width: 400px;
  margin: 0 auto;
  padding: 2em;
  border: 1px solid #ccc;
  border-radius: 5px;
}
form div {
  margin-bottom: 1em;
}
button {
  width: 100%;
  padding: 0.5em;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 5px;
}
</style>
