<template>
  <div>
    <div class="headercontainer">
      <div class="contentheader">
        <header>
          <h3>14</h3>
          <p>이제 알듯 말듯 하네요. 조금만 더 평가해주세요!</p>
        </header>
        <ul class="ul">
          <li class="selectedli">웹툰</li>
          <li>웹소설</li>
          <li>만화</li>
        </ul>
        <div class="sort">
          <div class="sortcontent">
            <img class="dropdown" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGZpbGw9IiNBMEEwQTAiIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTExLjY2MyAxNS44N2wtNS40OTQtNWEuNS41IDAgMCAxIC4zMzctLjg3aDEwLjk4OGEuNS41IDAgMCAxIC4zMzcuODdsLTUuNDk0IDVhLjUuNSAwIDAgMS0uNjc0IDB6Ii8+Cjwvc3ZnPgo=">
            <span>랜덤 웹툰</span>
          </div>
        </div>
      </div>
    </div>
    <section class="tabcontentscontainer">
      <div>
        <section class="contentssection">
          <div class="grid">
            <div class="row">
              <ul class="visualul">
                <li class="contentli" v-for="n in 5">
                  <div class="postercontainer">
                    <div class="loadingimg">
                      <img src="https://dhgywazgeek0d.cloudfront.net/watcha/image/upload/c_fill,h_400,q_80,w_280/v1466061307/polg4nkqbmuuohrjf3wy.jpg" alt="">
                    </div>
                  </div>
                  <div class="detail">
                    <h3 class="title">덤 앤 더머</h3>
                    <div class="information">1994 미국</div>
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </section>
      </div>
    </section>
  </div>
</template>

<script>
export default {
}
</script>

<style>
.body {
  background: rgb(248, 248, 248);
}
.headercontainer {
  top: auto;
  padding: 28px 0px 0px;
  font-family: Roboto, "Noto Sans KR", sans-serif;
}
.contentheader {
  max-width: 640px;
  border: 1px solid rgb(227, 227, 227);
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  margin: 0px auto;
}
.ul {
  list-style: none;
  padding: 0px;
  display: flex;
  margin: 0px 20px;
}
.selectedli {
  display: inline-flex;
  -webkit-box-pack: center;
  justify-content: center;
  -webkit-box-align: center;
  align-items: center;
  color: rgb(255, 47, 110);
  font-size: 15px;
  font-weight: 500;
  letter-spacing: -0.5px;
  line-height: 20px;
  box-sizing: border-box;
  min-width: 48px;
  height: 44px;
  border-bottom: 3px solid rgb(255, 47, 110);
  cursor: pointer;
  flex: 1 1 0%;
  background: rgb(255, 255, 255);
}
.ul li {
  display: inline-flex;
  -webkit-box-pack: center;
  justify-content: center;
  -webkit-box-align: center;
  align-items: center;
  /* color: rgb(255, 47, 110); */
  font-size: 15px;
  font-weight: 500;
  letter-spacing: -0.5px;
  line-height: 20px;
  box-sizing: border-box;
  min-width: 48px;
  height: 44px;
  /* border-bottom: 3px solid rgb(255, 47, 110); */
  cursor: pointer;
  flex: 1 1 0%;
  background: rgb(255, 255, 255);
}
h3 {
  padding-top: 13px;
}
.dropdown {
  width: 24px;
  height: 24px;
}
.sort {
  display: flex;
  -webkit-box-align: center;
  align-items: center;
  background: rgb(251, 251, 251);
  height: 48px;
  border-top: 1px solid rgb(227, 227, 227);
}
.sortcontent {
  margin: 0px 20px;
}
.tabcontentscontainer {
  max-width: 640px;
  border-right: 1px solid rgb(227, 227, 227);
  border-bottom: 1px solid rgb(227, 227, 227);
  border-left: 1px solid rgb(227, 227, 227);
  border-bottom-right-radius: 8px;
  border-bottom-left-radius: 8px;
  margin: auto auto 40px;
}
.contentssection {
  border-bottom-right-radius: 8px;
  border-bottom-left-radius: 8px;
}
.row {
  margin: 0px 20px;
}
.visualul {
  list-style: none;
  padding: 0px;
  margin: 0px;
}
.contentli {
  display: flex;
  -webkit-box-align: center;
  align-items: center;
  padding: 12px 0px;
  border-bottom: 1px solid rgb(237, 237, 237);
}
.postercontainer {
  width: 76px;
  height: 110px;
  margin: 0px 16px 0px 0px;
}
.loadingimg {
  position: relative;
  overflow: hidden;
  box-sizing: border-box;
  border: 1px solid rgba(0, 0, 0, 0.08);
  border-radius: 3px;
  vertical-align: top;
  width: 100%;
  height: 100%;
  background: rgb(248, 248, 248);
  transition: all 300ms ease 0s;
}
.detail {
  flex: 1 1 0%;
  padding: 2px 0px 0px;
}
.title {
  color: rgb(0, 0, 0);
  font-size: 17px;
  letter-spacing: -0.5px;
  line-height: 22px;
  margin: 0px 0px 2px;
  font-weight: normal !important;
}
</style>