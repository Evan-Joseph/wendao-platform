import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import './assets/main.css'; // 引入 Tailwind CSS

// FontAwesome 配置
import { library } from '@fortawesome/fontawesome-svg-core';
import { faGraduationCap } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

// 将需要使用的图标添加到库中
library.add(faGraduationCap);

const app = createApp(App);
app.component('font-awesome-icon', FontAwesomeIcon);
app.use(router);
app.use(store);
app.mount('#app');
