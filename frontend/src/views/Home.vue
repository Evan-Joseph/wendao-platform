<template>
  <div class="home">
    <h1>欢迎来到问道平台</h1>
    <p>这是首页。</p>
  </div>
</template>

<script>
export default {
  name: 'HomePage',  // 确保名称是多词的，避免 eslint 警告
};
</script>

<style scoped>
.home {
  text-align: center;
  margin-top: 2em;
}
</style>
