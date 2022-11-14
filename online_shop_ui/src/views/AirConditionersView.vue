<template>
  <section class="catalog">
    <div class="air_conditioner_list">
      <div class="row mt-2 air_conditioner">
        <div class="col-md-2">
          <AirConditioners></AirConditioners>
        </div>
      </div>

      <div class="row mt-2 air_conditioner">
        <div class="col-md-2">
          <AirConditioners></AirConditioners>
        </div>
      </div>

      <div class="row mt-2 air_conditioner">
        <div class="col-md-2">
          <AirConditioners></AirConditioners>
        </div>
      </div>

      <div class="row mt-2 air_conditioner">
        <div class="col-md-2">
          <AirConditioners></AirConditioners>
        </div>
      </div>

      <div class="row mt-2 air_conditioner">
        <div class="col-md-2">
          <AirConditioners></AirConditioners>
        </div>
      </div>

      <div class="row mt-2 air_conditioner">
        <div class="col-md-2">
          <AirConditioners></AirConditioners>
        </div>
      </div>
    </div>

  </section>
</template>

<script>
import Vue from 'vue';
import AirConditioners from "@/components/Products/AirConditioners.vue";
import ProductCard from "@/components/Products/ProductCard.vue";


export default Vue.extend({
  name: 'AirConditionersView',
  components: {AirConditioners, ProductCard},
});
</script>

<style>

.catalog {
}

.air_conditioner {
  margin-right: 10px;
  border: solid 1px grey;
}

.air_conditioner_list {

}

</style>