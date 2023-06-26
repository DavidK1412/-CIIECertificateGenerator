<template>
  <div>
    <div class="container">
      <div id="errorModal" class="modal" tabindex="-1">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-body">
              <p>Credenciales Incorrectas</p>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Cerrar</button>
            </div>
          </div>
        </div>
      </div>
      <div class="card-principal d-flex flex-row">
        <div class="first-card p-2  d-flex justify-content-center" >
          <img src="../assets/svgimage.jpg" alt="" class="img-fluid ">
        </div>
        <div class="second-card p-2 d-flex flex-column">
          <div class="image-top p-2">
            <img src="../assets/logo3.jpg" alt="Logo" class="Logo img-fluid">
          </div>
          <h5 class="p-4">Sistema de gestión de Certificados CIIE</h5>
          <div class="login-form">
            <form action="">
              <!-- Responsive form, email and password--->
              <div class="input-group input-group-lg p-4">
                <span class="input-group-text" id="inputGroup-sizing-lg"><i class="bi bi-envelope-at-fill"></i></span>
                <input v-model="user.email" type="email" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-lg">
              </div>
              <div class="input-group input-group-lg p-4">
                <span class="input-group-text" id="inputGroup-sizing-lg"><i class="bi bi-shield-lock-fill"></i></span>
                <input v-model="user.password" type="password" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-lg">
              </div>
              <div class="d-flex">
                <div class="input-group input-group-lg p-4">
                  <button v-on:click="logInUser" type="button" class="btn btn-login float-end btn-lg btn-block">Iniciar sesión</button>
                </div>
                <a class="p-4" v-on:click="loadValidateView">Quiero validar un certificado</a>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import {Modal} from "bootstrap";
export default {
  name: 'LogIn',
  components: {},
  data: function (){
    return {
      user: {
        email: '',
        password: ''
      }
    }
  },
  methods: {
    loadValidateView: function(){
      this.$emit('loadValidateView');
    },
    logInUser: function(){
      axios.post(
          'https://ciie-certificate-generator.vercel.app/login/',
          this.user,
      )
      .then((response) => {
        const userAccessData = {
          accessToken: response.data.access,
          refreshToken: response.data.refresh
        }
        console.log(userAccessData)
        this.$emit('loadAdminView', userAccessData);
        localStorage.setItem('accessData', JSON.stringify(userAccessData));
      })
      .catch((error) => {
        console.log(error);
        const modal = new Modal(document.getElementById('errorModal'));
        modal.show();
      })
    }
  }
}
</script>

<style scoped>


.card-principal{
  box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;
  position: absolute;
  border-radius: 1.5rem;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 75%;
  height: 80%;
}

.first-card{
  width:45%;
  height: 100%;
}

.second-card{
  margin: 1%;
  width: 55%;
  height: 100%;
}

.second-card h5{
  text-align: center;
}

.image-top{
  width: 100%;
  height: 20%;
}

.login-form{
  height: 80%;
  margin-bottom: 5%;

}

.Logo{
  width: 90%;
  height: 100%;
}

.btn-login{
  background-color: #005CA6;
  color: white;
}

a:hover{
  cursor: pointer;
}

/* Responsive */
@media (max-width: 768px) {

  .card-principal{
    width: 85%;
    height: 90%;
  }

  .first-card{
    width: 0%;
    height: 0%;
    display: none;
  }
  .second-card{
    width: 100%;
    height: 100%;
  }
}

</style>