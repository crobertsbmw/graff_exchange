// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './Exchange'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import VueResource from 'vue-resource'

Vue.config.productionTip = false

Vue.use(VueResource)

Vue.use(Vuetify, {
  theme: {
    primary: '#637943',
  }
})

new Vue({
  el: '#app',
  components: { App },
  template: '<App/>'
})
