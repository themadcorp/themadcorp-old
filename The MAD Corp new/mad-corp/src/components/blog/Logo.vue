<template>
	<g-link class="logo" to="/">
	  <span class="logo__text">
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
.logo {
	text-decoration: none;
  color: var(--body-color)!important;
  font-size: .9em;
	font-family: Montserrat;
  
	&__image {
		vertical-align: middle;
		border-radius: 99px;
		height: 40px;
		width: 40px;
		margin-right: .5em;
	}	
}
</style>