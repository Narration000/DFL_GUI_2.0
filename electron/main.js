// main.js
// 控制应用生命周期和创建原生浏览器窗口的模组
// app 模块，它控制应用程序的事件生命周期。
// BrowserWindow 模块，它创建和管理应用程序窗口。
const { app, BrowserWindow } = require('electron');
const path = require('path')
  // 打开窗口
function createWindow () {
  const mainWindow = new BrowserWindow({
    width: 2048, // 窗口的宽度
    height: 1080, // 窗口的高度
    // 网页功能设置
    webPreferences: {
      nodeIntegration: true,  // 是否启用Node integration. 默认值为 false.
      contextIsolation: false, // 是否在独立 JavaScript 环境中运行 electron API和指定的preload 脚本. 默认为 true
      enableRemoteModule: true,  // 启用或远程模块, 默认为 true
      preload: path.join(__dirname, 'preload.js'), // 使用预加载脚
    },
    autoHideMenuBar: true, // 窗口菜单栏是否自动隐藏，默认false
  }) 
  // 通过改变变量值来控制加载的文件，dev 或者build时修改env值。
  let env = 'pro';
  // 配置热更新
  if (env == 'pro') {
    const elePath = path.join(__dirname, '../node_modules/electron')
    require('electron-reload')('./', {
      electron: require(elePath),
    })
    // 热更新监听窗口，这里是vue启动时的地址
    mainWindow.loadURL('http://localhost:5173')
    // 打开开发工具
    mainWindow.webContents.openDevTools()
  } else {
    // 生产环境中要加载文件 index.html
    mainWindow.loadFile(path.resolve(__dirname, '../dist/index.html'))
  }
}
 
// 这段程序将会在 electron 结束初始化和创建浏览器窗口的时候调用
app.whenReady().then(() => {
  createWindow()
  app.on('activate', function () {
    // 如果没有其他打开的窗口，那么程序会重新创建一个窗口。
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})
 
// 当所有窗口都被关闭的时候退出程序。
app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit()
})
