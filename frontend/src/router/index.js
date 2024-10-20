import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Login from '../views/Login.vue';
import Register from '../views/Register.vue';
import LearningPath from '../views/LearningPath.vue';
import Recommendations from '../views/Recommendations.vue';
import Profile from '../views/Profile.vue';

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/login', name: 'Login', component: Login },
  { path: '/register', name: 'Register', component: Register },
  { path: '/learning-path', name: 'LearningPath', component: LearningPath },
  { path: '/recommendations', name: 'Recommendations', component: Recommendations },
  { path: '/profile', name: 'Profile', component: Profile }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
