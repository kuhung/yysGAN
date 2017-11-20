# 使用GAN生成新的游戏角色

## 摘要
Generative Adversarial Networks（简称GAN），中文名叫生成对抗网络。我们将使用它，来生成新的游戏角色。

## 依赖 （pip install）

```
cv2
tensorflow( >=1.0)
scipy
numpy
```
## 使用方法

```
cd yysGAN
python yysGAN.py
```

## 训练结果
![image1](https://github.com/kuhung/yysGAN/raw/master/output/epoch4950.jpg)

## 定制你的GAN图片生成模型
```
# 修改input下文件，改为你的jpg素材即可。
```

## 了解更多GAN的知识
查看由Siraj Raval整理的[Generative Adversarial Networks.ipynb](https://github.com/kuhung/yysGAN/blob/master/Generative%20Adversarial%20Networks.ipynb)。

## 参考资料
油管主播Siraj Raval[这里](https://youtu.be/yz6dNf7X7SA)以及原始代码贡献者[moxiegushi](https://github.com/moxiegushi/pokeGAN)。本人仅对resize函数和文件io进行了整理，修正了部分bug，简化了上手难度。

