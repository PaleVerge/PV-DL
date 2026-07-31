# PV-DL

---

<a href="https://wakatime.com/badge/user/33612af3-d9a2-4dd4-8be2-fa5e8944970b/project/54b7f2b0-d628-460b-944e-b0c67fba8f1f"><img src="https://wakatime.com/badge/user/33612af3-d9a2-4dd4-8be2-fa5e8944970b/project/54b7f2b0-d628-460b-944e-b0c67fba8f1f.svg" alt="wakatime"></a>

---

个人深度学习仓库，仅用作备份代码。

## 📚 学习路线

> 以《深度学习入门：基于Python的理论与实现》(鱼书)为主线，逐步过渡到 PyTorch 实战。
> ✅ = 已完成　⬜ = 计划中

### 阶段一：Python 基础与可视化 ✅
- NumPy 数组运算（向量化、广播、布尔索引）
- matplotlib 绘图基础：曲线、图例、坐标轴设置
- 对应目录：`matplotlib/`

### 阶段二：感知机与神经网络入门
- ✅ 感知机：AND / NAND / OR / NOR（权重 + 偏置实现）
- ✅ 多层感知机：XOR（组合单层感知机，体现非线性）
- ✅ 激活函数：阶跃函数、Sigmoid、ReLU（可视化对比）
- ⬜ 损失函数：均方误差、交叉熵误差
- ⬜ 数值微分与梯度（偏导数、梯度计算）
- ⬜ 梯度下降法（SGD）与学习率
- ⬜ 手写两层神经网络：前向传播 / 反向传播
- ⬜ 手写 MNIST 手写数字识别与准确率评估
- 对应目录：`感知机/`、`激活函数/`

### 阶段三：PyTorch 框架实战
- ✅ 张量基础：创建、类型转换、形状操作
- ⬜ autograd 自动求导与计算图
- ⬜ `torch.nn.Module` 搭建模型（线性层、激活、损失）
- ⬜ `DataLoader` 数据加载、批量训练与评估
- ⬜ CNN 卷积神经网络（LeNet / ResNet 实战）
- ⬜ RNN / LSTM 序列建模（文本 / 时间序列）
- ⬜ 迁移学习与模型微调
- 对应目录：`PyTorch/`

### 阶段四：进阶方向（可选）
- ⬜ Transformer 与注意力机制（GPT / BERT 原理）
- ⬜ 生成模型：VAE / GAN / Diffusion
- ⬜ 工程化：ONNX 导出、模型部署与推理加速