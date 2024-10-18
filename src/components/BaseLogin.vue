<template>
    <div style="height: 400px">
        <el-auto-resizer>
            <template #default="{ height, width }">
                <el-table-v2 :columns="columns" :data="data" :width="width" :height="height" fixed>
                    <template #cell="{ column, rowIndex }">
                        <template v-if="column.dataKey === 'actions'">
                            
                                <el-button @click="handleLogin(data[rowIndex])" type="primary">登录</el-button>
                            
                                <el-button type="primary" :icon="Edit" @click="editInfo(rowIndex)" />
                                <el-button type="primary" :icon="Delete" />
                            
                        </template>
                    </template>
                </el-table-v2>
            </template>
        </el-auto-resizer>
        <!-- Dialog for editing information -->
        <el-dialog v-model="dialogVisible" title="Edit Information">
            <el-form :model="form">
                <el-form-item label="nickname">
                    <el-input v-model="form.nickname"></el-input>
                </el-form-item>
                <el-form-item label="Password">
                    <el-input v-model="form.password"></el-input>
                </el-form-item>
            </el-form>
            <span slot="footer" class="dialog-footer">
                <el-button @click="dialogVisible = false">Cancel</el-button>
                <el-button type="primary" @click="submitEdit">Submit</el-button>
            </span>
        </el-dialog>
    </div>

</template>

<script lang="ts" setup>
import { ref, watch } from 'vue';
import { Edit, Delete } from '@element-plus/icons-vue'
import { ElDialog, ElButton, ElForm, ElFormItem, ElInput } from 'element-plus';
import axios from 'axios';


const dialogVisible = ref(false);
const form = ref({
    index: -1,
    account: '',
    nickname: '',
    password: ''
});

const columns = [
    { key: 'nickname', dataKey: 'nickname', title: '昵称', width: 150 },
    { key: 'account', dataKey: 'account', title: '账户', width: 150 },
    { key: 'password', dataKey: 'password', title: '密码', width: 150 },
    { key: 'actions', dataKey: 'actions', title: '操作', width: 150 },
];

// Load data from localStorage or use default data
const storedData = localStorage.getItem('userData');
const data = ref(storedData ? JSON.parse(storedData) : [
    { nickname: '用户1', account: '13055508296', password: 'aaaa1111' },
    { nickname: '用户2', account: 'account2', password: 'password2' },
    { nickname: '用户3', account: 'account3', password: 'password3' },
]);
// const data = ref([
//     { nickname: '用户1', account: '13055508296', password: 'aaaa1111' },
//     { nickname: '用户2', account: 'account2', password: 'password2' },
//     { nickname: '用户3', account: 'account3', password: 'password3' },
// ]);

// Watch for changes in data and save to localStorage
watch(data, (newData) => {
    localStorage.setItem('userData', JSON.stringify(newData));
}, { deep: true });

function handleLogin(row: any) {
    console.log('row:', row);
    const account = row.account;
    const password = row.password;
    axios.post('/api/login', { account, password })
        .then(response => {
            console.log('登录成功:', response.data);
        })
        .catch(error => {
            console.error('登录失败:', error);
        });
}

function editInfo(rowIndex: number) {
    form.value.account = data.value[rowIndex].account;
    form.value.nickname = data.value[rowIndex].nickname;
    form.value.password = data.value[rowIndex].password;
    dialogVisible.value = true;
    console.log('form:', form.value);
    console.log('dialogVisible:', dialogVisible.value);
}

function submitEdit() {
    // Update the data array with the edited information
    console.log('form.value.account:', form.value.account);
    const rowIndex = data.value.findIndex(row => row.account === form.value.account);
    console.log('rowIndex:', rowIndex);
    if (rowIndex !== -1) {
        data.value[rowIndex].nickname = form.value.nickname;
        data.value[rowIndex].password = form.value.password;
        console.log('data[rowIndex]:', data.value[rowIndex]);
    }
    dialogVisible.value = false;
}

</script>