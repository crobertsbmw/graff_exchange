<template light>
<v-app light>
  <v-toolbar>
    <v-toolbar-title>
        <img src="/static/img/logo_alpha.png" style="height:40px;">
    </v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-items>
      <v-btn v-if="!logged_in" flat href="#signup" class="grey--text text--darken-2 hidden-sm-and-down">Sign Up</v-btn>
      <v-btn v-if="!logged_in" flat class="grey--text text--darken-2 hidden-sm-and-down" @click="login_dialog=true">Log In</v-btn>
      <v-btn v-if="logged_in" flat class="grey--text text--darken-2 hidden-sm-and-down" @click="logout">Log Out</v-btn>
      <v-btn flat href="mailto:chase@indietroopers.com" class="grey--text text--darken-2 hidden-sm-and-down">Contact Us</v-btn>
      <v-spacer></v-spacer>
      <v-btn flat @click.stop="drawer = !drawer" class="grey--text text--darken-2 hidden-md-and-up">
        <v-icon>menu</v-icon>
      </v-btn>
    </v-toolbar-items>
  </v-toolbar>

    <v-navigation-drawer
      temporary
      right
      v-model="drawer"
      fixed
      app
    >
      <v-list>
        <v-list-tile v-if="!logged_in"href="#signup">
          <v-list-tile-action>
            <v-icon>assignment</v-icon>
          </v-list-tile-action>
          <v-list-tile-title>Sign Up</v-list-tile-title>
        </v-list-tile>

        <v-list-tile v-if="!logged_in" @click.stop="login_dialog=true">
          <v-list-tile-action>
            <v-icon>account_box</v-icon>
          </v-list-tile-action>
          <v-list-tile-title>Log In</v-list-tile-title>
        </v-list-tile>

        <v-list-tile v-if="logged_in" @click.stop="logout">
          <v-list-tile-action>
            <v-icon>directions_run</v-icon>
          </v-list-tile-action>
          <v-list-tile-title>Log Out</v-list-tile-title>
        </v-list-tile>

        <v-list-tile href="mailto:chase@indietroopers.com">
          <v-list-tile-action>
            <v-icon>mail</v-icon>
          </v-list-tile-action>
          <v-list-tile-title>Contact Us</v-list-tile-title>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
