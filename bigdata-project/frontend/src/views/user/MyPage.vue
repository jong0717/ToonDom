<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col mypage p-0">
          <img src="../../assets/img1.jpg" alt="img1" class="MPImg" />
          <div>
            <v-avatar color="cyan lighten-3">
              <v-icon dark>mdi-account-circle</v-icon>
            </v-avatar>
            <h3 class="font-weight-bold">홍순종</h3>
            <h6 class="text-secondary">프로필이 없습니다.</h6>
          </div>
          <div>
            <hr />
            <img src="@/assets/img2.jpeg" alt="img2" class="chartImg" />
            <p class="font-weight-bold">취향분석</p>
            <hr />
          </div>
          <div class="d-flex justify-content-around">
            <div class="webtoon">
              <i class="fas fa-book-open wishitem fa-7x"></i>
            </div>
            <div class="webnovel">
              <i class="fas fa-envelope-open wishitem fa-7x"></i>
            </div>
            <div class="cartoon">
              <i class="fab fa-waze wishitem fa-7x"></i>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Header from "../../components/Header.vue";

export default {
  components: {
    Header,
  },
};
</script>

<style>
.MPImg {
  width: 650px;
  height: 200px;
  border-radius: 5px;
}
.chartImg {
  width: 40px;
  height: 40px;
}
.webtoon {
  width: 192px !important;
  height: 192px !important;
  background: #11998e; /* fallback for old browsers */
  background: -webkit-linear-gradient(
    to right,
    #38ef7d,
    #11998e
  ); /* Chrome 10-25, Safari 5.1-6 */
  background: linear-gradient(
    to right,
    #38ef7d,
    #11998e
  ); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
}
.webnovel {
  width: 192px !important;
  height: 192px !important;
  background: #36d1dc; /* fallback for old browsers */
  background: -webkit-linear-gradient(
    to left,
    #5b86e5,
    #36d1dc
  ); /* Chrome 10-25, Safari 5.1-6 */
  background: linear-gradient(
    to left,
    #5b86e5,
    #36d1dc
  ); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  
}
.cartoon {
  width: 192px !important;
  height: 192px !important;
background: #DCE35B;  /* fallback for old browsers */
background: -webkit-linear-gradient(to right, #45B649, #DCE35B);  /* Chrome 10-25, Safari 5.1-6 */
background: linear-gradient(to right, #45B649, #DCE35B); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */


}
.wishitem {
  opacity: 0.3;
  position: relative;
  left: 20px;
  top: 70px;
}
</style>