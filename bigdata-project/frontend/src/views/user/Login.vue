<template>
  <div class="container">
    <h1>로그인</h1>
    <!-- <router-link to="/signup">
      <h6 class="mt-2">새 계정 만들기 ></h6>
    </router-link> -->
    <form class="mx-auto col-6">
      <div class="login-section">
        <div class="form-group">
          <v-text-field
            v-model="loginData.username"
            label="아이디"
            :rules="rules"
            hide-details="auto"
            type="email"
          />
        </div>
        <div class="form-group">
          <v-text-field v-model="loginData.password" type="password" label="비밀번호" />
        </div>
        <div class="d-flex justify-content-between">
          <div class="d-flex align-items-center">
            <b-form-checkbox
              id="checkbox-1"
              name="checkbox-1"
              value="accepted"
              unchecked-value="not_accepted"
            >내 계정 기억하기</b-form-checkbox>
          </div>
          <v-btn outlined rounded color="indigo" @click="login">로그인</v-btn>
        </div>
      </div>
    </form>
    <br>
    <!-- <div>
        <a href='http://localhost:8080/oauth2/authorize/google?redirect_uri="http://localhost:3000/oauth2/redirect"'>
            <div class='socialLogin'>
                <img :src="google.logo" alt="Google" contain height="30%" width="30%"/>
            </div>
        </a>
    </div>-->
  </div>
</template>

<script>
// import { mapGetters } from "vuex";
import axios from "axios";
import { mapMutations } from "vuex";

export default {
  data() {
    return {
      loginData: {
        username: null,
        password: null,
      },
    };
  },
  computed: {
    // ...mapGetters(["isLogIn"]),
  },
  methods: {
    ...mapMutations(["setCookie"]),
    login() {
      axios
        .post(`http://localhost:8000/rest-auth/login/`, this.loginData)
        .then((res) => {
          // console.log(res)
          // console.log(res.config.data);
          this.setCookie(res.data.key);
          this.$router.push("/");
          window.location.reload()
        })
        .catch(error => {
          console.log(error.response)
          alert("이메일 및 비밀번호를 확인해주세요.");
          // console.log(err.response.data.message);
        });
    },
  },
};
</script>

<style scoped>
/* h1 {
  font-size:3rem
  
} */
.divider {
  width: 1px;
  opacity: 0.8;
  background-color: #858f96;
  margin: 0 71px;
  height: 257px;
}
</style>