<!--   <v-parallax src="https://c1.staticflickr.com/8/7559/15674626183_d08dc37864_b.jpg" class="pa-5 mb-5">
 -->  
 <div id="backdrop" class="pa-0 mb-5">
    <v-layout v-resize="onResize" column justify-center :align-center="windowWidth < 800">    
      <div class="ma-5 pa-5">
        <h1 class="white--text">Exclusive Deals on Cutting Edge Tactical&nbsp;Tech</h1>
        <h3 class="white--text">Available to Members Only</h3>
        <h5 class="white--text">Launching Summer 2019</h5>
        <v-btn v-if="!logged_in" href="#signup" class="grey--text text--darken-4 primary mt-3" style="margin-left:0px;" @click="request = true">Request an Invite Code Now</v-btn>
      </div>
    </v-layout>
  </div>

  <v-container grid-list-md class="py-5">
    <v-layout row wrap>
      <v-flex sm6 xs12 style="display:flex; justify-content:center;">
        <v-card class="mx-4" style="max-width:400px;" center>
          <img src="/static/img/upper.jpg" width="100%">
          <div class="headline white--text pl-2 pa-1" style="background-color: rgba(1,1,1,0.5); height: fit-content; width: 100%;">55% OFF</div>
          <v-progress-linear class="my-0" value="80" height="8" color="success"></v-progress-linear>
          <div class="px-2" style="display:flex; justify-content:space-between;">
            <span>11 Hours Left</span> <span>80% Funded</span>
          </div>
          <div class="px-2 text-xs-right">
            30 TOQ
          </div>

          <div class="mx-2">
            <h3 class="headline mb-0 grey--text text--darken-3">TPNG AR-15 16" Complete&nbsp;Upper</h3>
            <p class="pb-2"><span style="font-size:150%" class="red--text text--darken-2">$179.00 </span>($399 msrp)</p> 
          </div>
        </v-card>
      </v-flex>

      <v-flex class="pa-4" sm6 xs12 style="font-size:130%; display:flex; justify-content:space-around; flex-direction:column;">
        <div>
          <p>
            <v-icon style="font-size:170%">timer</v-icon>&nbsp;&nbsp;&nbsp;Products are only live for 72 hours.
          </p>
          <p class="py-5">
            <v-icon style="font-size:170%">local_shipping</v-icon>&nbsp;&nbsp;&nbsp;Once the Target Order Quantity is fulfilled. No more orders are taken, and the order ships.
          </p>
          <p>
            <v-icon style="font-size:170%">remove_shopping_cart</v-icon>&nbsp;&nbsp;&nbsp;If the Target Order Quantity is not met, then the deal doesn't fund, and no one is charged.
          </p>
      </div>
      </v-flex>
    </v-layout>

    <v-divider class="my-5" id="signup"></v-divider>

    <transition name="slide" mode="out-in">
      <div v-if="logged_in" key="c">
        <v-layout row>
          <v-flex xs12 md8 offset-md2 lg6 offset-lg3>
            <v-card light class="pa-4">
              <h5 class="headline pb-4 text-xs-center">
                Invite Others
              </h5> 
              <p>
              Indie Troopers is a members only group. You have the power to invite others to become members using the code below, but please limit your invites to professionals in the industry:
            </p>
            <h2 class="text-xs-center">{{ref_code}}</h2>
            </v-card>
          </v-flex>
        </v-layout>
      </div>

      <div v-if="!logged_in && !request" key="a">
        <div style="width: 100%;" class="text-xs-center">
          <v-btn class="grey--text text--darken-4 primary mt-3 center-align" @click="request = !request">
            Request An Invite Code
          </v-btn>
          <p>OR</p>
        </div>
        <v-layout row>
          <v-flex xs12 md8 offset-md2 lg6 offset-lg3>
            <v-card light>
              <h5 class="headline pt-4 text-xs-center">
                Sign Up with Invite Code
              </h5> 
              <form class="pt-3 px-4 pb-4">
                <v-text-field
                  label="Invite Code"
                  v-model="invite_code"
                  :rules="codeRules"
                  validate-on-blur
                ></v-text-field>

                <v-text-field
                  label="Email"
                  v-model="email"
                  :rules="emailRules"
                  validate-on-blur
                ></v-text-field>

                <v-text-field
                  name="password"
                  label="Enter a Password"
                  hint="At least 8 characters"
                  v-model="password"
                  min="8"
                  type="password"
                >
                </v-text-field>
                <v-text-field
                  label="Confirm password"
                  v-model="confirm_password"
                  type="password"
                  :rules="confirmPassword"
                  validate-on-blur
                >
                </v-text-field>

                <v-btn @click="sign_up" :loading="loading" :disabled="!(email && password && confirm_password && invite_code)">Submit</v-btn>
              </form>
            </v-card>
          </v-flex>
        </v-layout>
      </div>

      <div v-if="!logged_in && request" key="b">
        <div style="width: 100%;" class="text-xs-center">
          <v-btn class="grey--text text--darken-4 primary mt-3 center-align" @click="request = !request">Already have an invite code?</v-btn>
          <p>OR</p>
        </div>

        <v-layout row>
          <v-flex xs12 md8 offset-md2 lg6 offset-lg3>
            <v-card light>
              <h5 class="headline pt-4 text-xs-center">
                Request an Invite Code
              </h5> 
              <form class="pt-3 px-4 pb-4">
                <v-text-field
                  label="Name"
                  v-model="name"
                ></v-text-field>
                
                <v-text-field
                  label="Email"
                  v-model="email"
                  :rules="emailRules"
                  validate-on-blur
                ></v-text-field>

                <p class="my-2" style="color: rgba(0,0,0,0.54); font-size: 16px; line-height: 20px;">
                  Are you Military, Ex-Military, Law Enforcement, former Law Enforcement, or otherwise regularly wear body armor for a living?
                </p>

                <v-radio-group class="pt-0" v-model="military_le" column>
                  <v-radio label="None"
                    color="green"
                    :value="null"></v-radio>

                  <v-radio label="Military"
                    color="green"
                    value="military"></v-radio>

                  <v-radio label="Ex-Military"
                    color="green"
                    value="ex-military"></v-radio>

                  <v-radio label="Law Enforcement"
                    color="green"
                    value="law_enforcement"></v-radio>

                  <v-radio label="Former Law Enforcement"
                    color="green"
                    value="ex-law_enforcement"></v-radio>

                  <v-radio label="Other"
                    color="green"
                    value="other"></v-radio>
                </v-radio-group>

                <p class="my-2" style="color: rgba(0,0,0,0.54); font-size: 16px; line-height: 20px;">
                  Approximately how often do you shoot?
                </p>

                <v-radio-group class="pt-0" v-model="shooting_frequency" column>
                  <v-radio label="Everyday"
                    color="green"
                    value="everyday"></v-radio>

                  <v-radio label="Few times a week"
                    color="green"
                    value="weekly"></v-radio>

                  <v-radio label="Few times a month"
                    color="green"
                    value="monthly"></v-radio>

                  <v-radio label="Few times a year"
                    color="green"
                    value="yearly"></v-radio>

                  <v-radio label="Hardly ever"
                    color="green"
                    value="never"></v-radio>
                </v-radio-group>

                <p class="my-2" style="color: rgba(0,0,0,0.54); font-size: 16px; line-height: 20px;">
                  What are you most interested in?
                </p>
                <v-checkbox v-model="interests"
                  class="pb-0 mb-0"
                  label="Target Shooting"
                  color="green"
                  value="target shooting"></v-checkbox>

                <v-checkbox v-model="interests"
                  label="Hunting"
                  color="green"
                  value="hunting"></v-checkbox>

                <v-checkbox v-model="interests"
                  label="Concealed Carry"
                  color="green"
                  value="concealed"></v-checkbox>

                <v-checkbox v-model="interests"
                  label="Home Defense"
                  color="green"
                  value="home defense"></v-checkbox>

                <v-checkbox v-model="interests"
                  label="Shotgun Shooting"
                  color="green"
                  value="shotguns"></v-checkbox>

                <v-checkbox v-model="interests"
                  class="mb-5"
                  label="Survival Gear"
                  color="green"
                  value="survival"></v-checkbox>

                <p class="my-2" style="color: rgba(0,0,0,0.54); font-size: 16px; line-height: 20px;">
                  Are you a competitive shooter?
                </p>

                <v-radio-group class="pt-0" v-model="competitive" column>
                  <v-radio label="Yes"
                    color="green"
                    value="true"></v-radio>
                  <v-radio label="No"
                    color="green"
                    value="false"></v-radio>
                </v-radio-group>

                <p class="my-2" style="color: rgba(0,0,0,0.54); font-size: 16px; line-height: 20px;">
                  Gender
                </p>

                <v-radio-group class="pt-0" v-model="gender" column>
                  <v-radio label="Female"
                    color="green"
                    value="Female"></v-radio>
                  <v-radio label="Male"
                    color="green"
                    value="Male"></v-radio>
                </v-radio-group>

                <v-text-field
                  label="Occupation"
                  v-model="occupation"
                ></v-text-field>

                <v-text-field
                  label="Best Rock 'n' Roll song of all time?"
                  v-model="song"
                ></v-text-field>

                <p class="my-2" style="color: rgba(0,0,0,0.54); font-size: 16px; line-height: 20px;">
                  Are you a certified shooting instructor?
                </p>
                <v-radio-group class="py-0 mb-0" v-model="instructor" column>
                  <v-radio label="No"
                    color="green"
                    :value="null"></v-radio>
                  <v-radio label="NRA"
                    color="green"
                    value="nra"></v-radio>
                  <v-radio label="USCCA"
                    color="green"
                    value="uscca"></v-radio>
                  <v-radio label="Other"
                    color="green"
                    value="other"></v-radio>
                </v-radio-group>

                <v-text-field
                  label="What's your next gun purchase?"
                  v-model="next_gun"
                ></v-text-field>

                <p class="my-2" style="color: rgba(0,0,0,0.54); font-size: 16px; line-height: 20px;">
                  Are you affiliated with any firearms, survival, tactical or otherwise related media outlets?
                </p>
                <v-radio-group class="pt-0" v-model="media" column>
                  <v-radio label="Yes"
                    color="green"
                    :value="true"></v-radio>
                  <v-radio label="No"
                    color="green"
                    :value="false"></v-radio>
                </v-radio-group>
                <v-text-field
                  v-if="media"
                  label="Please include a media link."
                  v-model="media_link"
                ></v-text-field>

                <p v-if="media==false" class="my-2" style="color: rgba(0,0,0,0.54); font-size: 16px; line-height: 20px;">
                  Are you affiliated with any firearms, survival, tactical or otherwise related <b>social media</b> outlets?
                </p>
                <v-radio-group v-if="media==false" class="pt-0" v-model="social" column>
                  <v-radio label="Yes"
                    color="green"
                    :value="true"></v-radio>
                  <v-radio label="No"
                    color="green"
                    :value="false"></v-radio>
                </v-radio-group>

                <v-text-field
                  v-if="social"
                  label="Please include a link to your social media profile"
                  v-model="social_link"
                ></v-text-field>

                <p class="my-2" style="color: rgba(0,0,0,0.54); font-size: 16px; line-height: 20px;">
                  Do you have a face tattoo?
                </p>
                <v-radio-group class="pt-0" v-model="face_tattoo" column>
                  <v-radio label="Yes"
                    color="green"
                    :value="true"></v-radio>
                  <v-radio label="No"
                    color="green"
                    :value="false"></v-radio>
                </v-radio-group>

                <v-btn @click="request_invite" :loading="loading" :disabled="!email">Submit</v-btn>
              </form>
            </v-card>
          </v-flex>
        </v-layout>
      </div>
    </transition>
  </v-container>

  <v-dialog v-model="login_dialog" lazy absolute width="400">
    <v-card>
      <v-card-title>
        <div class="headline">Login</div>
      </v-card-title>
      <v-card-text>
        <v-text-field
          label="Email"
          v-model="email"
          :rules="emailRules"
          validate-on-blur
        ></v-text-field>

        <v-text-field
          name="password"
          label="Password"
          v-model="password"
          min="8"
          type="password"
        ></v-text-field>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn class="green--text darken-1" flat="flat" @click.native="submit_login">Submit</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>

  <v-dialog v-model="success_dialog" lazy absolute width="400" persistent>
    <v-card>
      <v-card-title>
        <div class="headline">Success!</div>
      </v-card-title>
      <v-card-text v-if="request">We have received your application and will keep you updated via email at {{email}}. If you can't stand the suspense, you can always skip the line by buying an existing IndieTroopers member a box of Ammo in exchange for an Invite Code.</v-card-text>
      <v-card-text v-if="!request">You are all signed up. We will keep you updated via email at {{email}} as our March 29th launch date approaches.</v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn class="green--text darken-1" flat="flat" @click.native="success_dialog=false; email=null;">Sounds Good</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>

  <v-dialog v-model="denied_dialog" lazy absolute width="400" persistent>
    <v-card>
      <v-card-title>
        <div class="headline">Denied!</div>
      </v-card-title>
      <v-card-text>Unfortunately, your request has been denied. Our advanced algorithm detects that you are either high risk for making bad decisions, or a professional boxer that can afford to pay full retail.</v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn class="green--text darken-1" flat="flat" @click.native="denied_dialog=false;">Okay</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>

  <v-snackbar :timeout="6000" color="error" multi-line v-model="error_snackbar">
      {{ error_message }}
  </v-snackbar>

  <v-dialog v-model="error_dialog" lazy absolute max-width="400" persistent>
      <v-card>
        <v-card-title>
          <div class="headline">Something is wrong.</div>
        </v-card-title>
        <v-card-text>Try again. If it doesn't work. Send us an angry email.</v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn class="green--text darken-1" flat="flat" @click.native="submit()">Try Again</v-btn>
            <v-btn class="green--text darken-1" flat="flat" href="mailto:chase@indietroopers.com?Subject=Your%20website%20is%20broken&body=Just%20thought%20you%20should%20know%20that%20I%20spent%20like%2010%20minutes%20filling%20out%20this%20dumb%20invite%20request%20and%20now%20the%20submit%20button%20doesn't%20even%20work...">Send Angry Email</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

  <v-footer fluid class="primary px-0 py-5 my-0 grey--text text--darken-3">
        <div style="width:100%" class="text-xs-center">
          &copy; 2019 IndieTroopers.com
          <br>
          <a href="/static/privacy-policy.html" class="grey--text text--darken-3" style="text-decoration:none;">Privacy Policy</a>
      </div>
  </v-footer>

