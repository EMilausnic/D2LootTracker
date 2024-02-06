<template>
  <div>
    <h1>Token View</h1>
  </div>
</template>

<script>
export default {
  created() {
    // Call the method to handle the callback
    console.log("I CREATED THE TOKEN PAGE")
    this.handleCallback();
  },
  methods: {
    handleCallback() {
      const urlParams = new URLSearchParams(window.location.search);
      const code = urlParams.get('code');
      console.log(urlParams.get('code'));

      if (code) {
        // Perform authentication logic with the received code
        console.log('Code from URL:', code);
      }
    },
  },
};
</script>

<style>
/* Your component styles here */
</style>