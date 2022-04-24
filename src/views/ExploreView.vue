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
	</div>
</template>
<script>
   
</script>
<style scoped>
</style>