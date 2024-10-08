<template>
  <el-input
    v-model="filterText"
    style="width: 240px"
    placeholder="Filter keyword"
  />

  <el-tree
    ref="treeRef"
    style="max-width: 600px"
    class="filter-tree"
    :data="data"
    :props="defaultProps"
    default-expand-all
    :filter-node-method="filterNode"
    v-on:node-click="handleNodeClick"
  />
</template>

<script lang="ts" setup>
import { ref, watch, onMounted } from 'vue'
import { ElTree } from 'element-plus'
import axios from 'axios'

interface Tree {
  [key: string]: any
}

const filterText = ref('')
const treeRef = ref<InstanceType<typeof ElTree>>()
const data = ref<Tree[]>([])
const emits = defineEmits(['node-click-add'])

const defaultProps = {
  children: 'children',
  label: 'label',
}

watch(filterText, (val) => {
  treeRef.value!.filter(val)
})

const filterNode = (value: string, data: Tree) => {
  if (!value) return true
  return data.label.includes(value)
}

const handleNodeClick = (data: Tree) => {
  if (!data.children){
    console.log(data.label)
    emits('node-click-add', data.label)
  }
  
}

onMounted(async () => {
  try {
        const response = await axios.get('http://47.108.119.224:3000/getTreeData');
        data.value = response.data;
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    });
</script>