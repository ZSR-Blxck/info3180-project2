<template>
	<router-link
		class="car-link"
		:to="{
			name: 'cars',
			params: { id: cars.id }
		}">

		<div class="car-card">
			<h4>{{ car.name }}</h4>
			<div class="carModel">
				
				<span> {{ cars.model }}</span>
			</div>
			<img :src="cars.image" />
		</div>
	</router-link>
</template>

<script>
export default {
	props: {
		event: {
			type: Object,
			required: true
		}
	},
	data() {
		return {
			make: this.cars.make
		};
	}
};
</script>

<style>
.cars-card {
	width: 320px;
	height: auto;
	min-height: 450px;
	background: rgb(60, 62, 68);
	border-radius: 20px;
	overflow: hidden;
	padding: 10px 15px;
	margin-bottom: 24px;
	margin-right: 10px;
	transition: all 0.2s linear;
	cursor: pointer;
	color: white;
}
.make {
	display: flex;
	justify-content: center;
}
img {
	margin-top: 5%;
}
.cars-card:hover {
	transform: scale(1.01);
	box-shadow: 0 3px 12px 0 rgba(0, 0, 0, 0.2),
		0 1px 15px 0 rgba(0, 0, 0, 0.19);
}
.cars-card > .title {
	margin: 0;
}
.cars-link {
	color: black;
	text-decoration: none;
	font-weight: 100;
}
</style>