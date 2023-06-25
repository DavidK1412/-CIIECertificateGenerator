import { createRouter, createWebHashHistory } from 'vue-router'
import App from "@/App.vue";

import LogIn from "@/components/LogIn.vue";
import CertificateValidate from "@/components/CertificateValidate.vue";
import AdminView from "@/views/AdminView.vue";
import axios from "axios";

const routes = [
  {
    path: '/',
    name: 'home',
    component: App,
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
    component: AdminView,
    meta: {
        requiresAuth: true
    }
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
});

async function checkAuth() {
  if(localStorage.getItem("accessData") === null) {
    return false;
  }

  try{
    const token = JSON.parse(localStorage.getItem("accessData")).accessToken;
    const result = await axios.post("http://127.0.0.1:8000/verify/", {token: token});
    console.log(result);
    if (result.status === 200) {
      return true;
    }
  } catch (e) {
    console.log(e);
    return false;
  }
}

router.beforeEach(async (to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
        const auth = await checkAuth();
        if (!auth) {
        next({
            path: '/login',
            query: { redirect: to.fullPath }
        })
        } else {
        next();
        }
    } else {
        next();
    }
});

export default router
