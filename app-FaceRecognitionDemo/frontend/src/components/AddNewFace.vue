<template>
  <div id="addFace">
    <h4>添加新的用户脸部特征:</h4>
    <form name="imgForm" id="newFaceForm" enctype="multipart/form-data" action="http://fill.your.sever.ip:8000/addFace"
          method='post'>
      <input class="faceImg" name="faceImg" id="newFaceImg" type='file' accept="image/*" @change="selectImg"/>
    </form>
    <br><br>
    <h2>
      <router-link :to="{name:'RecogOldFace'}">点此识别老用户</router-link>
    </h2>
  </div>

</template>

<script>
  export default {
    name: "AddNewFace",
    methods: {
      selectImg() {
        let form = document.getElementById('newFaceForm');
        form.submit();
      }
    }
  }
</script>

<style scoped>

</style>
