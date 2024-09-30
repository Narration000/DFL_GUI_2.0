<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
  </div>
</template>

<<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  props: {
    msg: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      message: 'Hello, World!'
    };
  }
});
</script>

<style scoped>
h1 {
  font-weight: normal;
}
</style>