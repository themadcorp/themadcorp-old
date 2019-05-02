<template>
  <section class="page_404">
    <div class="container">
      <b-row>
        <b-col sm="12">
          <b-col class="text-center .mx-auto" sm="12">
            <div class="four_zero_four_bg">
              <h1 class="text-center">404</h1>
            </div>

            <div class="contant_box_404">
              <h3 class="h2">Looks like you're lost</h3>

              <p>the page you are looking for not avaible!</p>

              <g-link to="/" class="link_404">Go to Home</g-link>
            </div>
          </b-col>
        </b-col>
      </b-row>
    </div>
  </section>
</template>

<style>
.page_404 {
  padding: 20px 0;
  background: #fff;
  font-family: Montserrat;
}

.page_404 img {
  width: 100%;
}

.four_zero_four_bg {
  background-image: url('./../assets/images/404.gif');
  height: 400px;
  background-position: center;
}

.four_zero_four_bg h1 {
  font-size: 80px;
  font-family: Montserrat;
}

.four_zero_four_bg h3 {
  font-size: 80px;
  font-family: Noto-sans;
}

.link_404 {
  color: #fff !important;
  padding: 10px 20px;
  background: #39ac31;
  margin: 20px 0;
  display: inline-block;
  border-radius: 5px;
}
.contant_box_404 {
  margin-top: -50px;
}
</style>