</v-app>
</template>

<style>
body{
  background-color: #fff;
}
.parallax__image-container{
  background-color: #222;
}
.parallax__image{
  opacity: 0.7 !important;
}
</style>
<script>
  //let logged_in = true
  // let endpoint = "http://127.0.0.1:8000/"
  let endpoint = "/"
  export default {
    data () {
      return {
        error_snackbar: false,
        error_message: "Invalid Invite Code.",
        login_dialog: false,
        success_dialog: false,
        denied_dialog: false,
        error_dialog: false,
        drawer: false,
        logged_in: false,
        windowWidth: 50,
        ref_code: null,
        face_tattoo: null,
        invite_code: null,
        loading: false,
        request: false,
        email: null,
        name: null,
        password: null,
        confirm_password: null,
        interests: [],
        military_le: null,
        media: null,
        media_link: null,
        social: null,
        social_link: null,
        gender: null,
        competitive: null,
        shooting_frequency: null,
        instructor: null,
        occupation: null,
        song: null,
        next_gun: null,
        emailRules: [
          (v) => !!v || 'E-mail is required',
          (v) => /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'E-mail must be valid'
        ],
        codeRules: [
          (v) => !!v || 'Invite Code is Required',
        ],
        confirmPassword: [
          (v) => v == this.password || "Passwords do not match.",
        ],
      }
    },
    mounted () {
      this.onResize()
      try{
        this.logged_in = logged_in
      }catch(e){
        console.log("Didn't get the log in var")
      }
      try{
        this.ref_code = ref_code
      }catch(e){
        console.log("Didn't get the ref code")
      }
    },
    methods: {
      onResize () {
        this.windowWidth = window.innerWidth
      },
      submit () {
        this.error_dialog = false
        if (this.request) this.request_invite()
        else this.sign_up()
      },
      request_invite () {
        var params = {
          name: this.name,
          email: this.email,
          military_le: this.military_le,
          shooting_frequency: this.shooting_frequency,
          interests: this.interests,
          competitive: this.competitive | false,
          gender: this.gender,
          occupation: this.occupation,
          song: this.song,
          instructor: this.instructor,
          next_gun: this.next_gun,
          media: this.media | false,
          social: this.social | false,
          media_link: this.media_link,
          social_link: this.social_link,
          face_tattoo: this.face_tattoo | false
        }
        this.loading = true
        this.$http.post(endpoint+'request_invite/', params).then(  
          function(data){
            this.loading = false
            if (this.face_tattoo && !this.military_le){
              this.denied_dialog = true
              return
            }
            this.success_dialog = data.body.success
            if (!data.body.success){
              this.error_message = data.body.error
              this.error_snackbar = true
              return
            }
            this.name = null
            this.military_le = null
            this.shooting_frequency = null
            this.interests = []
            this.competitive = false
            this.gender = null
            this.occupation = null
            this.song = null
            this.instructor = null
            this.next_gun = null
            this.media = null
            this.social = null
            this.media_link = null
            this.social_link = null
            this.face_tattoo = null
          }
        ).catch( function(error){
          this.loading = false
          this.error_dialog = true
        });
      },
      logout () {
        this.ref_code = ""
        this.logged_in = false
        this.$http.post(endpoint+'logout/')
      },
      submit_login () {
        var params = {
          email: this.email,
          password: this.password,
        }
        this.loading = true
        this.$http.post(endpoint+'login/', params).then(  
          function(data){
            this.loading = false
            if (!data.body.success) {
              this.error_message = data.body.error
              this.error_snackbar = true
              this.password = ""
              this.email = ""
            }else{
              this.login_dialog = false
              this.ref_code = data.body.ref_code
              this.logged_in = true
            }
          }
        ).catch( function(error){
          this.loading = false
          this.error_message = "There's a problem reaching the server. If you think it's our fault, please let us know by sending us an email through CONTACT link."
          this.error_snackbar = true
        });
      },
      sign_up () {
        if (this.password != this.confirm_password) {
          this.error_message = "Passwords do not match."
          this.error_snackbar = true
          return
        }
        var params = {
          invite_code: this.invite_code,
          email: this.email,
          password: this.password,
        }
        this.loading = true
        this.$http.post(endpoint+'sign_up/', params).then(  
          function(data){
            this.success_dialog = data.body.success
            this.loading = false
            if (!data.body.success) {
              this.error_message = data.body.error
              this.error_snackbar = true
            }else{
              this.ref_code = data.body.ref_code
              this.logged_in = true
            }
          }
        ).catch( function(error){
          this.loading = false
          this.error_dialog = true
        });
      }
    }
  }
</script>

<style>
#backdrop{
  background:url(/static/img/sniper_background2.jpg);
  background-size:     cover;                      /* <------ */
  background-repeat:   no-repeat;
  background-position: center center; 
}
.checkbox .input-group__details{
  
  display:none;
}
.slide-enter-active, .slide-leave-active{
  transition: all 0.4s ease;
}

.slide-enter {
  transform: translateX(25%);
  opacity: 0;
}
.slide-leave-to {
  transform: translateX(-25%);
  opacity: 0;
}

</style>
