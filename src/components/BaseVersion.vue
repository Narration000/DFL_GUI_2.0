<template>
    <el-row>
        <el-col :span="12">
            <BaseLogin />
        </el-col>
        <el-col :span="12"><div class="grid-content ep-bg-purple-light" /></el-col>
    </el-row>
</template>

<script setup lang="ts">
import BaseLogin from './BaseLogin.vue';
</script>