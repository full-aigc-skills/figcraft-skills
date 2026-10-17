# FigCraft 场景技能

7 个本地未发布候选；配套 FigCraft Use 插件。源码事实源为本仓，插件副本通过 SHA-256 校验。

- figcraft-editor
- figcraft-wireframe
- figcraft-responsive-layout
- figcraft-design-system
- figcraft-prototype-flow
- figcraft-import-fig
- figcraft-dev-handoff

## 界面场景操作手册

新增8条界面设计流程，见 [figcraft-scenario-playbooks](skills/figcraft-scenario-playbooks/SKILL.md)。包含实际返回ID绑定、父子结构、自动布局和独立CLI执行脚本；宿主同步显示验收单独记录。

## main新增能力候选

新增[自动保存与协作成员控制指导](skills/figcraft-scenario-playbooks/references/main-workflows.md)，包括2个新方法和5处契约变化。仅核对固定main真实参数；新增业务、浏览器托管及协作服务器验收未完成。


## 原型真实宿主检查（2026-10-17，开发候选）

已通过隔离的Codex原生插件安装与app-server MCP路由，在Codex内置浏览器执行本仓prototype-flow步骤；实际点击Start→Result→Start。固定main d1d8c3f的Web候选可显示中文；同一会话node.set修改标题及按钮填色后，编辑器和proto.preview实时预览同时变化，原生工程保存成功。没有用独立SDK替代宿主调用。该结论仅覆盖一个合成原型，不是Kimi/ZCode、其他Fig场景或公开市场验收；默认旧内置Web未替换。

真实二进制.fig样例还暴露了原始CLI的独立圆角丢失（warnings为空）；插件候选新增构建补丁，相关Windows构建与业务结果另见目录仓回归记录，不据原型通过推断导入保真。
