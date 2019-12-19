<template light>
<v-app light>
  
<!--   <v-parallax src="https://c1.staticflickr.com/8/7559/15674626183_d08dc37864_b.jpg" class="pa-5 mb-5">
-->


 <div id="backdrop" class="pa-5 mb-5">
    <v-layout column justify-center>    
      <div class="ma-5 pa-5">
        <h1 class="white--text display-3">PistolStats.com</h1>
        <h2 class="white--text display-1">The Ultimate Pistol Database Engine</h2>
      </div>
    </v-layout>
  </div>
 
 <v-container>
  <div class="headline">
    This is currently a work in progress. Feel free to play around with it and check back again. 
  </div>
  <!-- <div class="headline">
    In the meantime, check out our <a href="/blog/gifts_for_gunners/">2018 Holiday Gift Guide!</a>
  </div> -->
 </v-container>
 <v-container>
  <div class="my-3" style="overflow-y:scroll; display:flex;">
    <div class="var_column">
        Size
        <v-select
          :items="['', 'Full', 'Compact', 'Subcompact']"
          label="Size"
          v-model="frame_size"
          single-line
        ></v-select>
      </div>
      <div class="var_column">
        Caliber
        <v-select
          :items="['', '.380', '9x19', '.22lr']"
          label="Caliber"
          v-model="caliber"
          single-line
        ></v-select>
      </div>

      <div class="var_column">
        Magazine Capacity
        <v-layout row>
          <v-flex xs5 class="pr-1">
            <v-select
            :items="['', '=', '≥', '≤']"
            v-model="magazine_capacity_sign"
            single-line
          ></v-select>
          </v-flex>
          <v-flex xs7 class="pl-1">
            <v-text-field
              v-model="magazine_capacity_value"
            ></v-text-field>
          </v-flex>
        </v-layout>
      </div>

      <div class="var_column">
        Action
        <v-select
          :items="['', 'SA', 'DAO', 'SA/DO']"
          label="Action"
          v-model="action"
          single-line
        ></v-select>
      </div>

      <div class="var_column">
        Hammer / Striker
        <v-select
          :items="['', 'Hammer', 'Striker']"
          single-line
          v-model="hammer"
        ></v-select>
      </div>

      <div class="var_column">
        MSRP
        <v-layout row>
          <v-flex xs7 class="pr-1">
            <v-select
            :items="['', '=', '≥', '≤']"
            single-line
            v-model="msrp_sign"
          ></v-select>
          </v-flex>
          <v-flex xs7 class="pl-1">
            <v-text-field
              prefix="$"
              v-model="msrp_value"
            ></v-text-field>
          </v-flex>
        </v-layout>
      </div>

     <div class="var_column">
        Weight (ounces)
        <v-layout row>
          <v-flex xs5 class="pr-1">
            <v-select
            :items="['', '=', '≥', '≤']"
            single-line
            v-model="weight_sign"
          ></v-select>
          </v-flex>
          <v-flex xs7 class="pl-1">
            <v-text-field
            v-model="weight_value"
            ></v-text-field>
          </v-flex>
        </v-layout>
      </div>

      <div class="var_column">
        Length (in.)
        <v-layout row>
          <v-flex xs5 class="pr-1">
            <v-select
            :items="['', '=', '≥', '≤']"
            single-line
            v-model="length_sign"
          ></v-select>
          </v-flex>
          <v-flex xs7 class="pl-1">
            <v-text-field
            v-model="length_value"
            ></v-text-field>
          </v-flex>
        </v-layout>
      </div>

      <div class="var_column">
        Width (in.)
        <v-layout row>
          <v-flex xs5 class="pr-1">
            <v-select
            :items="['', '=', '≥', '≤']"
            single-line
            v-model="width_sign"
          ></v-select>
          </v-flex>
          <v-flex xs7 class="pl-1">
            <v-text-field
            v-model="width_value"
            ></v-text-field>
          </v-flex>
        </v-layout>
      </div>

      <div class="var_column">
        Height (in.)
        <v-layout row>
          <v-flex xs5 class="pr-1">
            <v-select
            :items="['', '=', '≥', '≤']"
            single-line
            v-model="height_sign"
          ></v-select>
          </v-flex>
          <v-flex xs7 class="pl-1">
            <v-text-field
            v-model="height_value"
            ></v-text-field>
          </v-flex>
        </v-layout>
      </div>

      <div class="var_column">
        Trigger Lbs
        <v-layout row>
          <v-flex xs5 class="pr-1">
            <v-select
            :items="['', '=', '≥', '≤']"
            single-line
            v-model="trigger_lbs_sign"
          ></v-select>
          </v-flex>
          <v-flex xs7 class="pl-1">
            <v-text-field
            v-model="trigger_lbs_value"
            ></v-text-field>
          </v-flex>
        </v-layout>
      </div>

      <div class="var_column">
        Barrel Height (in.)
        <v-layout row>
          <v-flex xs5 class="pr-1">
            <v-select
            :items="['', '=', '≥', '≤']"
            single-line
            v-model="barrel_height_sign"
          ></v-select>
          </v-flex>
          <v-flex xs7 class="pl-1">
            <v-text-field
            v-model="barrel_height_value"
            ></v-text-field>
          </v-flex>
        </v-layout>
      </div>

      <div class="var_column">
        Sight Radius (in.)
        <v-layout row>
          <v-flex xs5 class="pr-1">
            <v-select
            :items="['', '=', '≥', '≤']"
            single-line
            v-model="sight_radius_sign"
          ></v-select>
          </v-flex>
          <v-flex xs7 class="pl-1">
            <v-text-field
            v-model="sight_radius_value"
            ></v-text-field>
          </v-flex>
        </v-layout>
      </div>

      <div class="var_column">
        Thumb Safety
        <v-select
          :items="['', 'Yes', 'No']"
          single-line
          v-model="thumb_safety"
        ></v-select>
      </div>
      <div class="var_column">
        Grip Safety
        <v-select
          :items="['', 'Yes', 'No']"
          v-model="grip_safety"
          single-line
        ></v-select>
      </div>

      <div class="var_column">
        Threaded Barrel
        <v-select
          v-model="threaded_barrel"
          :items="['', 'Yes', 'No']"
          single-line
        ></v-select>
      </div>

      <div class="var_column">
        Rifling
        <v-layout row>
          <v-flex xs5 class="pr-1">
            <v-select
            :items="['', '=', '≥', '≤']"
            single-line
            v-model="rifling_sign"
          ></v-select>
          </v-flex>
          <v-flex xs7 class="pl-1">
            <v-text-field
            v-model="rifling_value"
            ></v-text-field>
          </v-flex>
        </v-layout>
      </div>
  </div>

  <v-card>
  <div class="pa-2 grey lighten-3" color="">
  <v-toolbar card prominent color="grey lighten-3">
    <v-btn v-if="true" color="primary" @click="dialog=!dialog" class="">Compare</v-btn>
    <v-spacer></v-spacer>
    <span class="ma-4" style="font-size:1.25em;">Data Results</span>
  </v-toolbar>


    <!-- https://vuetifyjs.com/en/components/data-tables#example-server -->
