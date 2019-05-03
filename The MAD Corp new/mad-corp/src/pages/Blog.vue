<template>
  <Layout :show-logo="false">
    <!-- Author intro -->
    <Author :show-title="true" />
    
    <!-- 2 column grid -->
    <b-container class="text-center content">
      <b-row v-for="i in Math.ceil($page.posts.edges.length / 2)" :key="i">
        <b-col cols="12" md="6" sm="12" v-for="edge in $page.posts.edges.slice((i - 1) * 2, i * 2)" :key="edge.node.id">
          <PostCard :post="edge.node" />
        </b-col>
      </b-row>
    </b-container>

  </Layout>
</template>

<page-query>
{
  posts: allPost {
    edges {
      node {
        id
        title
        path
        tags {
          id
          title
          path
        }
        date (format: "D. MMMM YYYY")
        timeToRead
        description
        coverImage (width: 770, height: 380, blur: 0)
        ...on Post {
            id
            title
            path
        }
      }
    }
  }
}
</page-query>

<script>
import Author from '~/components/blog/Author.vue'
import PostCard from '~/components/blog/PostCard.vue'

export default {
  components: {
    Author,
    PostCard
  },
  metaInfo: {
    title: 'Blog'
  }
}
</script>
