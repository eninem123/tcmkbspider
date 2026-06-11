# 中医药知识库爬虫 📚

基于 Python 的中医药知识服务平台数据爬取工具，自动采集中药、方剂、穴位等中医药知识数据，支持递归深度爬取与多线程并发。

## 功能特性

- **全站递归爬取** - 通过关键词队列深度递归遍历，自动发现新的中医药词汇并爬取
- **多线程并发** - 基于 Queue 的多线程架构，提升爬取效率
- **反爬策略** - 随机 User-Agent 轮换，降低被封禁风险
- **结构化存储** - 数据以 CSV 格式保存，方便后续分析与使用
- **数据清洗** - 包含完整的数据清洗流程与 Hive 处理步骤

## 技术栈

- **语言**: Python 3.x
- **请求库**: requests
- **解析库**: BeautifulSoup, lxml / XPath
- **并发**: threading + Queue
- **数据存储**: CSV

## 项目结构

```
.
├── cnmedicine.py          # 主爬虫程序（类封装版）
├── cnmedicinequeue.py     # 队列版爬虫（多线程）
├── USER_AGENT_LIST.py     # User-Agent 池
├── tcmkbdata.csv          # 爬取结果数据
├── tcmkb2.csv             # 补充数据
├── cleansteps.md          # 数据清洗步骤
├── 测试用.py               # 测试脚本
└── readme.md              # 说明文档
```

## 快速开始

### 安装依赖

```bash
pip install requests beautifulsoup4 lxml
```

### 运行爬虫

**基础版：**
```bash
python cnmedicine.py
```

**队列多线程版：**
```bash
python cnmedicinequeue.py
```

## 数据说明

爬取的数据字段包括：
- 中药名称、别名、性味归经
- 功效主治、用法用量
- 方剂组成、功用主治
- 穴位定位、主治病症
- 等更多中医药相关知识

## 数据清洗

详见 [cleansteps.md](cleansteps.md)，包含完整的 Hive 数据清洗流程：
1. 数据导入 Hive
2. 字段拆分与表结构设计
3. 多维度数据分类
4. 噪声数据清理

## 注意事项

- 本项目仅供学习研究使用，请勿用于商业用途
- 爬取时请遵守目标网站的 robots.txt 协议
- 建议合理控制爬取频率，避免对目标服务器造成压力

## License

MIT License
