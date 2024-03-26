<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
    <h1 style="font-family: monospace;font-size: xxx-large;color: snow;">
      Destiny 2 Loot Pool Guide
    </h1>
    
  <RouterView />
</template>

<style scoped>
#app {
  width: auto !important;
  max-width: auto !important;

}
header {
  line-height: 1.5;
  max-height: 100vh;
  background-color: blueviolet;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

</style>
