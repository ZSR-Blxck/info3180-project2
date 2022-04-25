<template>
    <div>
        <h1 class="font-bold text-left font-montserrat text-4xl sm:text-6xl mb-7">Add New Car</h1>
            <p v-show="error" class="text-sm text-red-500">{{ errorMsg }}</p>
            <form @submit.prevent="checkForm" >
                <div class="grid-container">
                     
                    <div class="form-group">
                        <label for="car-Make">Make</label>
                        <input type="text" v-model="carmake" name="car_make" id="car-Make" class="form-control" />
                    </div>
                    <div class="form-group">
                        <label for="car-model">Model</label>
                        <input type="text" v-model="carModel" min="1" max="5" step="1" name="car_model" id="car-model" class="form-control" />
                    </div>
                     <div class="form-group">
                        <label for="car-colour">Colour</label>
                        <input type="text" v-model="carcolour" name="car_colour" id="car-colour" class="form-control" />
                    </div>
                    <div class="form-group">
                        <label for="car-year">Year</label>
                        <input type="text" v-model="caryear" name="car_year" id="car-year" class="form-control" />
                    </div>

                    <div class="form-group">
                        <label for="price">Price</label>
                        <input type="text" v-model="carPrice" name="car_price" id="car-price" class="form-control"/>
                    </div>

                    <div class= "form-group">
                        <span>Car Type: {{Sedan}} </span>
                        <br>
                        <select id=car-type v-model="carType">
                            <option>Sedan</option>
                            <option>Coupe</option>
                            <option>Hatchback</option>
                            <option>SUV</option>
                            <option>Pickup Truck</option>
                            <option>Motorcycle</option>
                        </select>
                    </div>

                    <div class= "form-group">
                        <span>Transmission: {{Automatic}} </span>
                        <br>
                        <select id=transmission v-model="carTransmission">
                            <option>Automatic</option>
                            <option>Standard</option>
                        </select>
                    </div>

                </div>

                    <div class="form-group">
                        <label for="description">Description</label>
                        <textarea v-model="carDescription" name="car_description" id="car-description" cols="30" rows="10" class="form-control"></textarea>
                    </div>
                    <div class="form-group">
                        <label for="car-photo">Photo</label>
                        <input type="file"  @change="uploadphoto" name="car_photo" ref="file" class="form-control" />
                    </div>
                    <div class="modal-footer">
                        <button type="submit" @click="onSubmit" >Save</button>
                    </div>
            </form>
    </div>
</template>
<script>
    export default {
        name:"viewCars",
        data() {
            return {
                carDescription: '',
                carMake: '',
                carModel: '',
                carColour: '',
                carYear:'',
                carTransmission:'',
                carType:'',
                carPrice:'',
                image: '',
                errorMsg: 'An Error occurred, please try again',    
            };
        },
        methods: {
            async checkForm() {
                await fetch("http://localhost:3000/api/cars", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({
                    carDescription: "this.carDescription",
                    carMake: 'this.carMake',
                    carModel: 'this.carModel',
                    carColour: 'this.carColour',
                    carYear:'this.carYear',
                    carTransmission:'this.carTransmission',
                    carType:'this.carType',
                    carPrice:'this.carPrice',
                    image: 'this.image',
                 }),
            });
        },  
    }
}
</script>

<style>
    .grid-container {
      display: grid;
      grid-template-columns: auto auto;
      grid-gap: 10px;
      padding: 10px;
    }

    .grid-container > div {
    }
    #car-type{
        width:100%;
        height: 38px;
        border-radius: 5px;
        border-color: lightgrey;
    }
    #transmission{
        width:100%;
        height: 38px;
        border-radius: 5px;
        border-color: lightgrey;
    }

    form{
        margin-left:10%;
        background-color:white;
        width: 70%;
        text-align:left;
        padding:2%;
        border-radius: 10px;
        font-weight:bold;
    }
    body{
        background-color:lightgrey;
    }
    h1{
        margin-left:10%;
    }
    button{
        background-color: lightgreen;
        float:left;
        width: 200px;
        border-radius: 5px;
    }
</style>