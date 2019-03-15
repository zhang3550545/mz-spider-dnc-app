## git简单操作命令

在操作之前，需要在电脑上安装git软件，大家可以自行百度

#### git init 初始化一个git项目

```
git init
```

#### git clone git项目地址
```
git clone https://github.com/zhang3550545/mz-spider-dnc-app.git

```

#### git add file_name 将一个新创建的文件添加到git管理

```
git add git简单操作.md
```

#### git commit -m "提交的描述信息"

注意：这里提交的文件，是需要通过git add命令添加到git管理中才能提交

```
git commit -m "提交git简单操作.md文件"
```

#### git pull 拉取git管理中最新的代码

```
git pull
```

#### git push 将commit命令提交的内容，上传到git管理的服务器

```
git push
```

#### git branch 创建分支

test为分支名称

```
git branch test
```