<v-data-table
    :headers="headers"
    :items="items"
    v-model="selected"
    item-key="pk"
    class="elevation-1"
    :rows-per-page-items="[10, 25]"
    :pagination.sync="pagination"
    :total-items="totalItems"
    :loading="loading"
  >
    <template slot="headerCell" slot-scope="props">
      <v-tooltip bottom>
        <span slot="activator">
          {{ props.header.text }}
        </span>
        <span>
          {{ props.header.text }}
        </span>
      </v-tooltip>
    </template>
    <!-- 
      Server side, we need to pull out the data, and just serve up unique make model caliber with variations mingled in. Variations need to be marked seperately. On the frontend, when a user clicks an item, then we can add that to selected_items, and then we also show variations that match the selected items. If they click again, then we can remove it from selected items and not show that.
     -->
    <template slot="items" slot-scope="props">
      <tr v-if="props.item" @click="show_variations()">
      <td>
        <v-checkbox
          primary
          hide-details
          v-model="props.selected"
        ></v-checkbox>
      </td>
      <td>{{ props.item.make }}</td>
      <td>{{ props.item.model }}</td>

      <td class="text-xs-right">{{ props.item.caliber }}</td>
      <td class="text-xs-right">{{ props.item.magazine_capacity }}</td>
      <td class="text-xs-right">{{ props.item.msrp }}</td>
      <td class="text-xs-right">{{ props.item.weight }}</td>
      <td class="text-xs-right">{{ props.item.trigger_lbs }}</td>
    </tr>
    </template>
  </v-data-table>
