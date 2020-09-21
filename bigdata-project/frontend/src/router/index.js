import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
// user
import Signup from '../views/user/Signup.vue'
import Login from '../views/user/Login.vue'
import Logout from '../views/user/Logout.vue'
import MyPage from '../views/user/MyPage.vue'

import Detail from '@/components/Detail.vue'
import Review from '@/views/Review.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: "/signup",
    name: "Signup",
    component: Signup
  },
  {
    path: "/login",
    name: "Login",
    component: Login
  },
  {
    path: "/logout",
    name: "Logout",
    component: Logout
  },
  {
    path: "/mypage",
    name: "MyPage",
    component: MyPage
  },
  {
    path: "/review",
    name: "Review",
    component: Review
  },
  {
    path: "/detail",
    name: "Detail",
    component: Detail
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
