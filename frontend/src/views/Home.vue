<template>
  <div class="home min-h-screen flex flex-col justify-center items-center bg-gray-100">
    <div class="bg-white shadow-2xl rounded-lg p-10 text-center max-w-xl">
      <h2 class="text-4xl font-extrabold text-green-600 mb-6">欢迎来到问道平台</h2>
      <p class="text-lg text-gray-700 mb-8">让个性化学习变得简单而有效</p>
      <router-link to="/register">
        <button class="bg-gradient-to-r from-green-400 to-blue-500 text-white px-8 py-4 rounded-full font-semibold shadow-lg transform hover:scale-105 transition-transform duration-300 ease-in-out">
          立即开始
        </button>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
};
</script>

<style scoped>
.home {
  background-image: url('https://source.unsplash.com/1600x900/?education,learning'); /* 使用背景图片 */
  background-size: cover;
  background-position: center;
  padding-top: 60px; /* 为了给粘性导航栏腾出空间 */
}
</style>
