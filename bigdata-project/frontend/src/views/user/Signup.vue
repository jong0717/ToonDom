<template>
  <div>
    <div class="container">
      <h1>가입하기</h1>
      <!-- <router-link to="/login">
        <h6 class="mt-3">로그인하기</h6>
      </router-link> -->
      <form class="col-6 mx-auto">
        <!-- <div class="form-group">
          <v-text-field label="이메일" hide-details="auto" v-model="signupData.email" type="email"></v-text-field>
        </div>-->
        <div class="form-group">
          <v-text-field v-model="signupData.username" label="아이디" hide-details="auto" type="text" />
        </div>
        <div class="form-group">
          <v-text-field
            v-model="signupData.password1"
            label="비밀번호"
            hide-details="auto"
            type="password"
          />
        </div>
        <div class="form-group">
          <v-text-field
            v-model="signupData.password2"
            label="비밀번호 확인"
            hide-details="auto"
            type="password"
          />
        </div>
        <div class="d-flex justify-content-between">
          <div class="d-flex align-items-center">
            <b-form-checkbox
              id="checkbox-1"
              v-model="isTerm"
              name="checkbox-1"
              value="accepted"
            >약관동의</b-form-checkbox>
          </div>
          <v-btn rounded outlined color="indigo" @click="check">가입하기</v-btn>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data: () => {
    return {
      signupData: {
        // email: "",
        username: "",
        password1: "",
        password2: "",
      },
      // isTerm: false,
    };
  },
  methods: {
    // ...mapActions("data", ["signup"]),
    check() {
      let checkList = [
        // this.signupData.email == "",
        this.signupData.username == "",
        this.signupData.password1 == "",
        this.signupData.password1 != this.signupData.password2,
        // !this.isTerm,
      ];
      let checkMessage = [
        // "이메일을 입력",
        "닉네임을 입력",
        "비밀번호를 입력",
        "비밀번호를 확인",
        "약관에 동의",
      ];

      for (let i = 0; i < 4; i++) {
        if (checkList[i]) {
          alert(checkMessage[i] + "해주세요.");
          return;
        }
      }
      this.signup(this.signupData);
    },
    signup() {
      axios
        .post("http://localhost:8000/rest-auth/signup/", this.signupData)
        .then(() => {
          alert("회원가입이 완료되었습니다.");
          this.$router.push("/");
          window.location.reload()
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style>
</style>