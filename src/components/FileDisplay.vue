<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'FileDisplay',
  data() {
    return {
      pythonFiles: [] as string[]
    };
  },
  mounted() {
    this.fetchPythonFiles();
  },
  methods: {
    async fetchPythonFiles() {
      try {
        const response = await fetch('/api/python-files');
        const files = await response.json();
        console.log('Python files fetched:', files);
        this.pythonFiles = files
          .filter((file: string) => file !== 'automation_steps.py');
        // .map(file => file.slice(file.lastIndexOf('_') + 1));
      } catch (error) {
        console.error('Error fetching Python files:', error);
      }
    },
    async runPythonFile(file: string) {
      try {
        const response = await fetch(`/api/run-python-file?file=${file}`, {
          method: 'POST'
        });
        const result = await response.json();
        console.log('Python file executed:', result);
      } catch (error) {
        console.error('Error running Python file:', error);
      }
    }
  }
});
</script>

<template>
  <div class="file-display">
    <h3>Python Scripts</h3>
    <button @click="fetchPythonFiles">Refresh</button>
    <ul>
      <li v-for="file in pythonFiles" :key="file">
        {{ file }}
        <button @click="runPythonFile(file)">
          Run
        </button>
      </li>
    </ul>
  </div>
</template>


<style>
.file-display {
  right: 0;
  top: 0;
  width: 300px;
  background-color: #f9f9f9;
}

.file-display li {
  text-align: left;
  /* Left align the text */
  padding: 5px 0;
  /* Add some padding for better readability */
}
</style>