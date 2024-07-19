# pytorch-gpgpusim 安装指引

1. 安装**cuda 10.1**版本（推荐）和 cuDNN （最高版本**v7.6.5**）
2. 创建Anaconda虚拟环境（python 3.8或2.7）
```shell
cd pytorch-gpgpusim
conda env create -n gpgpu-sim -f ./env_2.7.yaml # 如果想用3.8，改成`./env.yaml`。不建议使用3.8，因为可能不兼容的问题更大，如果用3.8遇到进程被kill，建议换成2.7
conda activate gpgpu-sim
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
pip install torchvision==0.2.2
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
# 先把配置文件放在同一文件夹下，再执行python脚本
cd pytorch-gpgpusim
python ./test_cnn.py > gpgpusim.log
```

8. 备注：

**由于该pytorch版本较老，直接跑一些较复杂神经网络会触发各种问题（建议不要调用较新的库，极有可能不兼容）**

**补充：现在初步推断torchvision可能会触发问题，建议暂时先不使用torchvision**
