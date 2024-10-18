<template>
  <div class="common-layout">
    <el-container>
      <el-header class="fixed-header">
        <el-row>
          <el-col :span="2">
            <RouterLink to="/">
              <el-button>Go to Base</el-button>
            </RouterLink>
          </el-col>
          <el-col :span="2">
            <RouterLink to="/pro">
              <el-button>Go to Pro</el-button>
            </RouterLink>            
          </el-col>
          <el-col :span="20"><div class="grid-content" /></el-col>
        </el-row>

        


      </el-header>
      <el-main class="fixed-main">
        <RouterView />
      </el-main>
    </el-container>
  </div>
</template>

