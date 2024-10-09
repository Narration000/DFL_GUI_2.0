<template>
    <el-button type="primary" @click="submitData">Submit Data</el-button>
</template>
  
<script lang="ts" setup>
import axios from 'axios';
// import helloWorldMsg from '../App.vue';
import { Ref } from 'vue';

export interface RootInstance {
  helloWorldMsg: Ref<string>;
  squareComponents: Ref<{ msg: string }[]>;
}
const props = defineProps({
  jsonDataString: {
    type: String,
    required: true
  }
});
const submitData = async () => {
  try {
    const dataToSend = {
      jsonDataString: props.jsonDataString
    }
    // console.log('helloWorldMsg:', helloWorldMsg.value)
    console.log('Data to send:', dataToSend)
    const response = await axios.post('http://47.108.119.224:3000/submitData', dataToSend, {
    headers: {
      'Content-Type': 'application/json'
    }
  })
    console.log('Data submitted successfully:', response.data)
  } catch (error) {
    console.error('Error submitting data:', error)
  }
}
</script>
  
  <style scoped>
  .el-button {
    margin-top: 20px;
  }
  </style>