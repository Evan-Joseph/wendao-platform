<template>
  <div class="login max-w-md mx-auto mt-20 p-6 bg-white rounded shadow-md">
    <h2 class="text-2xl font-bold text-blue-600 mb-6">登录</h2>
    <form @submit.prevent="loginUser">
      <div class="mb-4">
        <label for="email" class="block text-gray-700">邮箱</label>
        <input type="email" v-model="email" required class="w-full px-4 py-2 border rounded mt-1" />
      </div>
      <div class="mb-6">
        <label for="password" class="block text-gray-700">密码</label>
        <input type="password" v-model="password" required class="w-full px-4 py-2 border rounded mt-1"/>
      </div>
      <button type="submit" class="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-700 transition-all">登录
      </button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LoginPage',
  data() {
    return {
      email: '',
      password: '',
    };
  },
  methods: {
    loginUser() {
      axios.post('http://localhost:5000/api/login', {
        email: this.email,
        password: this.password,
      })
          .then(response => {
            console.log('登录成功', response.data);
            this.$router.push('/');
          })
          .catch(error => {
            console.error('登录失败', error);
          });
    },
  },
};
</script>
