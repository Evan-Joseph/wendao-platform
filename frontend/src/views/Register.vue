<template>
  <div class="register">
    <h2>注册</h2>
    <form @submit.prevent="registerUser">
      <div>
        <label for="username">用户名</label>
        <input type="text" v-model="username" required />
      </div>
      <div>
        <label for="email">邮箱</label>
        <input type="email" v-model="email" required />
      </div>
      <div>
        <label for="password">密码</label>
        <input type="password" v-model="password" required />
      </div>
      <button type="submit">注册</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'RegisterPage',  // 修改为多词名称
  data() {
    return {
      username: '',
      email: '',
      password: ''
    };
  },
  methods: {
    registerUser() {
      axios.post('http://localhost:5000/api/register', {
        username: this.username,
        email: this.email,
        password: this.password
      })
      .then(response => {
        console.log('注册成功', response.data);
        // 注册成功后跳转到登录页面
        this.$router.push('/login');
      })
      .catch(error => {
        console.error('注册失败', error);
      });
    }
  }
};
</script>

<style scoped>
.register {
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
