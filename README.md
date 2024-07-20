# pytorch-gpgpusim 安装指引

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
# 在pytorch-gpgpusim文件夹外创建一个新文件夹，将test_cnn.py放到新文件夹中（在pytorch-gpgusim目录下运行会报错）
# 先把配置文件放在同一文件夹下，再执行python脚本
python ./test_cnn.py > gpgpusim.log
```

8. 备注：

**由于该pytorch版本较老，直接跑一些较复杂神经网络会触发各种问题（建议不要调用较新的库，极有可能不兼容）**

~~**补充：现在初步推断torchvision可能会触发问题，建议暂时先不使用torchvision**~~
