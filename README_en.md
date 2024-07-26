# pytorch-gpgpusim Installation Guide (Matrix Multiplication Issue Resolved, Forward Pass Now Runs, But Still Errors with Matrix and Vector Multiplication in Backward Pass)

**Modified Sections:**
  1. Reimplemented matrix multiplication
     [View the changes here](https://github.com/superQCman/pytorch-gpgpusim/blob/de3ce84ce8178e88cc87fea96e4b10661df4cf0d/aten/src/THC/THCBlas.cu#L230)
  2. Corrected the order of parameter passing
     [View the changes here](https://github.com/superQCman/pytorch-gpgpusim/blob/de3ce84ce8178e88cc87fea96e4b10661df4cf0d/aten/src/THC/THCBlas.cu#L257)

**Issues (Functionality Involving Vector and Matrix Multiplication):**
  [View the problematic section here](https://github.com/superQCman/pytorch-gpgpusim/blob/de3ce84ce8178e88cc87fea96e4b10661df4cf0d/aten/src/THC/THCBlas.cu#L107)
  **Proposed Solutions:**
    1. Print out the input parameters, as they are likely incorrect in this version
    2. Reimplement matrix and vector multiplication (using CUDA at a low level may cause errors that are hard to trace)
    3. Each script run and recompilation is time-consuming; collaboration is welcomed to solve these issues

## Installation Steps
1. Install **CUDA 10.1** (recommended) and the latest compatible version of cuDNN (**v7.6.5**).
2. Create an Anaconda virtual environment (python 3.6 or 2.7 recommended):
```shell
cd pytorch-gpgpusim
conda create -n gpgpu-sim python=3.6 # Recommended Python version is 3.6
conda activate gpgpu-sim
pip install pyyaml numpy
```
3. Start compiling pytorch-gpgpusim:
```shell
git -c submodule."third_party/nervanagpu".update=none submodule update --init # Load submodules
source set_env.sh # Add paths, check to ensure paths are correct and consistent
python setup.py install
export PYTORCH_BIN=<pytorch directory>/torch/lib/libcaffe2_gpu.so # Location of libcaffe2_gpu.so in Anaconda
```
4. Install torchvision:
```shell
pip install torchvision==0.2.2 # When using torchvision to fetch data, consider downloading the data in advance as older versions may not find the data directly
```
5. Re-compile gpgpusim:
```shell
git clone https://github.com/wangeddie67/Chiplet_Heterogeneous_newVersion.git # Skip if you have already installed gpgpusim
cd Chiplet_Heterogeneous_newVersion
source setup_env.sh
cd gpgpu-sim
make -j4
```
6. Verification:
```shell
ldd $PYTORCH_BIN
```
If libcudart.so.10.1 is linked to gpgpu-sim's libcudart.so.10.1, it indicates that pytorch will use gpgpu-sim for CUDA computations. If not, re-execute step 5.

7. Testing:
```shell
cd ./benchmarks
make run-main
```

8. Remarks:

**As this version of pytorch is outdated, running complex neural networks can trigger various issues (it is advised against using newer libraries which may not be compatible).**
