import { createMemoryHistory, createRouter } from 'vue-router'

import BaseVersion from './components/BaseVersion.vue'
import AboutView from './components/AboutView.vue'
import ProVersion from './components/ProVersion.vue'


const routes = [
  { path: '/', component: BaseVersion },
  { path: '/about', component: AboutView },
  { path: '/pro', component: ProVersion },
]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
})

export default router