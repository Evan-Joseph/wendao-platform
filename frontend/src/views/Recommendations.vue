<template>
  <div class="recommendations">
    <h2>为您推荐的学习资源</h2>
    <ul>
      <li v-for="resource in resources" :key="resource.id">
        <h3>{{ resource.title }}</h3>
        <p>{{ resource.description }}</p>
        <button @click="likeResource(resource)">👍 {{ resource.likes }} 喜欢</button>
        <button @click="markAsCompleted(resource)">✅ 标记为完成</button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'RecommendationsPage',  // 修改为多词名称
  data() {
    return {
      resources: [
        {id: 1, title: '学习 JavaScript 基础', description: '适合初学者', likes: 0, completed: false},
        {id: 2, title: '深度学习导论', description: '机器学习入门', likes: 0, completed: false}
      ]
    };
  },
  methods: {
    likeResource(resource) {
      resource.likes++;
      // 可以在这里向后端发送请求，更新资源的点赞数量
    },
    markAsCompleted(resource) {
      resource.completed = true;
      // 同样可以在这里向后端发送请求，标记资源已完成
    }
  }
};
</script>

<style scoped>
.recommendations {
  max-width: 800px;
  margin: 0 auto;
  padding: 2em;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 1.5em;
  padding: 1em;
  border: 1px solid #ddd;
  border-radius: 5px;
}

button {
  margin-right: 10px;
  padding: 5px 10px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 3px;
}

button:hover {
  background-color: #2a8d6d;
}
</style>
