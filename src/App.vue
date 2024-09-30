<template>
  <!-- <div id="app">
    <div class="main-content">
      <DirectoryContainer :directories="directories" @directory-dblclick="addToSquareComponents" />
      <div class="content">
        <input v-model="helloWorldMsg" placeholder="Enter HelloWorld message" />
        <HelloWorld :msg="helloWorldMsg"/>
        <SquareComponent v-for="(component, index) in squareComponents" :key="index" :ref="'squareComponent' + index" :msg="component.msg"/>
        <SubmitButton ref="submitButton"/>
      </div>
    </div>
    <FileDisplay />
  </div> -->
  
  <el-row :gutter="200">
    <el-col :span="8"><div class="grid-content ep-bg-purple" /></el-col>
    <el-col :span="8"><div class="grid-content ep-bg-purple-light" /></el-col>
    <el-col :span="8"><div class="grid-content ep-bg-purple" /></el-col>
  </el-row>

  <el-row :gutter="200">
    <el-col :span="8">
      <DirectoryContainer :directories="directories" @directory-dblclick="addToSquareComponents" />
    </el-col>
    <el-col :span="8">
      <input v-model="helloWorldMsg" placeholder="Enter HelloWorld message" />
      <HelloWorld :msg="helloWorldMsg"/>
      <SquareComponent v-for="(component, index) in squareComponents" :key="index" :ref="'squareComponent' + index" :msg="component.msg"/>
      <SubmitButton ref="submitButton"/>
    </el-col>
    <el-col :span="8">
      <FileDisplay />
    </el-col>
  </el-row>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import HelloWorld from './components/HelloWorld.vue';
import SquareComponent from './components/SquareComponent.vue';
import SubmitButton from './components/SubmitButton.vue';
import FileDisplay from './components/FileDisplay.vue';
import DirectoryContainer from './components/DirectoryContainer.vue';

interface SquareComponentData {
  msg: string;
}

export default defineComponent({
  name: 'App',
  components: {
    HelloWorld,
    SquareComponent,
    SubmitButton,
    FileDisplay,
    DirectoryContainer
  },
  setup() {
    const directories = ref<string[]>(['登录', '转账']);
    const squareComponents = ref<SquareComponentData[]>([]);
    const helloWorldMsg = ref<string>('Welcome to Your Vue.js App');

    const addToSquareComponents = (dir: string) => {
      squareComponents.value.push({ msg: dir });
    };

    return {
      directories,
      squareComponents,
      helloWorldMsg,
      addToSquareComponents
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

<!-- <style>
#app {
  display: flex;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.main-content {
  display: flex;
  flex-grow: 1;
}
.checkbox-container {
  display: flex;
  flex-direction: column;
  margin-right: 20px;
  margin-right: 200px;
  text-align: left;
}
.content {
  flex-grow: 1;
}
.file-display {
  position: absolute;
  right: 0;
  top: 0;
  width: 200px;
  background-color: #f9f9f9;
  border-left: 1px solid #ddd;
  padding: 10px;
}

.el-row {
  margin-bottom: 20px;
}
.el-row:last-child {
  margin-bottom: 0;
}
.el-col {
  border-radius: 4px;
}
</style> -->
