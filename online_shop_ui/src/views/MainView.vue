<template>
  <section class="main">
  <div>
    <Main></Main>
  </div>
  </section>
</template>

<script>
import Vue from 'vue';
import Main from "@/components/StartPage/Main.vue";

export default Vue.extend({
  name: 'MainView',
  components: { Main },
});
</script>

<style scoped>

</style>