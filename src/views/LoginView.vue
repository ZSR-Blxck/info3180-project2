 <template>
       
        <div>
            <div class="box">
                
                <h3>
                    Login to your account
                </h3>
                <div class="grid-container">
                    <form @submit="login">
                        <div class="form-group">
                            <label>Email</label>
                            <input type="email" v-model="email" class="form-control">
                        </div>
                        <div class="form-group">
                            <label>Password</label>
                            <input type="password" v-model="password" class= "form-control">
                        </div>
                        
                        <button type="submit" :disabled="password.length < 3">
                            Login <font-awesome-icon class="ml-3" :icon="['fas', 'arrow-right']" /> 
                        </button>                            
                    </form>
                </div>
            </div>
        </div>
    </template>
    <script>
       
        export default {
            name: 'Login',
            
            data() {
                return {
                    email: '',
                    password: '',
                    error: false,
                    errorMsg: `An error occurred, please try again`
                }
            },
            methods: {
                async login(e) {
                    e.preventDefault()
                    try {
                        const res = await this.axios.post(`http://localhost:3000/auth/local`, {
                            identifier: this.email,
                            password: this.password
                        });
                        
                        const { jwt, user } = res.data
                        window.localStorage.setItem('jwt', jwt)
                        window.localStorage.setItem('userData', JSON.stringify(user))
                        window.localStorage.setItem('bookmarks', JSON.stringify(user.bookmarks))
                        this.$router.push('/')
                    } catch(error) {
                        this.error = true
                        this.password = ''
                    }
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
        form{
            background-color:white;
            width:40%;
            margin-left:65%;
            padding:20px;
        }
        body{
            background-color:lightgrey;
        }
        h3{
            text-align:center;
        }
        button{
            margin-top:30px;
        }
        label{
            font-weight:bold;
        }
    </style>