import Vue from 'vue'
import Vuex from 'vuex'

import cookies from 'vue-cookies'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    authToken: cookies.get('auth-token'),
  },
  getters: {
    isLogIn: state => !!state.authToken,
    config: state => ({ headers: { Authorization: `Token ${state.authToken}` } })
  },
  mutations: {
    setCookie(state, payload) {
      state.authToken = payload
      cookies.set('auth-token', payload)
    },
  },
  actions: {
  },
  modules: {
  }
})
