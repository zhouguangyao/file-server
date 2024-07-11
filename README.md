## 环境配置

conda是一个python版本管理工具，此处省略安装过程。


### 1. 创建项目环境
```bash
conda create --name file-server python=3.9
```
### 2. 切换环境
```bash
conda activate file-server
```

## 运行项目
### 1. 生成依赖文件
```bash
pip freeze > requirements.txt
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```


### 3. 运行
```bash
python app.py
```

## docker运行项目
本地先启动docker，此处省略docker安装、启动过程

### 1. 构建镜像
```bash
docker build -t file-server .
```

### 2. 安装依赖
```bash
docker run -p 5000:5000 file-server
```

## docker部署项目
### 本地
```bash
## 构造镜像：指定linux/amd64
docker build --platform=linux/amd64 -t file-server . 

## 镜像打标签
docker tag file-server registry.cn-beijing.aliyuncs.com/bigdata-common/file-server:0.0.1

## 登陆：只执行一次，需要输入密码
docker login --username=zhouguangyao-rsdt@1450747875273404 registry.cn-beijing.aliyuncs.com

## 推送镜像
docker push registry.cn-beijing.aliyuncs.com/bigdata-common/file-server:0.0.1

```

### 服务器
```bash
## 登陆：只执行一次，需要输入密码
docker login --username=zhouguangyao-rsdt@1450747875273404 registry.cn-beijing.aliyuncs.com

## 拉取镜像
docker pull registry.cn-beijing.aliyuncs.com/bigdata-common/file-server:0.0.1

## 运行：指定端口、绑定挂载
docker run -p 5000:5000 -v /mnt/file-server/uploads/:/mnt/file-server/uploads/ registry.cn-beijing.aliyuncs.com/bigdata-common/file-server:0.0.1
```

## docker-compose部署项目

### 本地
```bash
## 构造镜像：指定linux/amd64
docker build --platform=linux/amd64 -t file-server . 

## 镜像打标签
docker tag file-server registry.cn-beijing.aliyuncs.com/bigdata-common/file-server:0.0.1

## 登陆：只执行一次，需要输入密码
docker login --username=zhouguangyao-rsdt@1450747875273404 registry.cn-beijing.aliyuncs.com

## 推送镜像
docker push registry.cn-beijing.aliyuncs.com/bigdata-common/file-server:0.0.1

```

### 服务器
```bash
## 进入docker-compose.yaml所在目录
cd /mnt/projects/fl-local

## 拉取镜像
docker pull registry.cn-beijing.aliyuncs.com/bigdata-common/file-server:0.0.1

## 停止旧服务
docker compose stop file-server

## 启动新服务
docker compose up -d file-server

```