# xmr-stak-just4cpu

### 说明
基于[xmr-stak](https://github.com/fireice-uk/xmr-stak)项目构建的一个docker镜像, 只用于CPU挖矿, 主要是用于没有GPU的使用度不高的服务器, 争取资源利用最大化.

### 关于xmr-stak的抽成
源码中对于收益的抽成是2%, 这个作者已经在文档中说明了👉 [见此](https://github.com/fireice-uk/xmr-stak#default-developer-donation), 抽成比例的代码在xmr-stak/xmrstak/donate-level.hpp中.

在本镜像中, 已默认将抽成比例修改为0%, 如果你想要给xmr-stak的作者捐献以肯定作者对挖矿事业的贡献的话, 可以在dockerfile中修改抽成比例 👉 修改第11行代码`echo -e "#pragma once \nconstexpr double fDevDonationLevel = 0.0 / 100.0;" > ./xmrstak/donate-level.hpp`中的`0.0/100.0`比例即可, 然后自己构建镜像

### 使用方法
如需使用本镜像请使用docker命令`docker pull vanjaydo/xmr-stak-just4cpu`拉取, 然后使用命令`docker run --rm -it -u $(id -u):$(id -g) --name xmr-stak -v "$PWD":/mnt vanjaydo/xmr-stak-just4cpu`启动容器

具体使用指南与挖矿入门指南请见 👉 [传送门](https://blog.safeandsound.cn/post/MiningGuide.html)