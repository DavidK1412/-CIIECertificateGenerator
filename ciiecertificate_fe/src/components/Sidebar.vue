<template>
  <aside :class="`${ is_expanded ? 'is-expanded' : ''}`">
    <div class="logo">
      <img src="../assets/logo1.jpg" alt="Vue" />
    </div>

    <div class="menu-toggle-wrap">
      <button class="menu-toggle" v-on:click="ToggleMenu">
        <span class="material-icons">keyboard_double_arrow_right</span>
      </button>
    </div>

    <h3 class="text-center">Bienvenido: {{ user.name }}</h3>
    <div class="menu">
      <div v-if="loaded && user.can_create_users" @click="loadUsers" class="button">
        <span class="material-icons">group</span>
        <span class="text">Usuarios</span>
      </div>
      <div v-on:click="loadCertificates" n v-if="loaded" class="button">
        <span class="material-icons">description</span>
        <span class="text">Gestionar Certificados</span>
      </div>

    </div>

    <div class="flex"></div>

    <div class="menu">
      <div v-on:click="logOut" class="button">
        <span class="material-icons">logout</span>
        <span class="text">Cerrar sesión</span>
      </div>
    </div>
  </aside>
</template>

<script>
import { ref } from 'vue'
export default {
  name: 'SidebarMenu',
  components: {

  },
  data () {
    return {
      is_expanded: ref(localStorage.getItem("is_expanded") === "true"),
      user: {
        name: 'loading...',
        can_create_users: false
      },
      loaded: false
    }
  },
  methods: {
    ToggleMenu: function () {
      this.is_expanded = !this.is_expanded
      localStorage.setItem("is_expanded", this.is_expanded)
    },
    loadCertificates: function () {
      this.$parent.loadCertificates();
    }
    ,
    loadUsers: function () {
      this.$parent.loadUsers();
    },
    logOut: function () {
      this.$parent.logOut();
    },
    getUser: async function () {
      await new Promise(resolve => setTimeout(resolve, 2000));
      this.user = JSON.parse(localStorage.getItem("user"));
      this.loaded = true;
    }
  },
  async created() {
    await this.getUser();
  }
}

</script>

<style lang="scss" scoped>
aside {
  display: flex;
  flex-direction: column;

  background-color: var(--primary);
  color: var(--light);

  width: calc(2rem + 32px);
  overflow: hidden;
  min-height: 100vh;
  padding: 1rem;

  transition: 0.2s ease-in-out;

  .flex {
    flex: 1 1 0%;
  }

  .logo {
    margin-bottom: 1rem;

    img {
      width: 2rem;
    }
  }

  .menu-toggle-wrap {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 1rem;

    position: relative;
    top: 0;
    transition: 0.2s ease-in-out;

    .menu-toggle {
      transition: 0.2s ease-in-out;
      .material-icons {
        font-size: 2rem;
        color: var(--light);
        transition: 0.2s ease-out;
      }

      &:hover {
        .material-icons {
          color: var(--primary);
          transform: translateX(0.5rem);
        }
      }
    }
  }

  h3, .button .text {
    opacity: 0;
    transition: opacity 0.3s ease-in-out;
  }

  h3 {
    color: var(--light);
    font-size: 0.875rem;
    margin-bottom: 0.5rem;
    text-transform: uppercase;
  }

  .menu {
    margin: 0 -1rem;

    .button {
      display: flex;
      align-items: center;
      text-decoration: none;
      cursor: pointer;
      transition: 0.2s ease-in-out;
      padding: 0.5rem 1rem;

      .material-icons {
        font-size: 2rem;
        color: var(--light);
        transition: 0.2s ease-in-out;
      }
      .text {
        color: var(--light);
        transition: 0.2s ease-in-out;
      }

      &:hover {
        background-color: var(--dark-alt);

        .material-icons, .text {
          color: var(--primary);
        }
      }

      &.router-link-exact-active {
        background-color: var(--dark-alt);
        border-right: 5px solid var(--primary);

        .material-icons, .text {
          color: var(--primary);
        }
      }
    }
  }

  .footer {
    opacity: 0;
    transition: opacity 0.3s ease-in-out;

    p {
      font-size: 0.875rem;
      color: var(--grey);
    }
  }

  &.is-expanded {
    width: var(--sidebar-width);

    img {
      width: 10em;
    }

    .menu-toggle-wrap {
      top: -3rem;

      .menu-toggle {
        transform: rotate(-180deg);
      }
    }

    h3, .button .text {
      opacity: 1;
    }

    .button {
      .material-icons {
        margin-right: 1rem;
      }
    }

    .footer {
      opacity: 0;
    }
  }

  @media (max-width: 1024px) {
    position: absolute;
    z-index: 99;
  }
}
</style>