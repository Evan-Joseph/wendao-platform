<template>
  <div id="app">
    <nav>
      <router-link to="/">首页</router-link> |
      <router-link to="/login">登录</router-link> |
      <router-link to="/register">注册</router-link>
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style scoped>
nav {
  margin-bottom: 1em;
  padding: 1em;
  background-color: #f8f8f8;
  border-bottom: 1px solid #ddd;
}
a {
  margin: 0 10px;
  text-decoration: none;
  color: #42b983;
}
a:hover {
  color: #333;
}
</style>
