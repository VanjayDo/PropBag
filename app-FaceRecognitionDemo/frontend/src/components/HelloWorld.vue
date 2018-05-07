<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>
      <router-link :to="{name:'RecogOldFace'}">Recog Old Face</router-link>
    </h2>
    &&
    <h2>
      <router-link :to="{name:'AddNewFace'}">Add New Face</router-link>
    </h2>
  </div>
</template>

<script>
  export default {
    name: 'HelloWorld',
    data() {
      return {
        msg: 'this is a face recognition demo'
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1, h2 {
    font-weight: normal;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline-block;
    margin: 0 10px;
  }

  a {
    color: #42b983;
  }
</style>
