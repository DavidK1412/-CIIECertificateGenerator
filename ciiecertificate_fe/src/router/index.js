import { createRouter, createWebHashHistory } from 'vue-router'
import App from "@/App.vue";

import LogIn from "@/components/LogIn.vue";
import CertificateValidate from "@/components/CertificateValidate.vue";
import AdminView from "@/views/AdminView.vue";

const routes = [
  {
    path: '/',
    name: 'home',
    component: App
  },
  {
    path: '/login',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/validate',
    name: 'CertificateValidate',
    component: CertificateValidate
  },
  {
    path: '/admin',
    name: 'AdminView',
    component: AdminView
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
