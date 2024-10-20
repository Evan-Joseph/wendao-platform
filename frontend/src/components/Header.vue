<template>
  <header class="sticky top-0 z-50 bg-white shadow-md py-4">
    <div class="container mx-auto flex justify-between items-center px-6">
      <h1 class="text-3xl font-bold flex items-center text-green-600">
        <font-awesome-icon icon="graduation-cap" class="mr-2" /> 问道平台
      </h1>
      <nav class="flex space-x-6">
        <router-link to="/" class="text-gray-800 hover:text-green-500 transition duration-300 ease-in-out font-semibold">首页</router-link>
        <router-link v-if="!isAuthenticated" to="/login" class="text-gray-800 hover:text-green-500 transition duration-300 ease-in-out font-semibold">登录</router-link>
        <router-link v-if="!isAuthenticated" to="/register" class="text-gray-800 hover:text-green-500 transition duration-300 ease-in-out font-semibold">注册</router-link>
        <button v-if="isAuthenticated" @click="logout" class="text-gray-800 hover:text-red-500 transition duration-300 ease-in-out font-semibold">
          退出登录
        </button>
      </nav>
    </div>
  </header>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  name: 'HeaderComponent',
  computed: {
    ...mapState(['isAuthenticated']),
  },
  methods: {
    ...mapActions(['logout']),
    logout() {
      this.logout();
      this.$router.push('/login');
    },
  },
};
</script>

<style scoped>
header {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
nav a,
nav button {
  font-weight: bold;
  text-decoration: none;
  padding-bottom: 2px;
  border-bottom: 2px solid transparent;
}
nav a:hover,
nav button:hover {
  border-bottom-color: #38a169; /* Hover 时显示底部的绿色下划线 */
}
</style>
