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
              <input v-model="certificate.name" type="text" class="form-control" placeholder="Nombre de la persona" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-lg">
            </div>
            <div class="input-group input-group p-4">
              <span class="input-group-text" id="inputGroup-sizing-lg"><i class="bi bi-person-vcard"></i></span>
              <input v-model="certificate.person_id" type="text" class="form-control" placeholder="ID de la persona" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-lg">
            </div>
            <div class="input-group input-group p-4">
              <span class="input-group-text" id="inputGroup-sizing-lg"><i class="bi bi-file-text-fill"></i></span>
              <textarea v-model="certificate.description" class="form-control"  aria-label="Sizing example input" aria-describedby="inputGroup-sizing-lg"> </textarea>
            </div>
            <div class="input-group input-group p-4">
              <span class="input-group-text" id="inputGroup-sizing-lg"><i class="bi bi-geo-alt-fill"></i></span>
              <input v-model="certificate.city"  type="text" class="form-control" placeholder="Ciudad donde se expide" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-lg">
            </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Cancelar</button>
          <button @click="createCertificate" type="button" data-bs-dismiss="modal" class="btn btn-success">Guardar certificado</button>
        </div>
      </div>
    </div>
  </div>
  <div id="main">
    <div class="superior p-4">
      <div>
        <button type="button" class="btn btn-primary"><i class="bi bi-card-checklist"></i> Listar todos los certificados</button>
      </div>
      <div class="input-group ">
        <div class="input-group">
          <span class="input-group-text" id="addon-wrapping"><i class="bi bi-person-vcard"></i></span>
          <input v-model="personName" type="text" class="form-control" placeholder="Nombre persona" aria-label="Username" aria-describedby="addon-wrapping">
          <button v-on:click="filterCertificates" type="button" class="btn btn-primary"><i class="bi bi-search"></i></button>
        </div>
      </div>
      <div>
        <button type="button" class="btn btn-success" @click="openModal"><i class="bi bi-card-checklist"></i> Nuevo certificado</button>
      </div>
    </div>
    <div class="table-responsive">
      <table class="table">
        <thead>
        <tr>
          <th scope="col">ID</th>
          <th scope="col">Fecha</th>
          <th scope="col">Otorgado a</th>
          <th scope="col">Descripción</th>
          <th scope="col">Creado por</th>
          <th scope="col">Acciones</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="icertificate in certificates" :key="icertificate.id">
          <th scope="row">{{icertificate.id}}</th>
          <td>{{icertificate.date}}</td>
          <td>{{icertificate.name}}</td>
          <td>{{icertificate.description}} </td>
          <td>{{icertificate.created_by.name}}</td>
          <td>
            <button @click="generate(icertificate)" type="button" class="btn btn-primary"><i class="bi bi-download"></i></button>
            <button @click="deleteCertificate(icertificate.id)" type="button" class="btn btn-danger"><i class="bi bi-trash"></i></button>
          </td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { Modal } from "bootstrap";
import { generateCertificate } from "../scripts/certificateGenerator"

export default {
  name: 'CertificatesAdmin',
  components: {

  },
  data () {
    return {
      user: {

      },
      certificates: [

      ],
      personName: "",
      certificate : {
        user_id: '',
        person_id: '',
        city: '',
        name: '',
        description: '',
      }
    }
  },
  methods: {
    openModal: function () {
      const modal = new Modal(document.getElementById('createModal'));
      modal.show();
    },
    generate: function (certificate) {
      generateCertificate(certificate);
    },
    deleteCertificate: function (id) {
      const token = JSON.parse(localStorage.getItem("accessData"));
      axios.delete(
          `http://127.0.0.1:8000/certificates/${id}/`,
          {
            headers: {
              'Authorization': `Bearer ${token.accessToken}`
            }
          }
      ).then( response => {
        if (response.status === 200){
          alert("Certificado eliminado correctamente");
          this.getAllCertificates();
        }
      }).catch( error => {
        console.log(error);
      })
    },
    getAllCertificates: function () {
      const token = JSON.parse(localStorage.getItem("accessData"));
      axios.get(
          'http://127.0.0.1:8000/certificates/',
          {
            headers: {
              'Authorization': `Bearer ${token.accessToken}`
            }
          }
      ).then((response) => {
        this.certificates = response.data;
      }).catch((error) => {
        console.log(error);
      })
    },
    filterCertificates: async function () {
      if (this.personName === ""){
        this.getAllCertificates();
        alert("No se ha ingresado un nombre");
      } else {
        this.certificates = this.certificates.filter(certificate => certificate.name.includes(this.personName));
      }
    },
    createCertificate: function () {
      const token = JSON.parse(localStorage.getItem("accessData"));
      this.certificate.user_id = JSON.parse(localStorage.getItem("user")).id;
      axios.post(
          'http://127.0.0.1:8000/certificates/',
          this.certificate,
          {
            headers: {
              'Authorization': `Bearer ${token.accessToken}`
            }
          }
      ).then(response => {
        this.getAllCertificates();
        alert(`Certificado ${response.data.id} creado con éxito`);
        generateCertificate(response.data)
        this.certificate = {
          user_id: '',
          person_id: '',
          city: '',
          name: '',
          description: '',
        }
      }).catch(error => {
        console.log(error);
      })
    }
  },
  created(){
    this.getAllCertificates();
    setTimeout(() => {
      this.certificate.user_id = JSON.parse(localStorage.getItem("user")).id;
      console.log(this.certificate.user_id)
    }, 2000);
  }
}

</script>

<style scoped>
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