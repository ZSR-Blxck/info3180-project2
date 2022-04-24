<template>
    <div>
        <div class="flex items-center justify-center h-screen">
            <div class="sm:w-1/2">
                <div class="p-5 w-4/5 mx-auto text-left font-raleway">
                    <h1 class="font-bold text-left font-montserrat text-4xl sm:text-6xl mb-7">
                        New Car
                        </h1>
                        <p v-show="error" class="text-sm text-red-500">{{ errorMsg }}</p>
                        <form id="carForm" method="post" @submit.prevent="checkForm" novalidate="true">
                             <div class="form-group">
                                <label for="description">Description</label>
                                <textarea v-model="cars.carDescription" name="car_description" id="car-description" cols="30" rows="10" class="form-control"></textarea>
                            </div>
                            <div class="form-group">
                                <label for="car-Make">Car Make</label>
                                <input type="text" v-model="cars.carmake" name="car_make" id="car-Make" class="form-control" />
                            </div>
                            <div class="form-group">
                                <label for="car-model">Model</label>
                                <input type="text" v-model="cars.carModel" min="1" max="5" step="1" name="car_model" id="car-model" class="form-control" />
                            </div>
                             <div class="form-group">
                                <label for="car-year">Colour</label>
                                <input type="text" v-model="cars.carcolour" name="car_colour" id="car-colour" class="form-control" />
                            </div>
                            <div class="form-group">
                                <label for="car-year">Year</label>
                                <input type="text" v-model="cars.caryear" name="car_year" id="car-year" class="form-control" />
                            </div>

                            <div class= "form-group">
                                <span>Transmission: {{Automatic}} </span>
                                <br>
                                <select v-model="cars.carTransmission">
                                    <option>Automatic</option>
                                    <option>Standard</option>
                                </select>
                            </div>

                             <div class="form-group">
                                <label for="car-type">Type</label>
                                <input type="text" v-model="cars.carModel" min="1" max="5" step="1" name="car_model" id="car-model" class="form-control" />
                            </div>
                             <div class="form-group">
                                <label for="price">Price</label>
                                <input type="text" v-model="cars.carPrice" name="car_price" id="car-price" class="form-control"/>
                            </div>
                            <div class="form-group">
                                <label for="car-photo">Photo</label>
                                <input type="file"  @change="uploadphoto" name="car_photo" ref="file" class="form-control" />
                            </div>
                        </form>
                           
                    </div>
                    <div class="modal-footer">
                        <button @click="submitFile" >Save</button>
                    </div>
                </div>
            </div>
        </div>
</template>
<script>
    export default {
        data() {
            return {
                cars:{
                    carDescription: '',
                    carMake: '',
                    carModel: '',
                    carColour: '',
                    carYear:'',
                    carTransmission:'',
                    carType:'',
                    carPrice:'',
                    image: '',
                    error: null,
                    errorMsg: 'An Error occurred, please try again',
                }
            };
        },
        methods: {
            checkform: async function(e) {

                try {
                        await this.$https.post("http://localhost:3000/api/cars", 
                        {
                            carDescription:this.cars.carDescription,
                            carMake: this.cars.carMake,
                            carModel:this.cars.carModel,
                            carColour:this.cars.carColour,
                            carYear:this.cars.carYear,
                            carTransmission:this.cars.carTransmission,
                            carPrice:this.cars.carPrice,
                            images:this.cars.image,

                    });

                    this.cars.carDescription = '';
                    this.cars.carMake = '';
                    this.cars.carModel='';
                    this.cars.carColour='';
                    this.cars.carYear = '';
                    this.cars.carTransmission ='';
                    this.cars.carPrice='';
                    this.cars.image='';

                    return;
                } catch (error){  
                    this.cars.error = true;
                    return;
                }
            }
            e.preventDefault();
        }
    };
</script>