<template>
  <Layout :show-logo="false">
    <!-- Author intro -->
    <Author :show-title="true" />

  </Layout>
</template>

<script>
import Author from '~/components/blog/Author.vue'

export default {
  components: {
    Author
  },
  metaInfo: {
    title: 'Home'
  }
}
</script>
