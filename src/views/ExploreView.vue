<template>
	<div class="cars">
	    <br>
	    <h2 class="page-header" id="explore-head">Explore</h2>
	    <br>
	    <div id="exp" class="card text-left" style="width: 48rem;">
	        <form id="search">
	            <div class="row mb-2">
	                <div class="col-auto">
	                    <div class="form-group">
	                        <label for="make">Make</label>
	                        <input name="make" v-model="make" placeholder="Make" class="form-control explore-field">
	                    </div>
	                </div>
	                <div class="col-auto">
	                    <div class="form-group">
	                        <label for="model">Model</label>
	                        <input name="model" v-model="model" placeholder="Model" class="form-control explore-field">
	                    </div>
	                </div>
	                <div class="col-auto">
	                    <div class="form-group">
	                        <br>
	                        <button type="button" class="btn btn-success">Search</button>
	                    </div>
	                </div>
	            </div>
	        </form>
	    </div>

	     <section class="cars">
            <div v-if="!cars.length" class="no-cars">
                You haven't added any cars.
            </div>
            <div v-for="(car, index) in cars" class="card">
                <svg class="bd-placeholder-img card-img-top" width="100%" height="180" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: Image cap" preserveAspectRatio="xMidYMid slice" focusable="false"><title>Placeholder</title><rect width="100%" height="100%" fill="#868e96"></rect><text x="50%" y="50%" fill="#dee2e6" dy=".3em">Image</text></svg>
                <div class="card-body">
                    <h5 class="card-title">{{ car.Make }}</h5>
                    <p class="card-text">{{ car.Model }}</p>
                    <p class="card-text text-center text-muted">
                        <img src="images/star.svg" alt="star" v-for="n in car.favorite" /> <br><small>({{ car.favorite + '/5' }} {{ (car.favorite > 1) ? 'stars' : 'star' }})</small>
                    </p>
                </div>
                <div class="card-footer text-muted d-flex">
                    <button @click="editMovie(index)" class="btn btn-primary btn-sm text-right"><img src="images/pencil.svg" alt=""> Edit</button>
                    <button @click="removeMovie(index)" class="btn btn-danger btn-sm text-right"><img src="images/trashcan.svg" alt=""> Remove</button>
                </div>
            </div>
            <!-- <car-card v-for="(car, index) in cars" 
                        v-bind:car="car"
                        v-bind:key="index" 
                        v-on:edit="editMovie(index)" 
                        v-on:remove="removeMovie(index)">
            </car-card> -->
        </section>

	</div>
</template>
<script>
	
</script>
<style scoped>
</style>