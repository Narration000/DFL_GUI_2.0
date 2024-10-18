<template>
  <div>
    <input v-model="helloWorldMsg" placeholder="Enter HelloWorld message" />
    <div class="hello">
      <h1>{{ helloWorldMsg }}</h1>
    </div>

    <h3>Click Order</h3>
    <ul>
      <li v-for="(label, index) in clickOrder" :key="index" @dblclick="openDialog(index)">
        {{ index + 1 }}. {{ label }}
      </li>
    </ul>
    <!-- 对话框 -->
    <el-dialog v-model="dialogVisible" @close="closeDialog" title="Edit Key-Value Pairs">

      <el-table :data="tableData" style="width: 100%" max-height="250">
        <el-table-column prop="id" label="ID" width="150" />
        <el-table-column prop="key" label="Key" width="150">
          <template #default="scope">
            <el-input v-model="scope.row.key" placeholder="Please input" />
          </template>
        </el-table-column>
        <el-table-column prop="value" label="Value" min-width="120">
          <template #default="scope">
            <el-input v-model="scope.row.value" placeholder="Please input" />
          </template>
        </el-table-column>
        <el-table-column fixed="right" label="Operations" width="120">
          <!-- 删除按钮 -->
          <template #default="scope">
            <el-button link type="primary" size="small" @click.prevent="deleteRow(scope.$index)">
              Remove
            </el-button>
          </template>
        </el-table-column>
      </el-table>
      <!-- 添加按钮 -->
      <el-button class="mt-4" style="width: 100%" @click="onAddItem">Add Item</el-button>
      <!-- 确认和取消按钮 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">Cancel</el-button>
        <el-button type="primary" @click="closeDialog">Confirm</el-button>
      </span>

    </el-dialog>
    <el-button type="primary" @click="submitData">Submit Data</el-button>
    <!-- 删除元素 -->
    <!-- <el-button @click="deleteClickOrderElement">Delete ClickOrder Element</el-button> -->
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import axios from 'axios';
import { ElDialog, ElTable, ElTableColumn, ElInput, ElButton } from 'element-plus'

const props = defineProps({
  clickOrder: {
    type: Array as () => { label: string, key: string, value: string }[],
    required: true
  }
})

const helloWorldMsg = ref<string>('Welcome to Your Vue.js App');

const dialogVisible = ref(false)
const tableData = ref<{ id: number; key: string; value: string }[]>([])
const currentIndex = ref<number | null>(null)
const jsonData = ref<{ [key: number]: { id: number; key: string; value: string }[] }>({})
const jsonDataString = ref<string>('')

const openDialog = (index: number) => {
  currentIndex.value = index
  dialogVisible.value = true
  // Initialize table data with the current item's data from jsonData
  // tableData.value = jsonData.value[index] || props.clickOrder.map((item, idx) => ({
  //   id: idx + 1,
  //   key: item.key,
  //   value: item.value
  // }))
  tableData.value = jsonData.value[index] || [{ id: 1, key: '', value: '' }];
  console.log('tableData:', tableData.value)
}

const closeDialog = () => {
  saveData();
  dialogVisible.value = false;
}

const onAddItem = () => {
  const newItem = { id: tableData.value.length + 1, key: '', value: '' }
  tableData.value.push(newItem)
}

const deleteRow = (index: number) => {
  tableData.value.splice(index, 1)
}

const saveData = () => {
  if (currentIndex.value !== null) {
    jsonData.value[currentIndex.value] = tableData.value
  }
  const dataToSave = {
    clickOrder: props.clickOrder,
    tableData: jsonData.value
  }
  jsonDataString.value = JSON.stringify(dataToSave)
  console.log('dataToSave:', dataToSave)
  console.log('jsonDataString:', jsonDataString.value) // Replace this with actual save logic
  dialogVisible.value = false
}

// const deleteClickOrderElement = () => {
//   if (currentIndex.value !== null) {
//     props.clickOrder.splice(currentIndex.value, 1);
//     currentIndex.value = null;
//     dialogVisible.value = false;
//   }
// };

const submitData = async () => {
  try {
    const dataToSend = {
      scriptName: helloWorldMsg.value,
      jsonDataString: jsonDataString.value
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



// HelloWorld.vue
// const msg = ref('Welcome to Your Vue.js App')
// const helloWorldMsg = ref<string>('Welcome to Your Vue.js App');
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

/* HelloWorld.vue styles */
.hello h1 {
  font-weight: normal;
}
</style>