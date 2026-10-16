# 本场景的 Craft 方法与参数

先读取输入与当前选择。数值、路径、名称和对象编号仅为格式示例；用当前输入、实际返回ID和目标尺寸替换后执行。

| 顺序与目的 | 实际方法 | 参数例子与返回值绑定 |
| --- | --- | --- |
| 1. 按真实页面尺寸创建容器 | `node.create` | `{"type":"frame","name":"Desktop","width":1280,"height":1024}` |
| 2. 建立导航区域占位 | `node.create` | `{"type":"rectangle","name":"Navigation","x":0,"y":0,"width":240,"height":1024,"parent":"$frame.id"}；绑定：parent = 第1步实际返回 frame.id；必须替换为真实ID后执行` |
| 3. 建立内容标题 | `node.create` | `{"type":"text","name":"PageTitle","text":"页面目标","x":280,"y":40,"parent":"$frame.id"}；绑定：parent = 第1步实际返回 frame.id；必须替换为真实ID后执行` |

## 如何调用

宿主内已打开编辑器时使用该同会话MCP；先等待editor_status就绪，读取实际工具schema和当前命令参数。独立CLI可用于文件任务，但新进程与已打开Web编辑器不是同一状态。

本插件MCP包装：`run_command`，参数 `{"command": "node.create", "params": {"type": "frame", "name": "Desktop", "width": 1280, "height": 1024}}`。后续行保持同一会话和对象选择，逐条检查实际结果。

CLI 语法（下面是展示用写法，实际跨平台执行用argv避免shell引号差异）：

figcraft-cli run steps.json --in input.figcraft --out output.figcraft；steps.json 是 [{"command":"node.create","params":{"type":"frame","name":"Screen","width":390,"height":884}}]。返回ID用于parent等关联，不能猜测。

## 参数核对与完成标准

先查 [当前版本观察目录](craft-command-evidence.json) 中对应方法的完整参数，再按实际运行时查询更新。结构化步骤见 [craft-steps.json](craft-steps.json)。

页面任务、信息层级和主要操作清楚，按容器结构而非一张平面图交付。

边界：子节点parent应替换为第一步返回frame ID；没有parent时它们会落在页面根级。

保存可编辑工程后由新进程或重新打开的同一宿主会话核对；导出格式单独解码/查看。方法存在和零退出不代表本场景已经完成。

工作流来源与许可见 [workflow-sources.json](workflow-sources.json)。仅借鉴事实与方法，本文与参数例子原创编写。

返回值绑定说明：表中的 `$...` 是待解析参数，不是发送给引擎的字符串。逐步取得真实返回ID后替换，再调用下一步。若实际返回结构不同，先检查结果，不猜ID。
