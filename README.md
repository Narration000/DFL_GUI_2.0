# DFL_GUI

## 解决依赖
```
npm install electron-builder --save-dev

npm cache clean --force
rm -rf node_modules
npm install
```

### 启动
- 启动vue3
```
npm run dev
```
- 启动本地API端口服务（文件读取、脚本执行）
```
npm run start-server
```
- 启动客户端
```
npm run dev
npm run electron:serve
```

### 打包
```
npm run build
npm run electron:build

### Compiles and hot-reloads for development
```
npm run serve
```
or
```
npm run electron:serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
