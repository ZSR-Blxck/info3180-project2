<template>
  <div>
    <h1>Register New User</h1>
      <form @submit.prevent="registerUser">
      <div class="grid-container">
	  		<div class="form-group">

	  			<label for="username">Username</label>
	  			<input type="text" name="username" placeholder="Username" v-model="username" required />

	  			<label for ="fullname">Fullname</label>
	      	<input type="text" name="fullname" placeholder="Fullname" v-model="fullname" required />
	      
	      	<label for ="location">Location</label>
	      	<input type="text" name="location" placeholder="location" v-model="location" required />
	  		</div>

	  		<div class="form-group">
	  			<label for ="password">Password</label>
	  			<input type="password" name="password" placeholder="Password" v-model="password" required/>

	  			<label for ="email">Email</label>
	      	<input type="text" name="email" placeholder="Email" v-model="email" required/>	      
	      </div>
	  	</div>

	  		<div class="form-group">
	  			<label for="bio">Biography</label>
	  			<textarea name="bio" v-model="bio"/>
	  		</div>
	      <div class="form-group">
	      	<label for="user-photo">Upload Photo</label>
	        <input type="file"  @change="uploadphoto" name="user_photo" ref="file" class="form-control" />
	      </div>

	      <button type="submit" class="w-full text-center py-2.5 rounded-lg bg-green-500 text-black hover:bg-green-600 focus:outline-none my-1" @click="onSubmit">Register</button>
      </form>
  </div>
</template>
<script>
export default {
  name: "register",
  data() {
    return {
      name: "",
      username: "",
      password: "",
      email: "",
      location:"",
      bio:"",
      user_photo:"",
      message:null,
    };
  },
  methods: {
    async registerUser() {
      await fetch("http://localhost:3000/api/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name: "this.name",
          username: "this.username",
          email: "this.email",
          password: "this.password",
          location: "this.location",
          bio: "this.bio",
          user_photo:"this.user_photo"
        }),
      });
    },

  }
};
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
    form{
        margin-left:15%;
        background-color:white;
        width: 70%;
        text-align:left;
        padding:2%;
        border-radius: 10px;
        font-weight:bold;
    }
    h1{
    	margin-left:15%;
    }
    body{
        background-color:lightgrey;
    }
    input{
    	width:100%;
    	padding:10px;
    	}
    textarea{
    	width:100%;
    	height:150px;
    }
</style>