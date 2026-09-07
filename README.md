# 云南旅行攻略系统

## 文件结构

```
yunnan-trip-2026/
├── index.html                    # 主页面
├── travel-guides.yaml            # 攻略配置文件
├── scripts/
│   └── yaml-to-html.py          # 转换脚本
└── README.md                     # 本文件
```

## 使用说明

### 1. 编辑攻略

编辑 `travel-guides.yaml` 文件，格式如下：

```yaml
guides:
  - id: "unique-id"
    day: 1  # 天数（0=通用攻略）
    location: "地点名称"
    type: "美食"  # 美食/景点/交通/攻略
    source: "user"  # user=用户收藏, search=搜索发现
    title: "攻略标题"
    url: "https://www.xiaohongshu.com/explore/xxx"  # PC链接
    short_url: "https://xhslink.cn/o/xxx"  # 手机短链接（可选）
    summary: "摘要"
    stats:
      likes: 1000  # 点赞数（可选）
      collects: 500  # 收藏数（可选）
      comments: 50  # 评论数（可选）
    highlights:
      - "亮点1"
      - "亮点2"
    tips: "实用建议"
    tags: ["标签1", "标签2"]
```

### 2. 生成HTML

运行转换脚本：

```bash
python scripts/yaml-to-html.py
```

脚本会：
- 读取 `travel-guides.yaml`
- 生成每日攻略卡片（紧凑版）
- 生成攻略汇总卡片（详细版）
- 更新 `index.html`

### 3. 查看效果

打开 `index.html`，攻略会显示在：
- 每个Day卡片的底部（点击"📖 攻略推荐"展开）
- 页面底部的"📱 小红书热门攻略"区域

## 链接说明

- **PC链接**：完整的小红书链接，PC端可直接访问
- **手机短链接**：`xhslink.cn` 短链接，手机端更友好
- **显示逻辑**：
  - PC端显示"📕 PC查看"按钮
  - 手机端显示"📱 手机打开"按钮

## 自适应显示

- **少量攻略（≤3条）**：全部显示
- **多量攻略（>3条）**：按地点分组，每组最多显示2条
- **攻略汇总**：按天分组，按地点分类，卡片网格布局

## 攻略数据

当前收录：
- 用户收藏：8篇
- 搜索发现：38篇
- **总计：46篇**

覆盖地点：
- Day1：篆新市场、昆明站附近、大理古城
- Day2：洱海日出、忠义市场、丽江古城
- Day3：甘海子、蓝月谷、白沙古镇、束河古镇
- Day4：虎跳峡、白水台、纳帕海、独克宗古城
- Day5：松赞林寺、拉姆央措湖、纳帕海环湖

## 更新日志

- 2026-09-07：创建攻略系统，收录46篇攻略
