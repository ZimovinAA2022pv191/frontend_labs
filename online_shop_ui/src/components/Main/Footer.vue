<template>
  <footer>
    <div class="container">
      <div>&copy; Patter Hause</div>
      <div>+7(930)090-14-87</div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "Footer"
}
</script>

<style>
footer {
  background-color: rgb(42, 63, 108);
  padding: 15px;
  color: #fff;
  height: 100px;
  margin-top: -100px;
}
footer .container {
  height: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>