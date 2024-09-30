<template>
  <div class="square-container">
    <div class="square" @dblclick="toggleEditMode">
      <!-- @blur="checkInput()" @keyup.enter="checkInput()" -->
      <template v-if="isEditing">
        <template v-if="msg === '登录'">
          <div style="width: 60px;">用户名</div>
          <input type="text" v-model="inputValue1" style="background-color: white; color: black; height: 30px; margin-right: 10px;" />
          <div style="width: 60px;">密码</div>
          <input type="text" v-model="inputValue2" style="background-color: white; color: black; height: 30px; margin-right: 10px;" />
        </template>
        <template v-else-if="msg === '转账'">
          <div style="width: 60px;">收款人</div>
            <input type="text" v-model="inputValue1" style="background-color: white; color: black; height: 30px; margin-right: 10px;" />
          <div style="width: 60px;">收款账户</div>
            <input type="text" v-model="inputValue2" style="background-color: white; color: black; height: 30px; margin-right: 10px;" />

        </template>
      </template>
      <template v-else>
        {{ msg }}
      </template>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  props: {
    msg: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      isEditing: false,
      inputValue1: '',
      inputValue2: ''
    };
  },
  methods: {
    toggleEditMode() {
      this.isEditing = !this.isEditing;
      if (this.isEditing) {
        this.inputValue1 = '';
        this.inputValue2 = '';
      }
    },
    checkInput() {
      if (this.inputValue1 !== '' ||  this.inputValue2 !== '--') {
        this.isEditing = true;
      }
      // else if (this.inputValue1 !== '' ||  this.inputValue2 !== '--') {
      //   this.isEditing = false;
      // }
      else {
        this.isEditing = false;
      }
    }
  }
});
</script>

<style scoped>
.square-container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 10px;
}
.square {
  width: 280px;
  height: 60px;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white; /* 设置文字颜色为白色 */
  font-size: 1rem; /* 设置文字大小 */
  font-weight: bold; /* 设置文字加粗 */
  text-align: center; /* 文字居中 */
  background-color: #2c3e50; /* 固定背景颜色 */
}
input {
  width: 100%;
  height: 100%;
  border: none;
  text-align: center;
  font-size: 1rem;
  font-weight: bold;
  color: white;
  background-color: transparent;
}
button {
  margin-top: 10px;
  padding: 5px 10px;
  font-size: 1rem;
  cursor: pointer;
}
.submitted-value {
  margin-top: 10px;
  font-size: 1rem;
  color: #2c3e50;
}
</style>