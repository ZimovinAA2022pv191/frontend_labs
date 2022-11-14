<template>
  <div class="product">
    <div class="separator">
      <div class="front-title">
        <div>
          <img src="../../../public/catalog_images/rovex.jpeg" />
        </div>
        

          <div>
            <div class="product-title">Кондиционер (сплит-система) Rovex Trend-09 DEXP WM-F610NTMA/WW настенный
              [автоматический режим, вентиляция, обогрев, осушение, до - 20м<sup>2</sup>, 34дБ]
            </div>
        </div>

            <div class="product-info">
              <button class="btn btn-primary" type="submit">Сравнить</button>
            </div>
          </div>
          <div class="price_actions">
            <div class="price">
              <b>13 339 ₽</b>
              <div class="sub_price">
                от 1 345 ₽/мес.
              </div>
            </div>
            <div class="btn-buy">
              <button class="btn btn-cart">В корзину</button>
            </div>
          </div>


      </div>
  </div>
</template>

<script>
export default {
  name: "AirConditioners"
}
</script>

<style>

.front-title{
  display: flex;
}

.btn-buy{
  width: 100px;
  height: 100px;
}

.product {
  position: relative;
  border: 1px solid #ddd;
  padding: 15px;
  width: 1000px;
  height: 150px;

}

.price_actions{
  display: inline-block;

}

.separator{
  display: flex;
}

.product .product-title {
  font-size: 16px;
  width: 500px;
  padding-left: 20px;
}
.product img {
  width: 200px;
  height: 100px;
}
.price {
  background-color: red;
  font-size: 18px;
  font-family: 'Open Sans', sans-serif;

}

.product-info{
  align-items: center;
  padding-left: 20px;
  padding-top: 70px;
}

.sub_price{
  font-size: 14px;
}
.discount {
  background-color: #f8dc07;
  color: #333;
  padding: 5px;
  font-size: 18px;
  margin-left: 15px;
}
.triangle {
  position: absolute;
  left: 0;
  top: 0;
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 70px 70px 0 0;
  border-color: red transparent transparent transparent;
}
.discount-percent {
  position: absolute;
  top: 10px;
  left: 5px;
  color: #fff;
  font-size: 16px;
}
.btn-cart {
  width: 100%;
  background-color: rgb(42, 63, 108);
  color: #fff;
  border-radius: 4px;
  height: 45px;
}
.btn.btn-cart:hover {
  background-color: rgb(19, 24, 47);
  color: #fff;
}

</style>