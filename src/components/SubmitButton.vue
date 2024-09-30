<template>
    <div>
      <!-- <button @click="submitValue">提交</button> -->
      <el-button type="primary" :disabled="isSquareComponentsEmpty" @cick="submitValue">提交</el-button>
    </div>
  </template>
  
<script lang="ts">
import axios from 'axios';
import { defineComponent, ComponentPublicInstance } from 'vue';
import { RootInstance } from '../types/rootInstance';

interface SquareComponent {
  getValue: () => string;
  [key: string]: any; // Allow indexing with string keys
}

interface Value {
  msg: string;
  values: { label: string; value: any }[];
  scriptName?: string;
}

export default defineComponent({
  name: 'SubmitButton',
  data() {
    return {
      submittedValues: [] as string[]
    };
  },
  computed: {
    isSquareComponentsEmpty(): boolean {
      const root = this.$root as ComponentPublicInstance<RootInstance>;
      return root?.squareComponents?.value?.length === 0;
    }
  },
  methods: {
    async submitValue() {
      this.submittedValues = [];
      const root = this.$root as ComponentPublicInstance<RootInstance>;
      const squareComponents = root.$refs as Record<string, SquareComponent[]>;
      const helloWorldMsg = root.helloWorldMsg.value;
      console.log('squareComponents:', squareComponents);
      const values: Value[] = Object.keys(squareComponents)
        .filter(refKey => refKey.startsWith('squareComponent'))
        .map(refKey => {
          const component = squareComponents[refKey][0];
          const inputValueKeys = Object.keys(component).filter(key => key.startsWith('inputValue'));
          return { 
            msg: component.msg, 
            values: inputValueKeys.map(key => ({ label: key, value: component[key] })) 
          };
        });

      // Add HelloWorld message to the values
      values.push({ msg: '', values: [], scriptName: helloWorldMsg });
      console.log('Submitting values:', values);
      try {
        const response = await axios.post('http://47.108.119.224:3000/submit', values, {
          headers: {
            'Content-Type': 'application/json'
          }
        });
        this.submittedValues = response.data.values;
        console.log('Response from /submit:', response.data);
        if (response.data.message === 'Data received successfully') {
          alert('Data received successfully');
          location.reload();
        }
      } catch (error) {
        console.error('Error submitting values:', error);
      }
    }
  }
});
</script>
  
  <style scoped>
  button {
    margin-top: 10px;
    padding: 5px 10px;
    font-size: 1rem;
    cursor: pointer;
  }
  .submitted-value {
    margin-top: 10px;
    font-size: 1rem;
    color: #2c3e50;
  }
  </style>