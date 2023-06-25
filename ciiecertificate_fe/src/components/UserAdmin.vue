<template>
  <div id="createModal" class="modal" tabindex="-1">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Crear certificado</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">

          <div class="input-group input-group p-4">
            <span class="input-group-text" id="inputGroup-sizing-lg"><i class="bi bi-person-fill"></i></span>
            <input v-model="user.name" type="text" class="form-control" placeholder="Nombre usuario" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-lg">
          </div>
          <div class="input-group input-group p-4">
            <span class="input-group-text" id="inputGroup-sizing-lg"><i class="bi bi-person-vcard"></i></span>
            <input v-model="user.email" type="text" class="form-control" placeholder="Correo usuario" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-lg">
          </div>
          <div class="input-group input-group p-4">
            <span class="input-group-text" id="inputGroup-sizing-lg"><i class="bi bi-person-vcard"></i></span>
            <input v-model="user.password" type="password" class="form-control" placeholder="Contraseña" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-lg">
          </div>
          <div class="form-check p-4">
            <label class="form-check-label" for="flexCheckChecked">
              ¿Administrador?
            </label>
            <input class="form-check-input" type="checkbox"  v-model="user.can_create_users" id="flexCheckChecked">
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Cancelar</button>
          <button @click="createUser" type="button" data-bs-dismiss="modal" class="btn btn-success">Guardar Usuario</button>
        </div>
      </div>
    </div>
  </div>
  <div id="main">
    <div class="superior p-4">
      <div>
        <button v-on:click="getUsers" type="button" class="btn btn-primary"><i class="bi bi-card-checklist"></i> Listar todos los usuarios</button>
      </div>
      <div class="input-group ">
        <div class="input-group">
          <span class="input-group-text" id="addon-wrapping"><i class="bi bi-person-vcard"></i></span>
          <input v-model="userEmail" type="text" class="form-control" placeholder="Correo Usuario" aria-label="Username" aria-describedby="addon-wrapping">
          <button v-on:click="filterUsers" type="button" class="btn btn-primary"><i class="bi bi-search"></i></button>
        </div>
      </div>
      <div>
        <button type="button" class="btn btn-success" v-on:click="openModal"><i class="bi bi-card-checklist"></i> Nuevo usuario</button>
      </div>
    </div>
    <div class="table-responsive">
      <table class="table">
        <thead>
        <tr>
          <th scope="col">ID</th>
          <th scope="col">Email</th>
          <th scope="col">Nombre</th>
          <th scope="col">Admin</th>
          <th scope="col">Acciones</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="iuser in users" :key="iuser.id">
          <th scope="row">{{iuser.id}}</th>
          <td>{{iuser.email}}</td>
          <td>{{iuser.name}}</td>
          <td>{{iuser.can_create_users}} </td>
          <td>
            <button @click="deleteUser(iuser.id)" type="button" class="btn btn-danger"><i class="bi bi-trash"></i></button>
          </td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
  import axios from "axios";
  import {Modal} from "bootstrap";

  export default {
    name: 'UserAdmin',
    data() {
      return {
        users: [],
        user: {
          email: '',
          name: '',
          password: '',
          id: '',
          can_create_users: false,
        },
        activeUser: { },
        userEmail: '',
      }
    },
    methods: {
      openModal: function() {
        const modal = new Modal(document.getElementById('createModal'));
        modal.show();
      },
      createUser: function() {
        const token = JSON.parse(localStorage.getItem("accessData"));
        axios.post(
            'http://localhost:8000/users/'
            , this.user
            ,{
              headers: {
                'Authorization': `Bearer ${token.accessToken}`
              }
            }
        ).then(response => {
            console.log(response);
            this.user = {
              email: '',
              name: '',
              id: '',
              can_create_users: false,
            }
          }).catch(error => {
            console.log(error);
          });
      },
      filterUsers: function(){
        this.users = this.users.filter(user => user.email.includes(this.userEmail));
      },
      deleteUser: function(id) {
        const token = JSON.parse(localStorage.getItem("accessData"));
        if(id === this.activeUser.id){
          alert("No puedes eliminar tu propio usuario");
          return;
        }
        axios.delete(
            `http://localhost:8000/users/${id}/`,
            {
              headers: {
                'Authorization': `Bearer ${token.accessToken}`
              }
            }
        ).then(response => {
          if (response.status === 200) {
            alert("Usuario eliminado");
            this.getUsers();
          }
        }).catch(error => {
          console.log(error);
        });
      },
      getUsers: function(){
        const token = JSON.parse(localStorage.getItem("accessData"));
        axios.get(
            'http://127.0.0.1:8000/users/',
            {
              headers: {
                'Authorization': `Bearer ${token.accessToken}`
              }
            }
        ).then(response => {
          this.users = response.data;
        }).catch(error => {
          console.log(error);
        });
      },
    },
    created() {
      setTimeout(() => {
        this.activeUser = JSON.parse(localStorage.getItem("user"));
      }, 2000);
      this.getUsers();
    }
  }
</script>

<style scoped>
#main{
  width: 100%;
}

.superior{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.superior > div{
  width: 30%;
}


@media (max-width: 768px) {
  .superior{
    flex-direction: column;
  }
  .superior > div{
    margin: 5%;
    width: 50%;
  }
}
</style>