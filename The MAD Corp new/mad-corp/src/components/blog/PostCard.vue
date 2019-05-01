<template>
  <div class="card transition">
    <h2 class="transition">{{ post.title }}<br><small class="post-desc">{{ post.description }}</small></h2>
    <div class="cta-container transition"><g-link :to="post.path" class="cta">More</g-link></div>
    <div class="date">{{ post.date }}</div>
    <div class="tags">
      <g-link class="hashtag" v-for="tag in post.tags" :key="tag.id" :to="tag.path">
   			{{ tag.title }}
   		</g-link>
    </div>
    <g-image class="card_circle transition" v-if="post.coverImage" :src="post.coverImage" />
  </div>
</template>

<script>
import PostMeta from '~/components/blog/PostMeta'
import PostTags from '~/components/blog/PostTags'

export default {
  components: {
    PostMeta,
    PostTags
  },
  props: ['post'],
}
</script>


<style>

.transition {
  transition: 0.3s cubic-bezier(0.3, 0, 0, 1.3);
}

.card {
  background-color: #fff;
  height: 400px;
  width: 320px;
  margin: auto;
  margin-bottom: 2.0em;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3);
  overflow: hidden;
  border-radius: 5px;
}

.card:hover {
  box-shadow: 0px 30px 30px rgba(0, 0, 0, 0.2);
  height: 430px;
  width: 333px;
}

.card_circle {
  width: 450px;
  height: 400px;
  object-fit: cover;
  position: absolute;
  border-radius: 50%;
  margin-left: -66px;
  margin-top: -270px;
}

.card:hover .card_circle {
  border-radius: 0;
  margin-top: -130px;
}

h2.transition {
  text-align: center;
  margin-top: 160px;
  padding-left: 12px;
  padding-right: 12px;
  position: absolute;
  z-index: 9;
  font-size: 22px;
  color: #2196f3;
  width: 100%;
  font-family: Noto-Sans;
  font-weight: 700;
}

h2 small.post-desc {
  font-weight: normal;
  font-size: 65%;
  color: rgba(0, 0, 0, 0.5);
}

.card:hover h2 {
  margin-top: 100px;
  color: #fff;
}

.card:hover h2 small.post-desc {
  color: #fff;
}

.cta-container {
  text-align: center;
  margin-top: 290px;
  position: absolute;
  z-index: 9;
  width: 100%;
  font-family: Noto-Sans;
}

.cta {
  color: #fff;
  border: 2px solid #2196f3;
  background-color: #2196f3;
  padding: 5px 25px;
  border-radius: 50px;
  font-size: 0.8em;
  text-decoration: none;
  font-weight: bold;
}

.card:hover .cta-container {
  margin-top: 320px;
}

a:hover {
  text-decoration: none;
}

.date {
  position: absolute;
  bottom: 15px;
  left: 20px;
  z-index: 10;
  font-family: Noto-Sans;
  color: grey;
  font-size: 15px;
}

.tags {
  display: flex;
  position: absolute;
  right: 10px;
  bottom: 15px;
}

.hashtag {
  font-family: Noto-Sans;
  font-size: 10px;
  background: rgba(180, 180, 180, 0.5);
  border-radius: 0.3rem;
  padding: 0.2em 0.6em;
  margin-right: 0.5em;
  z-index: 10;
  font-weight: 600;
  color: #505050;
}

</style>