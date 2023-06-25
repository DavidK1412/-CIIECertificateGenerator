<template>
  <div class="home">
    <div class="d-flex flex-row">
      <SidebarMenu class="sidebar"></SidebarMenu>
      <div class="content">
        <UserAdmin v-if="userView"></UserAdmin>
        <certificates-admin v-if="certificateView"></certificates-admin>

      </div>

    </div>
  </div>
</template>

<script>
import SidebarMenu from "@/components/Sidebar.vue";
import CertificatesAdmin from "@/components/Certificates.vue";
import UserAdmin from "@/components/UserAdmin.vue";
import jwtDecode from "jwt-decode";
import axios from "axios";

export default {
  name: 'AdminView',
  components: {
    UserAdmin,
    SidebarMenu,
    CertificatesAdmin,
  },
  data () {
    return {
      userView: false,
      certificateView: true,
    }
  },
  computed: {
    isAuthenticated: {
      get: function(){
        return this.$route.meta.requiresAuth;
      },
      set: function(){}
    }
  },
  methods: {
    loadCertificates: function () {
      this.userView = false;
      this.certificateView = true;
    },
    loadUsers: function () {
      this.certificateView = false;
      this.userView = true;
    }, logOut: function () {
      this.$emit('logOut')
    },
    getUserData: async function () {
      const token = JSON.parse(localStorage.getItem("accessData"));
      const decoded = jwtDecode(token.accessToken);
      await axios.get(
          `http://localhost:8000/users/${decoded.user_id}/`,
          {
            headers: {
              'Authorization': `Bearer ${token.accessToken}`
            }
          }
      ).then((response) => {
        const user = response.data;
        localStorage.setItem('user', JSON.stringify(user));
      }).catch((error) => {
        console.log(error);
        this.logOut();
      })
    },
  },
  created(){
    this.getUserData();
  }
}
</script>


<style lang="scss">
:root {
  --primary: #005CA6;
  --primary-alt: #005CA7;
  --grey: #64748b;
  --dark: #1e293b;
  --dark-alt: #334155;
  --light: #f1f5f9;
  --sidebar-width: 300px;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Fira sans', sans-serif;
}



.content{
  margin-left: 5%;
  width: 100%;
}

body {
  background: var(--light);
}

button {
  cursor: pointer;
  appearance: none;
  border: none;
  outline: none;
  background: none;
}

.app {
  display: flex;

  main {
    flex: 1 1 0;
    padding: 2rem;

    @media (max-width: 1024px) {
      padding-left: 6rem;
    }
  }
}

@media (max-width: 728px) {
  .content{
    margin-left: 20%;

  }
}
</style>