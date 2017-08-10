## ipDB
##### 根据qqwry自写脚本处理格式化的规范格式ipdb,附送二分法查找ip效率测试代码,非常适合进行大规模ip geo匹配

***

### 文件说明:
##### ipdb: ipDB_0401.txt
##### 二分法效率测试: xIPGeo-tools.py

***

### 截图:
![image](https://github.com/DrizzleRisk/ipDB/blob/master/screen.png)

***

### tips:
##### 1.文件整体加载到内存需要耗费一些时间，但二分法本身效率非常高,在python环境下,100万个随机ip匹配Geo信息,只需要几秒钟
##### 2.关于ipDB,本来我是想做一个类似geoip2的东西用于logstash,但暂时还没有时间做,后续如果有同学有兴趣,我可以把qqwry格式化的脚本也放出来