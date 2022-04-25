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

	    <div class="cars">
	    	<div v-if="loading" class="loading">Loading...</div>

    		<div v-if="error" class="error">{{ error }}</div>
		  	
		  	<div v-if="cars" class="content">
				<b-card>
					<b-card-body>
						hi
					</b-card-body>
				</b-card>
				<b-card>
					<b-card-body>
						<h2> {{cars.year}}{{cars.make}}</h2>
						<p> cars.model</p>
					</b-card-body>
				</b-card>
			</div>
			<div v-else null class="content">
				<h1> No Cars Added</h1>
			</div>
		</div>

	</div>
</template>
<script>
	export default {
		data() {
		    return {
		    	loading: false,
		      	cars: null,
		      	error: null,
		    }
		},
		created(){
		this.$watch(
			()=>this.$route.params,
			()=> {
				this.fetchData()
			},
			{immediate:true}
		)
	},
	methods:{
	  	fetchData() {
	  		this.error = this.cars= null
	  		this.loading = true

	  		getCars(this.$route.params.id,(err,post) => {
	  			this.loading = false
	  			if(err){
	  				this.error = err.toString()
	  			} else {
	  				this.cars=cars
	  			}

	  		})
	  	},
	},
	}
</script>
<style scoped>
</style>