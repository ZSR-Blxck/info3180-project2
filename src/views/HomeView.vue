<script>
export default {
    data() {
        return {
            message: "Buy and Sell Cars Online",
            message2: "United Auto Sales provides the fastest, easiest and most user friendly way to buy or sell cars online. Find a Great Price on the Vehicle You Want"
        };
    },
}
</script>

<template>
    <div class="container">
      <div class="grid-container">
        <div class="item1">
            <h1>{{ message }}</h1>
            <p>{{message2}}</p>
        </div>
        <div class="item2">
            <img alt="Vue logo" class="logo" src="@/assets/2018-Ford-Mustang-GT-Performance-Pack-Manual-04.webp"/>
        </div>
      </div>
    </div>
</template>

<style>
/* Add any component specific styles here */
    .grid-container {
      display: grid;
      grid-template-columns: auto auto;
      grid-gap: 10px;
      padding: 10px;
    }

    .grid-container > div {
    }
    img{
        width:100%;
        height:120%;
    }
    .item1{
        padding-top:20%;
        text-align:center;
        width:70%;
    }
</style>