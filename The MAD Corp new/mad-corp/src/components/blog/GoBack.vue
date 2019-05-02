<template>
	<g-link class="goBack" to="/blog">
	  <span class="goBack__text">
	    &larr; {{ $static.metaData.blogName }}
	  </span>
	</g-link>
</template>

<static-query>
query {
  metaData {
    blogName
  }
}
</static-query>

<style lang="scss">
.goBack {
	text-decoration: none;
  color: var(--body-color)!important;
  font-size: .9em;
	font-family: Montserrat;
  
	&__text {
		margin: 0 10px 20px 10px;
		display: inline-block;
	}

	&__image {
		vertical-align: middle;
		border-radius: 99px;
		height: 40px;
		width: 40px;
		margin-right: .5em;
	}	
}
</style>