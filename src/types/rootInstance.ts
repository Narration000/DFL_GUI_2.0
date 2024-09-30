import { Ref } from 'vue';

export interface RootInstance {
  helloWorldMsg: Ref<string>;
  squareComponents: Ref<{ msg: string }[]>;
}