<template>
  <Layout>
    <div class="content">
      <GoBack v-if="showGoBack" />
      <br>
      <h1 class="tag-title text-center space-bottom">
        # {{ $page.tag.title }}
      </h1>

      <div class="posts">
        <PostCard v-for="edge in $page.tag.belongsTo.edges" :key="edge.node.id" :post="edge.node"/>
      </div>
    </div>
  </Layout>
</template>

<page-query>
query Tag ($id: String!) {
  tag (id: $id) {
    title
    belongsTo {
      edges {
        node {
          ...on Post {
            title
            path
            date (format: "D. MMMM YYYY")
            timeToRead
            description
            coverImage (width: 860, blur: 10)
            content
          }
        }
      }
    }
  }
}
</page-query>

<script>
import Author from '~/components/blog/Author.vue'
import PostCard from '~/components/blog/PostCard.vue'
import GoBack from '~/components/blog/GoBack.vue'

export default {
  components: {
    Author,
    PostCard,
    GoBack
  },
  props: {
    showGoBack: { default: true }
  },
  metaInfo: {
    title: 'Hello, world!'
  }
}
</script>

<style lang="scss">
  
</style>
