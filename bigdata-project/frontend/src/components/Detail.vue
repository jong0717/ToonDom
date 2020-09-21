<template>
  <div class="container">
    <div class="d-flex">
      <img
        src="https://shared-comic.pstatic.net/thumb/webtoon/733766/45/thumbnail_202x120_62391051-aaa2-4ff4-8c4d-885243e744b1.jpg"
        alt="toonImg"
        style="height:200px;"
        class="m-2"
      />
      <div class="text-left m-2">
        <h2>인생존망</h2>
        <p class="m-1">
          학교 다닐때 그렇게 놀았으면,
          졸업하고 지금은 불행해야하는거 아니야?
          <br />너 때문에 망한 내인생, 너도 한번 당해봐
        </p>
        <p class="m-1">장르</p>
        <p class="m-1">작가</p>
        <div class="d-flex mt-2">
          <!-- <button class="store"></button> -->

          <button type="button" class="btn btn-primary store m-1">+ 보관하기</button>
          <button type="button" class="btn btn-primary webgo m-1">웹툰 보러가기</button>
          <!-- <v-btn color="blue-lighten-1">+ 보관하기</v-btn> -->
          <div class="ml-4">
            <p class="text-left ml-3 p-0" style="height: 10px; font-size:13px; color:grey;">평가하기</p>
            <!-- <v-rating v-model="rating" background-color="orange lighten-3" color="orange"></v-rating> -->
            <v-rating
              v-model="rating"
              color="yellow darken-3"
              background-color="grey darken-1"
              :empty-icon="emptyIcon"
              :half-icon="halfIcon"
              half-increments
              hover
            ></v-rating>
          </div>
        </div>
      </div>
    </div>
    <div class="comment d-flex justify-content-around align-items-center">
      <p>대단한 작품이군요! 홍순종 님의 감동을 글로 남겨보세요</p>
      <!-- <div class="comment">
            <h3>코멘트 남기기</h3>
      </div>-->
      <!-- <v-btn class="ma-2 cmtBtn" outlined x-large color="black"><span class="btn_content">코멘트 남기기</span></v-btn> -->
      <button type="button" class="ma-2 cmtBtn">
        <span class="btn_content">코멘트 남기기</span>
      </button>
      <!-- <button type="button" class="btn btn-outline-secondary cmtBtn p-0"><span class="btn_content p-0">코멘트 남기기</span></button> -->
      <!-- <v-btn x-large color="success" dark>Extra large Button</v-btn> -->
    </div>
    <div>
      <h4 class="font-weight-bold text-left ml-4">별점 그래프</h4>
      <h6 class="text-right">
        평균
        <v-icon color="black">mdi-star</v-icon>4.4
      </h6>
      <img src="@/assets/img3.jpg" alt />
    </div>
    <v-slide-group v-model="model" class="pa-4" active-class="success" show-arrows>
      <v-slide-item v-for="n in 10" :key="n" v-slot:default="{ active, toggle }">
        <v-card
          :color="active ? undefined : 'grey lighten-1'"
          class="ma-4"
          height="250"
          width="250"
          @click="toggle"
        >
          <v-row class="fill-height" align="center" justify="center">
            <v-scale-transition>
              <v-icon v-if="active" color="white" size="48" v-text="'mdi-close-circle-outline'"></v-icon>
            </v-scale-transition>
          </v-row>
        </v-card>
      </v-slide-item>
    </v-slide-group>
  </div>
</template>

<script>
export default {
  data: () => ({
    rating: 0,
    emptyIcon: "mdi-star-outline",
    halfIcon: "mdi-star-half-full",
    model: null,
  }),
};
</script>

<style scoped>
.store {
  background-color: #42a5f5;
  outline: 0;
  border: 0;
  height: 40px;
}
.webgo {
  background-color: #81c784;
  outline: 0;
  border: 0;
  height: 40px;
}
.comment {
  border: solid 1px gray;
  border-radius: 5px;
  margin-bottom: 20px;
}
.cmtBtn {
  width: 300px;
  outline-color: gray !important;
  border: solid 1px gray;
  border-radius: 5px;
  height: 50px;
}
.btn_content {
  font-size: 20px;
}
</style>