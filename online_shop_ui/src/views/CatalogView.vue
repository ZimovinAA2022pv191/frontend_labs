<template>
  <section class="catalog">
    <h1>Каталог товаров</h1>

    <hr>

    <div class="row mt-2">
      <div class="col-md-2">
        <CatalogFilters></CatalogFilters>
      </div>
      <div class="col-md-10">
        <CatalogSorts></CatalogSorts>
        <section class="products-list row">
          <div class="col-md-6 col-lg-3 mb-5">
            <ProductCard></ProductCard>
          </div>
          <div class="col-md-6 col-lg-3 mb-5">
            <ProductCard></ProductCard>
          </div>
          <div class="col-md-6 col-lg-3 mb-5">
            <ProductCard></ProductCard>
          </div>
          <div class="col-md-6 col-lg-3 mb-5">
            <ProductCard></ProductCard>
          </div>
          <div class="col-md-6 col-lg-3 mb-5">
            <ProductCard></ProductCard>
          </div>
          <div class="col-md-6 col-lg-3 mb-5">
            <ProductCard></ProductCard>
          </div>
          <div class="col-md-6 col-lg-3 mb-5">
            <ProductCard></ProductCard>
          </div>
          <div class="col-md-6 col-lg-3 mb-5">
            <ProductCard></ProductCard>
          </div>
        </section>
      </div>
    </div>
  </section>
</template>

<script lang="ts">
import Vue from 'vue';
import ProductCard from "@/components/Products/ProductCard.vue";
import CatalogFilters from "@/components/Catalog/CatalogFilters";
import CatalogSorts from "@/components/Catalog/CatalogSorts";

export default Vue.extend({
  name: 'CatalogView',
  components: { ProductCard, CatalogFilters, CatalogSorts },
});
</script>