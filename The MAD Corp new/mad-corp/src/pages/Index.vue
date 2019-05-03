<template>
  <Layout>
    <div id="parallax-container">
      <div id="parallax-0"></div>
      <div id="parallax-1"></div>
      <div id="parallax-2"></div>
      <div id="parallax-3"></div>
      <div id="parallax-4"></div>
    </div>

    <div id="content">
      <b-container>
        <h1 class="hero">The MAD Corp.</h1>
        <p class="hero">Innovation & Technology Company.</p>
        <br>

        <!-- About section -->
        <h2>About</h2>
        <p>
          We're are an Innovation & Technology Company. Driven by the idea of conquering the world, 
          we intend to change the world in a better way through Technology & Science.
          The MAD Corp. has been established with the motive of delivering the most Creative 
          and Eminent Innovations to all the inhabitants of this planet. <br>
        </p>
        <p>
          We believe in <strong>Innovating Together</strong>!
        </p>

        <!-- Team Section -->

      </b-container>
    </div>
  </Layout>
</template>

<script>
export default {
  components: {},
  metaInfo: {
    title: "Home"
  },
  mounted() {
    window.addEventListener('scroll', () => {
        let parent =  document.getElementById('parallax-container');
        let children = parent.getElementsByTagName('div');
        for(let i = 0; i < children.length; i++) {
          children[i].style.transform = 'translateY(-' + (window.pageYOffset * 1.58 * i / children.length) + 'px)';
        }
      }, false)
  }
};
</script>

<style>

#parallax-container {
  display: block;
  height: 1000px;
}

#parallax-container div {
  position: fixed;
  top: 0;
  background-position: center !important;
  transform: translateY(0px);
  height: 570px;
  width: 100%;
  background-size: cover;
}

#parallax-0 {
  background-image: url('./../assets/images/parallax/background.png');
  position: absolute !important;
}

#parallax-1 {
  background-image: url('./../assets/images/parallax/stars.png');
}

#parallax-2 {
  background-image: url('./../assets/images/parallax/pink-smoke.png');
}

#parallax-3 {
  background-image: url('./../assets/images/parallax/white-smoke.png');
}

#parallax-4 {
  background-image: url('./../assets/images/parallax/rocket.png');
}

#content {
  display: block;
  position: relative;
  background-color: #F9FBFC;
  margin-top: -580px;
  padding-top: 10px;
  padding-bottom: 100px;
  text-align: justify;
}

#content h1.hero {
  text-align: center;
  font-family: Montserrat, 'sans-serif';
  font-size: 48px;
  font-weight: 400;
  letter-spacing: 10px;
  margin-bottom: 0.3em;
}

#content p {
  line-height: 1.8em;
}

#content p.hero {
  text-align: center;
  font-size: 18px;
  font-family: Montserrat, 'sans-serif';
}

#content .container {
  padding: 10px 30px ;
}

#content h2 {
  font-family: Montserrat, 'sans-serif';
  font-weight: 500;
}
</style>
