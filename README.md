基于Pytest+Allure+Request+Yaml的接口自动化框架，目前还在完善

##项目结构
```text
├── core/                   # 框架核心引擎逻辑
│   ├── assertion/          # 断言引擎
│   ├── engine/             # 核心引擎
│   ├── extract/            # 参数提取
│   ├── loader/             # 用例加载器
│   ├── render/             # 变量渲染
│   ├── runner/             # 用例执行器
│   └── variable/           # 变量池
├── test_cases/             # 测试用例
├── utils/                  # 公用工具
├── .dockerignore           # Docker 忽略配置文件
├── .gitignore              # Git 忽略配置文件
├── Dockerfile              # 容器化构建文件（支持 CI/CD 流程一键镜像打包）
├── docker-compose.yml      # 多容器编排配置（支持一键拉起测试环境与执行依赖）
├── requirements.txt        # 项目依赖包清单（已锁定稳定版本）
├── run.py                  # 框架主入口
└── test_api.py             # 顶层接口集成测试脚本
