# 本场景的 Craft 方法与参数

先读取输入与当前选择。数值、路径、名称和对象编号仅为格式示例；用当前输入、实际返回ID和目标尺寸替换后执行。

| 顺序与目的 | 实际方法 | 参数例子与返回值绑定 |
| --- | --- | --- |
| 1. 创建流程起点画框 | `node.create` | `{"type":"frame","name":"Start","width":390,"height":884}` |
| 2. 创建目标画框 | `node.create` | `{"type":"frame","name":"Result","x":450,"width":390,"height":884}` |
| 3. 在起点框内建立真实按钮热点 | `node.create` | `{"type":"rectangle","name":"Continue","parent":"$start.id","x":24,"y":720,"width":342,"height":48}；绑定：parent = 第1步返回的起点frame ID` |
| 4. 把按钮点击连接到实际目标画框 | `proto.interaction.add` | `{"id":"$button.id","dest":"$result.id"}；绑定：id = 第3步按钮ID；dest = 第2步目标frame ID` |
| 5. 登记明确的原型流程起点 | `proto.flow.add` | `{"start":"$start.id","name":"Main flow"}；绑定：start = 第1步起点frame ID` |
| 6. 打开原型设置面板核对流程起点 | `view.prototype` | `{}` |
| 7. 启动实际演示，再通过当前宿主可用浏览器控制点击按钮验证跳转 | `proto.present` | `{"start":"$start.id"}；绑定：start换成真实起点frame ID；只有实际点击后到达目标frame才完成此场景` |

## 如何调用

宿主内已打开编辑器时使用该同会话MCP；先等待editor_status就绪，读取实际工具schema和当前命令参数。独立CLI可用于文件任务，但新进程与已打开Web编辑器不是同一状态。

本插件MCP包装：`run_command`，参数 `{"command": "node.create", "params": {"type": "frame", "name": "Start", "width": 390, "height": 884}}`。后续行保持同一会话和对象选择，逐条检查实际结果。

CLI 语法（下面是展示用写法，实际跨平台执行用argv避免shell引号差异）：

figcraft-cli run steps.json --in input.figcraft --out output.figcraft；steps.json 是 [{"command":"node.create","params":{"type":"frame","name":"Screen","width":390,"height":884}}]。返回ID用于parent等关联，不能猜测。

## 参数核对与完成标准

先查 [当前版本观察目录](craft-command-evidence.json) 中对应方法的完整参数，再按实际运行时查询更新。结构化步骤见 [craft-steps.json](craft-steps.json)。

从入口实际点击走到目标，核对返回路径、错误态和触发区域。

边界：创建画框不自动建立连线；交互通过node.set interactions当前schema配置，先查返回ID与格式。

保存可编辑工程后由新进程或重新打开的同一宿主会话核对；导出格式单独解码/查看。方法存在和零退出不代表本场景已经完成。

工作流来源与许可见 [workflow-sources.json](workflow-sources.json)。仅借鉴事实与方法，本文与参数例子原创编写。

返回值绑定说明：表中的 `$...` 是待解析参数，不是发送给引擎的字符串。逐步取得真实返回ID后替换，再调用下一步。若实际返回结构不同，先检查结果，不猜ID。

返回值绑定说明：表中的 `$...` 是待解析参数，不是发送给引擎的字符串。逐步取得真实返回ID后替换，再调用下一步。若实际返回结构不同，先检查结果，不猜ID。
