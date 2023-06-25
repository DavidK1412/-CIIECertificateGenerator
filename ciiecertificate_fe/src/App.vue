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
    computed: {
      isAuthenticated: {
        get: function(){
          return this.$route.meta.requiresAuth;
        },
        set: function(){}
      }
    },
    methods: {
      logOut: function(){
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
    created: function(){
      if(this.isAuthenticated){
        this.$router.push({name: 'AdminView'});
      }else{
        this.$router.push({name: 'LogIn'});
      }
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
