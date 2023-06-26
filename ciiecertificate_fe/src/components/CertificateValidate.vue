<template>
  <div>
    <div class="container">
      <div id="errorModal" class="modal" tabindex="-1">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-body">
              <p v-if="certificate.founded">
                El certificado identificado con el ID <b>{{certificate.id}}</b> otorgado a <b>{{certificate.name}} identificado {{certificate.id_type}} {{certificate.person_id}}</b> por <b>{{certificate.description}}</b> expedido por el CIIE en la fecha <b>{{certificate.date}}</b> en la ciudad de <b>{{certificate.city}}</b>
              </p>
              <a id="download" v-if="certificate.founded" @click="downloadCertificate">Quiero descargarlo</a>
              <p v-else-if="!certificate.founded">
                El certificado identificado con el ID {{certificate.id}} no existe
              </p>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Cerrar</button>
            </div>
          </div>
        </div>
      </div>
      <div class="card-principal d-flex flex-column">
        <div class="fs-4 m-4">
          <i v-on:click="back" class="bi bi-arrow-left text-start"></i>
          <h4 class="text-lg-center">Validar certificado</h4>
        </div>

        <p class="text-lg-center fs-6 m-3">Por favor, ingresa el ID asociado al certificado para confirmar su validez</p>
        <div class="input-group input-group-lg p-4">
          <span class="input-group-text" id="inputGroup-sizing-lg"><i class="bi bi-file-earmark-check-fill"></i></span>
          <input v-model="certificate.id" type="text" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-lg">
        </div>
        <div class="input-group input-group-lg p-2">
          <button v-on:click="validateCertificate" type="button" class="btn btn-login float-end btn-lg btn-block">Validar</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script >
import axios from 'axios';
import {Modal} from "bootstrap";
import { generateCertificate } from "../scripts/certificateGenerator";

export default {
  name: 'CertificateValidate',
  components: {

  },
  data: function (){
    return {
      certificate : {
        id: '',
        founded: false,
        name: '',
        createdBy: '',
        date: '',
        city: '',
        description: '',
        person_id: '',
        id_type: ''
      }
    }
  },
  methods: {
    downloadCertificate: function(){
      generateCertificate(this.certificate);
    },
    validateCertificate: function(){
      const modal = new Modal(document.getElementById('errorModal'));
      axios.get(`http://localhost:8000/certificates/validate/${this.certificate.id}/`)
      .then(response => {
        this.certificate.name = response.data.name;
        this.certificate.createdBy = response.data.created_by.name;
        this.certificate.date = response.data.date;
        this.certificate.city = response.data.city;
        this.certificate.description = response.data.description;
        this.certificate.person_id = response.data.person_id;
        this.certificate.founded = true;
        modal.show();
      })
      .catch(error => {
        console.error(error)
        this.certificate.founded = false;
        modal.show();
      })
    },
    back: function(){
      this.$router.push({name: 'LogIn'});
    }
  }
}

</script>

<style scoped>

#download{
  color: #005CA6;
  cursor: pointer;
}

.card-principal{
  box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;
  position: absolute;
  border-radius: 1.5rem;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 30%;
  height: 60%;
}

.card-principal h5{
  text-align: center;
}

.btn-login{
  /* center button */
  margin: 0 auto;
  background-color: #005CA6;
  color: white;
}

i{
  cursor: pointer;
}

@media (max-width: 768px) {
  .card-principal{
    width: 90%;
    height: 90%;
  }
}

</style>