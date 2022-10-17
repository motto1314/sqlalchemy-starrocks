### superset使用方法

下载该源码：
```
git clone ...
```

安装(如果是superset docker，使用root用户安装)：
```
pip install .
```

在superset中选择使用Other数据源，并配置：
```
starrocks://root:@x.x.x.x:9030/superset_db
```
