# FigCraft 场景技能

11 个技能与入口，配套 FigCraft Use 开发预发布 `0.1.0-dev.20261018.1`。源码事实源为本仓，插件副本通过 SHA-256 校验。

- figcraft-editor
- figcraft-wireframe
- figcraft-responsive-layout
- figcraft-design-system
- figcraft-prototype-flow
- figcraft-import-fig
- figcraft-dev-handoff
- figcraft-scenario-playbooks
- figcraft-light-dark-token-card
- figcraft-swappable-icon-button
- figcraft-signed-bar-chart

## 界面场景操作手册

新增8条界面设计流程，见 [figcraft-scenario-playbooks](skills/figcraft-scenario-playbooks/SKILL.md)。包含实际返回ID绑定、父子结构、自动布局和独立CLI执行脚本；宿主同步显示验收单独记录。

## main新增能力候选

新增[自动保存与协作成员控制指导](skills/figcraft-scenario-playbooks/references/main-workflows.md)，包括2个新方法和5处契约变化。仅核对固定main真实参数；新增业务、浏览器托管及协作服务器验收未完成。


## 原型真实宿主检查（2026-10-17，开发候选）

已通过隔离的Codex原生插件安装与app-server MCP路由，在Codex内置浏览器执行本仓prototype-flow步骤；实际点击Start→Result→Start。固定main d1d8c3f的Web候选可显示中文；同一会话node.set修改标题及按钮填色后，编辑器和proto.preview实时预览同时变化，原生工程保存成功。没有用独立SDK替代宿主调用。该结论仅覆盖一个合成原型，不是Kimi/ZCode、其他Fig场景或公开市场验收；默认旧内置Web未替换。

真实二进制.fig样例按对象类型核对矢量顶点与画框圆角；原始CLI保留了本样例几何。曾把矢量通用圆角字段当作真实几何导致误报，现已修正检查器并撤回不必要的运行时补丁。该单一样例不代表所有Figma文件完整保真。

## 主题、图标插槽与数据柱图开发候选

新增三个独立技能：`figcraft-light-dark-token-card`（明暗模式、语义别名及CSS/JSON交付）、`figcraft-swappable-icon-button`（实例交换、布尔可见性与独立文字）、`figcraft-signed-bar-chart`（正负零值的可编辑柱图）。固定Figma官方GitHub示例/参考，中文步骤与参数原创。本批为开发预发布，市场安装状态以固定发行与目录仓清单为准；官方0.6.0 macOS完整18记录287次CLI执行通过，三个新场景设置/几何/PNG/SVG、新建及已有文件、输入保护和修改后重开通过；既有原型仅连线持久化，点击仍未验收。Windows完整18记录296次已记录直接CLI调用、140输出摘要通过；真实Codex MCP/IAB执行60个配方步骤并观察主题/按钮/柱图同步，七个实际保存文件独立CLI回读通过。四个独立Python入口在真实Windows的ASCII标准输出/中文路径专项回归均通过；真实业务设计与其他宿主仍未验收。
