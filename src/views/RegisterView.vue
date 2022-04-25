<template>
  <div>
    <div>
      <div class="bg-grey-lighter about object-cover bg-cover bg-center min-h-screen flex flex-col">
        <div
          class="container max-w-sm mx-auto flex-1 flex flex-col items-center justify-center px-2">
          <form @submit.prevent="registerUser" class="bg-white px-6 py-8 rounded shadow-md text-black w-full">

              <h1 class="mb-8 text-3xl text-center">Sign up</h1>

              <input type="text" class="border rounded-lg px-3 py-2 mt-1 mb-5 text-sm w-full" placeholder="Fullname" v-model="fullname" required />

              <input type="text" class="border rounded-lg px-3 py-2 mt-1 mb-5 text-sm w-full" placeholder="Username" v-model="username" required />

              <input type="password" class="border rounded-lg px-3 py-2 mt-1 mb-5 text-sm w-full" placeholder="Password" v-model="password" required/>
          
              <input type="text" class="border rounded-lg px-3 py-2 mt-1 mb-5 text-sm w-full" placeholder="Email" v-model="email" required/>

              <input type="text" class="border rounded-lg px-3 py-2 mt-1 mb-5 text-sm w-full" placeholder="location" v-model="location" required />

              <textarea class="border rounded-lg px-3 py-2 mt-1 mb-5 text-sm w-full" placeholder="biography" v-model="bio" required></textarea>

              <label for="user-photo">Upload Photo</label>
                                <input type="file"  @change="uploadphoto" name="user_photo" ref="file" class="form-control" />

              <button type="submit" class="w-full text-center py-2.5 rounded-lg bg-green-500 text-black hover:bg-green-600 focus:outline-none my-1" @click="onSubmit">Register</button>
            </form>
          </div>
        </div>
      </div>
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