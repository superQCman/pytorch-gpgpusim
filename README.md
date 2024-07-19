# pytorch-gpgpusim 安装指引

1. 安装cuda 10.1版本（推荐）
2. 创建Anaconda虚拟环境（python 3.8）
```shell
cd pytorch-gpgpusim
conda env create -n gpgpu-sim -f ./env.yaml
```
4. 启动编译pytorch-gpgpusim
```shell
source set_env.sh #这里最好检查一下路径存在且没问题，确保
python setup.py install
export PYTORCH_BIN=<pytorch directory>/torch/lib/libcaffe2_gpu.so #anaconda 中的位置
```
5. 安装torchvision
```shell
pip install torchvision==0.2.2
```
6. 启动gpgpu-sim
7. 验证
```shell
ldd $PYTORCH_BIN
```
若libcudart.so.10.1链接到gpgpu-sim中的libcudart.so.10.1，说明pytorch在执行cuda计算时会使用gpgu-sim。
8. 备注：
由于该pytorch版本较老，直接跑一些较复杂神经网络会触发各种问题（尤其从外界读取数据，建议先随机在python中设置数据）