</div>
</v-card>

 <v-dialog v-model="dialog" scrollable max-width="900px">
      <v-card>
        <v-card-text>
          <v-layout>
            <v-flex xs6 v-for="gun in selected" :key="selected.pk" class="mx-2">
              <v-card>
                <div class="text-xs-center">
                  <img class="ma-1" :src="gun.image_url" height="200px" >
                </div>
                <v-card-title primary-title>
                  <div>
                    <h3 class="headline mb-0">{{gun.make}} - {{gun.model}}</h3>
                    <h3 class="subheading">{{ gun.variation }}</h3>
                  </div>
                </v-card-title>

                <v-list two-line>
                  <template v-for="(value, key) in gun" v-if="['image_url', 'make', 'model', 'variation', 'pk'].indexOf(key) == -1">
                    <v-list-tile :key="key">
                      <v-list-tile-content>
                        <v-list-tile-title>{{value}}</v-list-tile-title>
                        <v-list-tile-sub-title class="pl-0" style="text-transform: capitalize;">{{key.replace("_", " ")}}</v-list-tile-sub-title>
                      </v-list-tile-content>
                    </v-list-tile>
                    <v-divider></v-divider>
                  </template>
                </v-list>
                <v-card-actions>
                  <v-btn flat color="primary">Share</v-btn>
                  <v-btn flat color="primary">Explore</v-btn>
                </v-card-actions>

              </v-card>
            </v-flex>
          </v-layout>

        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-btn color="primary" flat @click.native="dialog = false">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

