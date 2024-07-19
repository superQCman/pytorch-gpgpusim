# pytorch-gpgpusim 安装指引

1. 安装cuda 10.1版本（推荐）
2. 创建Anaconda虚拟环境（python 3.8或2.7）
```shell
cd pytorch-gpgpusim
conda env create -n gpgpu-sim -f ./env.yaml # 3.8可能不兼容的问题更大，如果用3.8遇到进程被killed，建议换成2.7 （./env_2.7.yaml）
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
9. 测试
```shell
# 把配置文件放在同一文件夹下
python ./test_cnn.py > gpgpusim.log
```
10. 备注：
由于该pytorch版本较老，直接跑一些较复杂神经网络会触发各种问题（建议不要调用较新的库，极有可能不兼容）
