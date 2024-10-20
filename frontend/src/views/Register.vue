<template>
  <div class="register max-w-md mx-auto mt-20 p-6 bg-white rounded shadow-md">
    <h2 class="text-2xl font-bold text-blue-600 mb-6">注册</h2>
    <form @submit.prevent="registerUser">
      <div class="mb-4">
        <label for="username" class="block text-gray-700">用户名</label>
        <input type="text" v-model="username" required class="w-full px-4 py-2 border rounded mt-1" />
      </div>
      <div class="mb-4">
        <label for="email" class="block text-gray-700">邮箱</label>
        <input type="email" v-model="email" required class="w-full px-4 py-2 border rounded mt-1" />
      </div>
      <div class="mb-6">
        <label for="password" class="block text-gray-700">密码</label>
        <input type="password" v-model="password" required class="w-full px-4 py-2 border rounded mt-1"/>
      </div>
      <button type="submit" class="w-full bg-green-500 text-white py-2 rounded hover:bg-green-700 transition-all">注册
      </button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'RegisterPage',
  data() {
    return {
      username: '',
      email: '',
      password: '',
    };
  },
  methods: {
    registerUser() {
      axios.post('http://localhost:5000/api/register', {
        username: this.username,
        email: this.email,
        password: this.password,
      })
          .then(response => {
            console.log('注册成功', response.data);
            this.$router.push('/login');
          })
          .catch(error => {
            console.error('注册失败', error);
          });
    },
  },
};
</script>
