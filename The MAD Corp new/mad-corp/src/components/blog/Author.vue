<template>
	<div class="author">

		<g-image alt="Author image" class="author__image" src="~/assets/images/logo.png" width="180" height="180" blur="5" />

		<h1 v-if="showTitle" class="author__site-title">
			{{ $static.metaData.blogName }}
		</h1>

		<p class="author__intro">
			A minimalistic blog for technology💻 business💱 & even algebra📐
		</p>

		<p class="author__links">
			Follow on <a href="//twitter.com/">Twitter</a>
			<a href="//github.com/themadcorp">GitHub</a>
		</p>

	</div>
</template>

<static-query>
query {
  metaData {
    blogName
  }
}
</static-query>

<script>
export default {
	props: ['showTitle']
}
</script>

<style lang="scss">

.author {
	margin: 0 auto;
	max-width: 500px;
	text-align: center;
	padding: calc(var(--space) / 2) 0;

	&__image {
		width: 90px;
		height: 90px;
		margin-bottom: 1em;
	}

	&__intro {
		opacity: .8;
		padding: 10px 20px;
	}

	&__site-title {
		font-size: 2.5em;
		font-family: Montserrat;
		font-weight: 400;
		letter-spacing: 5px;
	}

	&__links {
		margin-top: -.5em;
		a {
			margin: 0 .5em;
		}
	}
}
</style>