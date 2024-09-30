<!-- <template>
    <div class="directory-container">
      <h3>Directories</h3>
      <ul>
        <li
        v-for="dir in directories"
        :key="dir"
        @dblclick="handleDoubleClick(dir)">
            {{ dir }}
        </li>
      </ul>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent } from 'vue';
  
  export default defineComponent({
    name: 'DirectoryContainer',
    props: {
      directories: {
        type: Array as () => string[],
        required: true
      }
    },
    data() {
      return {
        isHovered: false
      };
    },
    methods: {
      handleDoubleClick(dir: string) {
        this.$emit('directory-dblclick', dir);
      },
      handleMouseOver() {
        this.isHovered = true;
      },
      handleMouseOut() {
        this.isHovered = false;
      }
    }
  });
  </script>
  
  <style scoped>
  .directory-container {
    display: flex;
    flex-direction: column;
    margin-right: 20px;
    text-align: left;
  }
  .directory-container ul {
  list-style-type: none;
  padding: 0;
}

.directory-container li {
  padding: 10px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.directory-container li.hover {
  background-color: #07ccf3;
}

</style> -->

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
  />
</template>

<script lang="ts" setup>
import { ref, watch } from 'vue'
import { ElTree } from 'element-plus'

interface Tree {
  [key: string]: any
}

const filterText = ref('')
const treeRef = ref<InstanceType<typeof ElTree>>()

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

const data: Tree[] = [
  {
    label: '通用功能',
    children: [
      {
        label: '登录',
      },
      {
        label: '点击元素',
      },
      {
        label: '输入验证码',
      }
    ],
  },
  {
    label: 'Level one 2',
    children: [
      {
        label: 'Level two 2-1',
      },
      {
        label: 'Level two 2-2',
      },
    ],
  },
  {
    label: 'Level one 3',
    children: [
      {
        label: 'Level two 3-1',
      },
      {
        label: 'Level two 3-2',
      },
    ],
  },
]
</script>