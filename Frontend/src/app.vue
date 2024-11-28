<!-- frontend/src/App.vue -->
<template>
    <div id="app">
      <h1>EHR Management System</h1>
      <form @submit.prevent="submitRecord">
        <input v-model="patientId" placeholder="Patient ID" required />
        <input v-model="dataHash" placeholder="Data Hash" required />
        <button type="submit">Add Record</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        patientId: '',
        dataHash: ''
      }
    },
    methods: {
      async submitRecord() {
        await fetch('/add_record', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ patientId: this.patientId, dataHash: this.dataHash })
        });
        this.patientId = '';
        this.dataHash = '';
      }
    }
  }
  </script>