</v-container>
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
/*.parallax__image-container{
  background-color: #222;
}
.parallax__image{
  opacity: 0.7 !important;
}*/
</style>
<script>
  //let logged_in = true
  let endpoint = "/db/"

  // let endpoint = "/"
  export default {
    data () {
      return {
        dialog: false,
        make: null,
        model: null,
        frame_size: null,
        caliber: null,
        magazine_capacity_sign: null,
        magazine_capacity_value: null,
        action: null,
        hammer: null,
        msrp_sign: null,
        msrp_value: null,
        weight_sign: null,
        weight_value: null,
        length_sign:null,
        length_value:null,
        width_sign: null,
        width_value: null,
        height_sign:null,
        height_value:null,
        trigger_lbs_sign: null,
        trigger_lbs_value: null,
        barrel_height_sign:null,
        barrel_height_value:null,
        sight_radius_sign: null,
        sight_radius_value: null,
        thumb_safety:null,
        grip_safety:null,
        threaded_barrel:null,
        rifling_sign: null,
        rifling_value: null,

        selected: [],
        items:[],
        variations:[ {text:"variation 1"}, {text:"variation 2"}, {text:"third variation"}, 
        ],
        totalItems: 8,
        loading: true,
        pagination: {
          rowsPerPage: 10
        },

        headers: [
          {
            text: '',
            sortable: false,
          },
          {
            text: 'Make',
            align: 'left',
            value: 'make'
          },
          {
            text: 'Model',
            align: 'left',
            value: 'model'
          },
          { text: 'Caliber', value: 'caliber' },
          { text: 'Magazine Size', value: 'magazine_capacity' },
          { text: 'MSRP', value: 'msrp' },
          { text: 'Weight', value: 'weight' },
          { text: 'Trigger Lbs', value: 'trigger_lbs' }
        ]
      }
    },
    watch: {
      selected: function(){
        if (this.selected.length > 3)
          this.selected = this.selected.slice(0,3)
      },
      frame_size: function(){ this.getDataFromApi() },
      caliber: function(){ this.getDataFromApi() },
      magazine_capacity_sign: function(){ this.getDataFromApi() },
      magazine_capacity_value: function(){ this.getDataFromApi() },
      action: function(){ this.getDataFromApi() },
      hammer_striker: function(){ this.getDataFromApi() },
      msrp_sign: function(){ this.getDataFromApi() },
      msrp_value: function(){ this.getDataFromApi() },
      weight_sign: function(){ this.getDataFromApi() },
      weight_value: function(){ this.getDataFromApi() },
      length_sign: function(){ this.getDataFromApi() },
      length_value: function(){ this.getDataFromApi() },
      width_sign: function(){ this.getDataFromApi() },
      width_value: function(){ this.getDataFromApi() },
      height_sign: function(){ this.getDataFromApi() },
      height_value: function(){ this.getDataFromApi() },
      trigger_lbs_sign: function(){ this.getDataFromApi() },
      trigger_lbs_value: function(){ this.getDataFromApi() },
      barrel_height_sign: function(){ this.getDataFromApi() },
      barrel_height_value: function(){ this.getDataFromApi() },
      sight_radius_sign: function(){ this.getDataFromApi() },
      sight_radius_value: function(){ this.getDataFromApi() },
      thumb_safety: function(){ this.getDataFromApi() },
      grip_safety: function(){ this.getDataFromApi() },
      threaded_barrel: function(){ this.getDataFromApi() },
      rifling_sign: function(){ this.getDataFromApi() },
      rifling_value: function(){ this.getDataFromApi() },

      pagination: {
        handler () {
          this.getDataFromApi()
        },
        deep: true
      }
    },
    mounted () {
      this.getDataFromApi()
    },
    methods: {
      show_variations(){
        console.log("Show Variations")
        
      },
      getDataFromApi () {
        this.loading = true
        this.selected = []
        const { sortBy, descending, page, rowsPerPage } = this.pagination

        let params = {
          "sortBy": sortBy,
          "rows": rowsPerPage,
          "page": page,
          "descending": descending,
          frame_size: this.frame_size,
          caliber: this.caliber,
          magazine_capacity_sign: this.magazine_capacity_sign,
          magazine_capacity_value: this.magazine_capacity_value,
          action: this.action,
          hammer: this.hammer,
          msrp_sign: this.msrp_sign,
          msrp_value: this.msrp_value,
          weight_sign: this.weight_sign,
          weight_value: this.weight_value,
          height_sign: this.height_sign,
          height_value: this.height_value,
          length_sign: this.length_sign,
          length_value: this.length_value,
          width_sign: this.width_sign,
          width_value: this.width_value,
          trigger_lbs_sign: this.trigger_lbs_sign,
          trigger_lbs_value: this.trigger_lbs_value,
          barrel_height_sign: this.barrel_height_sign,
          barrel_height_value: this.barrel_height_value,
          sight_radius_sign: this.sight_radius_sign,
          sight_radius_value: this.sight_radius_value,
          thumb_safety: this.thumb_safety,
          grip_safety: this.grip_safety,
          threaded_barrel: this.threaded_barrel,
          rifling_sign: this.rifling_sign,
          rifling_value: this.rifling_value,
        }
        console.log(params)
        this.$http.post(endpoint+'gun_query/', params).then(  
          function(data){
            this.loading = false
            if (!data.body.success) {
              alert(data.body.error)
            }else{
              this.items = data.body.guns
              this.totalItems = data.body.total_guns
            }
          }
        ).catch( function(error){
          console.log(error)
          this.loading = false
          alert("There's a problem reaching the server. If you think it's our fault, please let us know by sending us an email through the CONTACT link.");
        });
      }
    }
  }
</script>

<style>
#backdrop{
  background:url(/static/img/stats_background3.jpg);
  background-size:     cover;
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
.var_column {
   width: 160px;
   padding: 12px;
   flex-shrink: 0;
}
.container{
  max-width: 1000px;
}

</style>
