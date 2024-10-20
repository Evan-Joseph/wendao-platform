<template>
  <div class="profile max-w-md mx-auto mt-20 p-6 bg-white rounded shadow-md">
    <h2 class="text-2xl font-bold text-blue-600 mb-6">个人资料</h2>
    <form @submit.prevent="updateProfile">
      <div class="mb-4">
        <label for="username" class="block text-gray-700">用户名</label>
        <input type="text" v-model="username" class="w-full px-4 py-2 border rounded mt-1" />
      </div>
      <div class="mb-6">
        <label for="email" class="block text-gray-700">邮箱</label>
        <input type="email" v-model="email" class="w-full px-4 py-2 border rounded mt-1" />
      </div>
      <button type="submit" class="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-700 transition-all">更新资料</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'UserProfile',
  data() {
    return {
      username: 'Evan Joseph',
      email: 'evan@example.com',
    };
  },
  methods: {
    updateProfile() {
      console.log('更新个人资料:', this.username, this.email);
    },
  },
};
</script>
