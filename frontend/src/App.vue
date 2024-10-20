<template>
  <div id="app">
    <Header />
    <router-view />
    <Footer />
  </div>
</template>

<script>
import Header from './components/Header.vue';
import Footer from './components/Footer.vue';

export default {
  name: 'App',
  components: {
    Header,
    Footer
  }
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
