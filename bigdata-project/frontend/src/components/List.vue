<template>
  <div>
    <!-- <div class="ListContainer">
      <div class="item">
        <div class="Title">네이버</div>
        <img
          src="https://dhgywazgeek0d.cloudfront.net/watcha/image/upload/c_fill,h_700,q_80,w_490/v1597194922/eccgvp8yabjv6hdqpsek.jpg"
          alt
          height="350"
        />
        <div class="ContentInfo">
          <div class="ContentTitle">
            <h6>테넷</h6>
          </div>
          <div class="ContentRating">
            <p>평균★3.9</p>
          </div>
        </div>
      </div>
    </div>-->
    <div class="listcontainer">
      <!-- <h4 class="title">오늘의 웹툰</h4> -->
      <v-sheet class="mx-auto" elevation="" max-width="1200">
        <div>
          <h4 class="title">오늘의 웹툰</h4>
        </div>
        <v-slide-group v-model="model" class="pa-4 group" active-class="success" show-arrows>
          <v-slide-item v-for="n in 15" :key="n" v-slot:default="{ active, toggle }">
            <v-card
              :color="active ? undefined : 'grey lighten-1'"
              class="ma-4"
              height="180"
              width="180"
              @click
            >
              <v-row class="fill-height" align="center" justify="center">
                <v-scale-transition>
                  <v-icon v-if="active" color="white" size="48" v-text="'mdi-close-circle-outline'"></v-icon>
                </v-scale-transition>
              </v-row>
              <div class="contentinfo">
                <p>제목</p>
                <p>평균★9.2</p>
              </div>
            </v-card>
          </v-slide-item>
        </v-slide-group>
      </v-sheet>
    </div>
    <div class="listcontainer">
      <!-- <h4 class="title">네이버</h4> -->
      <v-sheet class="mx-auto" elevation="" max-width="1200">
        <div>
          <h4 class="title">네이버</h4>
        </div>
        <v-slide-group v-model="model" class="pa-4 group" active-class="success" show-arrows>
          <v-slide-item v-for="n in 15" :key="n" v-slot:default="{ active, toggle }">
            <v-card
              :color="active ? undefined : 'grey lighten-1'"
              class="ma-4"
              height="180"
              width="180"
              @click
            >
              <v-row class="fill-height" align="center" justify="center">
                <v-scale-transition>
                  <v-icon v-if="active" color="white" size="48" v-text="'mdi-close-circle-outline'"></v-icon>
                </v-scale-transition>
              </v-row>
              <div class="contentinfo">
                <p>제목</p>
                <p>평균★8.7</p>
              </div>
            </v-card>
          </v-slide-item>
        </v-slide-group>
      </v-sheet>
    </div>
  </div>
</template>

<script>
export default {
  name: "List",
  data: () => {
    return {
      why: "22",
      model: null,
    };
  },
};
</script>

<style>
.title {
  color: #292a32;
  font-size: 22px;
  font-weight: 700;
  text-align: left;
  margin-left: 90px;
  margin-bottom: 0px;
}
.listcontainer {
  color: #292a32;
  margin-top: 8px;
  font-family: Roboto, "Noto Sans KR", sans-serif;
}
.group {
  height: 300px;
}
.contentinfo {
  margin-top: 3px;
  margin-bottom: 0px;
}
p {
  margin-bottom: 0 !important;
}
  
</style>