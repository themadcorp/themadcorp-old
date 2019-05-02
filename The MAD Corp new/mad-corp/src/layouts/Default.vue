<template>
  <div id="app">

    <b-navbar toggleable="lg" type="light" variant="" sticky>
      <b-navbar-brand to="/">The MAD Corp.</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item to="/blog">Blog</b-nav-item>
          <b-nav-item to="/about">About</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    
    <!-- <header class="header">
      <div class="header__left">
        <GoBack v-if="showGoBack" /> 
      </div>
      
      <div class="header__right">        
        <ToggleTheme />
      </div>
    </header> -->

    

    <main class="main">
      <GoBack v-if="showGoBack" />
      <slot :showGoBack="false"/>
    </main>

    <footer class="footer">
      <span class="footer__copyright">Copyright © {{ new Date().getFullYear() }}. </span>
      <span class="footer__links">Powered by <a href="http://www.themadcorp.com"> The MAD Corp </a></span>
    </footer>

  </div>
</template>

<script>
import GoBack from '~/components/blog/GoBack.vue'
import ToggleTheme from '~/components/blog/ToggleTheme.vue'

export default {
  props: {
    showGoBack: { default: false }
  },
  components: {
    GoBack,
    ToggleTheme
  }
}
</script>

<style lang="scss">

@font-face {
    font-family: Montserrat;
    src: url('../assets/montserrat-latin-400.woff');
    font-weight: normal;
  }

@font-face {
    font-family: Noto-sans;
    src: url('../assets/noto-sans-latin-400.woff');
    font-weight: normal;
  }

.navbar {
  background-color: #ffffff;
  box-shadow: 0 2px 10px 0 rgba(0,0,0,.16);
  // height: 70px;

  &-toggler {
    border: none;
  }

  &-toggler:focus {
    border: unset;
  }
}

button:focus {
    outline: none;
}

.main {
  font-family: Montserrat;
  margin: 0 auto;
  padding: 1.5em 15px 0;
}

.footer {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: calc(var(--space) / 2);
  text-align: center;
  font-size: .8em;

  > span {
    margin: 0 .35em;
  }

  a {
    color: currentColor;
  }
}
</style>
