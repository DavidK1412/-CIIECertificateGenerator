<template>
  <router-view
    v-on:loadAdminView="loadAdminView"
    v-on:loadValidateView="loadValidateView"
    v-on:logOut="logOut"
  />
</template>

<script>
  export default {
    name: 'App',
    data(){
      return{
        isAuthenticated: false,
      }
    },
    components: {

    },
    methods: {
      verifyAuth: function(){
        if(!this.isAuthenticated) {
          this.$router.push({name: 'LogIn'});
        }else {
          this.$router.push({name: 'AdminView'});
        }
      },
      logOut: function(){
        this.isAuthenticated = false;
        localStorage.removeItem('accessData');
        localStorage.removeItem('user');
        this.$router.push({name: 'LogIn'});
      },
      loadAdminView: function(){
        this.isAuthenticated = true;
        this.$router.push({name: 'AdminView'});
      },
      loadValidateView: function(){
        this.$router.push({name: 'CertificateValidate'});
      }
    },
    created(){
      this.verifyAuth();
    }
  }

</script>

<style>
*{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
router-view{
  background: url("assets/background.jpg");
}
</style>
