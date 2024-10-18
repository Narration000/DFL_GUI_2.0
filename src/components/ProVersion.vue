<template>
    <el-row :gutter="200">
      <el-col :span="8"><div class="grid-content ep-bg-purple" /></el-col>
      <el-col :span="8"><div class="grid-content ep-bg-purple-light" /></el-col>
      <el-col :span="8"><div class="grid-content ep-bg-purple" /></el-col>
    </el-row>
  
    <el-row :gutter="200">
      <el-col :span="8">
  
        <DirectoryContainer @node-click-add="handleNodeClick"/>
      </el-col>
      <el-col :span="8">
  
        <!-- <input v-model="helloWorldMsg" placeholder="Enter HelloWorld message" /> -->
        <!-- <HelloWorld :msg="helloWorldMsg"/> -->
        <ClickOrderComponent :clickOrder="clickOrder"/>
        <!-- <SquareComponent v-for="(component, index) in squareComponents" :key="index" :ref="'squareComponent' + index" :msg="component.msg"/> -->
        <!-- <SquareComponent :nodeName="selectedNodeName" /> -->
        <!-- <SubmitButton ref="submitButton"/> -->
        <!-- <SubmitDataButton /> -->
      </el-col>
      <el-col :span="8">
        <FileDisplay />
      </el-col>
    </el-row>
  </template>
  
  <script lang="ts">
  import { defineComponent, ref } from 'vue';
  import HelloWorld from './HelloWorld.vue';
  // import SquareComponent from './components/SquareComponent.vue';
  // import SubmitButton from './components/SubmitButton.vue';
  import FileDisplay from './FileDisplay.vue';
  import DirectoryContainer from './DirectoryContainer.vue';
  import ClickOrderComponent from './ClickOrderComponent.vue';
  import SubmitDataButton from './SubmitDataButton.vue'
  
  
  export default defineComponent({
    name: 'App',
    components: {
      HelloWorld,
      // SquareComponent,
      SubmitDataButton,
      FileDisplay,
      DirectoryContainer,
      ClickOrderComponent
    },
    setup() {
      // const squareComponents = ref<SquareComponentData[]>([]);
      const helloWorldMsg = ref<string>('Welcome to Your Vue.js App');
      const clickOrder = ref<string[]>([]);
  
      const handleNodeClick = (label: string) => {
        clickOrder.value.push(label);
      };
      return {
        // squareComponents,
        helloWorldMsg,
        clickOrder,
        handleNodeClick
      };
    }
  });
  </script>
  
  <style lang="scss">
  .el-row {
    margin-bottom: 20px;
  }
  .el-row:last-child {
    margin-bottom: 0;
  }
  .el-col {
    border-radius: 4px;
  }
  
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .ep-bg-purple {
    background: purple;
  }
  .ep-bg-purple-light {
    background: lightpurple;
  }
  </style> 