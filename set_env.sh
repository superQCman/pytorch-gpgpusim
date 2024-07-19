export LD_LIBRARY_PATH="/usr/local/cuda/lib64/:$LD_LIBRARY_PATH"
#	:/usr/lib/x86_64-linux-gnu/:$LD_LIBRARY_PATH"
export CUDNN_INCLUDE_DIR="/usr/local/cuda-10.1/targets/x86_64-linux/include"
# export CUDNN_LIBRARY="/usr/lib/x86_64-linux-gnu/"
# export CUDNN_LIBRARY=""
export TORCH_CUDA_ARCH_LIST="6.1+PTX"
#	export PYTORCH_BIN=/usr/lib/x86_64-linux-gnu/libcudnn.so
export CUDA_HOME=/usr/local/cuda/
export CUDA_INSTALL_PATH=/usr/local/cuda/
export CUDA_INCLUDE_DIRS=/usr/local/cuda/include/
export CUB_HOME=....
# export PYTORCH_BIN=/home/sim/anaconda3/envs/gpgpu-sim/lib/python2.7/site-packages/torch/lib/libcaffe2_gpu.so
export PATH=/usr/local/cuda/bin:$PATH
