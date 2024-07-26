[English](./README_en.md)
# pytorch-gpgpusim 安装指引（矩阵相乘问题已解决，涉及矩阵相乘正向传播模块可以运行，由于反向传播需要矩阵和向量相乘，暂时还会报错）

已修改部分：
  1. 重新实现矩阵相乘
  https://github.com/superQCman/pytorch-gpgpusim/blob/de3ce84ce8178e88cc87fea96e4b10661df4cf0d/aten/src/THC/THCBlas.cu#L230
  2. 原本参数传递顺序有问题，修改成正确形式
  https://github.com/superQCman/pytorch-gpgpusim/blob/de3ce84ce8178e88cc87fea96e4b10661df4cf0d/aten/src/THC/THCBlas.cu#L257
  3. [重新实现batch矩阵相乘](https://github.com/superQCman/pytorch-gpgpusim/blob/84d7413cf73c2a2604065adbf7118b729fe82123/aten/src/THC/THCBlas.cu#L457C1-L526C7)

存在问题部分（功能是向量和矩阵相乘）：
  https://github.com/superQCman/pytorch-gpgpusim/blob/de3ce84ce8178e88cc87fea96e4b10661df4cf0d/aten/src/THC/THCBlas.cu#L107
  修改方案：
    1. 打印出传入参数，这个版本参数传递很可能是错的
    2. 重新实现矩阵和向量相乘（使用cuda底层代码很可能报错，且问题难以找到）
    3. 每次运行脚本以及重新编译时间开销较大，希望有能力的能共同解决

## 安装步骤
1. 安装**cuda 10.1**版本（推荐）和 cuDNN （最高版本**v7.6.5**）
2. 创建Anaconda虚拟环境（python 3.6或2.7）
```shell
cd pytorch-gpgpusim
conda create -n gpgpu-sim python=3.6 # 推荐使用3.6
conda activate gpgpu-sim
pip install pyyaml numpy
```
3. 启动编译pytorch-gpgpusim
```shell
git -c submodule."third_party/nervanagpu".update=none submodule update --init # 加载子模块
source set_env.sh # 添加路径，这里最好检查一下路径存在且没问题，确保路径一致
python setup.py install
export PYTORCH_BIN=<pytorch directory>/torch/lib/libcaffe2_gpu.so # Anaconda 中libcaffe2_gpu.so的位置
```
4. 安装torchvision
```shell
pip install torchvision==0.2.2 # 使用torchvision获取数据建议先提前下载下来再运行（版本较老直接运行可能找不到数据）
```
5. 重新编译gpgpusim
```shell
git clone https://github.com/wangeddie67/Chiplet_Heterogeneous_newVersion.git # 如果已经安装过gpgpusim可跳过
cd Chiplet_Heterogeneous_newVersion
source setup_env.sh
cd gpgpu-sim
make -j4
```
6. 验证
```shell
ldd $PYTORCH_BIN
```
若libcudart.so.10.1链接到gpgpu-sim中的libcudart.so.10.1，说明pytorch在执行cuda计算时会使用gpgu-sim。如果没有链接到gpgu-sim，重新执行第5步。

7. 测试
```shell
cd ./benchmarks
make run-main
```

8. 备注：

**由于该pytorch版本较老，直接跑一些较复杂神经网络会触发各种问题（建议不要调用较新的库，极有可能不兼容）**
