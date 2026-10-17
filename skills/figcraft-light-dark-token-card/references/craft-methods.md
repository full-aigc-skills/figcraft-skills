# 明暗主题与语义颜色变量卡：CLI/MCP方法

按[具体步骤和参数](craft-steps.json)逐步执行，完整实际枚举在[命令记录](craft-command-evidence.json)。创建动作先查询已有文件与名称，现有内容不可初始化。每个capture均为真实回执：node/instance/collection/variable返回的ID类型不同，原样使用，不拼接或假设为连续数字。

CLI可以使用本技能独立附带的run_recipe.py：以宿主实际技能安装目录定位脚本，使用`--cli`指定已核实的可执行程序，`--output`为不存在的新.figcraft路径，已有输入用`--input`。没有任何其他技能目录依赖；执行器只串行调用原生命令并绑定返回值，不计算业务效果。也可用`figcraft-cli run 命令数组.json --in 原文件 --out 新文件`手动分批，在捕获返回ID后生成下个数组；原生CLI不会解析$ref标记。

插件MCP服务为`figcraft-editor`，先读取实际工具schema：`run_command {"command":"node.get","params":{"id":实际返回ID}}`。该会话的ID与独立CLI文件不同。当前Web支持与否须实际调用核实，不能由原生目录推断。`open_file`/`save_file`按当前schema的path完成同会话可编辑文件交付，`export`只生成派生图；完整文件及PNG/SVG均检查实际写入回执与新路径存在。不要直接假设浏览器虚拟路径等于工作区路径。

背景与文字颜色经真实语义别名和模式继承；修改Dark基础色只改变Dark容器。JSON/CSS保留模式及可用引用，保存重开仍可编辑。

不是直接导入Figma/W3C token；不得把颜色截图当作变量绑定。检查同名集合并选择新任务名，不能覆盖既有品牌变量；示例不代表自动满足对比度规范。

新增节点/组件可能位于画板外作为定义，给已有文件追加时先检查实际空白区域并调整全部相关坐标，保留用户原节点、主组件和变量。原文件摘要不能变化；新文件重开后检查同样的ID关联、值和几何。图层存在或导出成功不代表设计质量、可访问性或Figma兼容性已验收。
