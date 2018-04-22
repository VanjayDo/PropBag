<template>
  <div id="recogFace">
    <h4>识别老用户:</h4>
    <form name="imgForm" id="oldFaceForm" enctype="multipart/form-data"
          action="http://fill.your.sever.ip:8000/whetherOldFriend"
          method='post'>
      <input class="faceImg" name="faceImg" id="oldFaceImg" type='file' accept="image/*" @change="selectImg"/>
    </form>
    <br><br>
    <h2>
      <router-link :to="{name:'AddNewFace'}">点此添加新用户</router-link>
    </h2>
  </div>
</template>

<script>
  export default {
    name: 'demo',
    methods: {
      selectImg() {
        let form = document.getElementById('oldFaceForm');
        form.submit();
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
