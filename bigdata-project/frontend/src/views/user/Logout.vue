<template>
  <div />
</template>

<script>
import axios from "axios";
import cookies from 'vue-cookies'
import { mapGetters, mapMutations } from 'vuex';
export default {
  data() {
    return {
    }
  },
  computed: {
    ...mapGetters(["config"])
  },
  created() {
    this.logout()
  },
  methods: {
    ...mapMutations(["setCookie"]),
    logout() {
      axios.post(`http://localhost:8000/rest-auth/logout/`, null, this.config)
      .then((res) => {
        console.log(res)
        this.setCookie(null)
        cookies.remove('auth-token')
        this.$router.push('/')
      })
    }
  },
  
}
</script>

<style>

</style>