<template>
    <div>
        <h3>Click Order</h3>
        <ul>
        <li v-for="(label, index) in clickOrder" :key="index" @dblclick="openDialog(index)">
            {{ index + 1 }}. {{ label }}</li>
        </ul>
        <el-dialog v-model="dialogVisible" title="Edit Label">
            <el-input v-model="inputValue" placeholder="Enter new label"></el-input>
            <span slot="footer" class="dialog-footer">
                <el-button @click="dialogVisible = false">Cancel</el-button>
                <el-button type="primary" @click="updateLabel">Confirm</el-button>
            </span>
            </el-dialog>
    </div>
  </template>
  
<script lang="ts" setup>
import { ref } from 'vue'
import { ElDialog, ElInput, ElButton } from 'element-plus'

const props = defineProps({
    clickOrder: {
        type: Array as () => string[],
        required: true
}
})
const dialogVisible = ref(false)
const inputValue = ref('')
const currentIndex = ref<number | null>(null)
const openDialog = (index: number) => {
    currentIndex.value = index
    inputValue.value = props.clickOrder[index]
    dialogVisible.value = true
}
const updateLabel = () => {
    if (currentIndex.value !== null) {
        props.clickOrder[currentIndex.value] = inputValue.value
        
    }
    dialogVisible.value = false
}

</script>
  
  <style scoped>
  h3 {
    font-size: 1.2rem;
    margin-bottom: 10px;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    margin-bottom: 5px;
  }
  </style>