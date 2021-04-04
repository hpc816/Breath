## 个人任务清单

#### TODO-LIST

- 仓库同步问题：这两项修改不涉及核心代码部分，不要同步到仓库，同步了之后反而会让其他成员需要重新配置pycharm![image-20210404172224095](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210404172224095.png)





- 1.spafe似乎对音频信号的采样率有特殊的要求，现在只有设置sr=16000程序才能跑通，考虑调整代码，使得使用原始采样率时也不会报错



- 2.每次都需要提取特征比较费时间，对内存和CPU消耗也比较大，考虑将音频的特征矩阵提取之后保存





- 3.**预测时对每个用户只使用到了User Model， Others Model还未完成部署**，后续相关预测操作也没实现
  - Other Model训练部分：目前运行起来没啥问题![image-20210404155940765](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210404155940765.png)
  - 预测部分：
    - **未逐帧比较，仅比较特征向量作为整体输入，若Target User Model得分>Other User Model 得分，则认为认证通过：**
      - 效果：比单纯的预测准确率要高了![image-20210404164535605](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210404164535605.png)
    - **逐帧比较，计算每一帧Log(LLuser/LLother)，而后求均值**
      - 效果：验证准确率反而不如上面的![image-20210404171229255](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210404171229255.png)
    - 尝试修改，每次输入相邻两个帧的特征向量：效果还是不太好
      - 效果：![image-20210404171631423](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210404171631423.png)





- 4.GMM模型超参数中的**高斯分布数目最优值**还需要通过**实验或者细读论文**得到



- 5.实现求GFCC的一阶微分和二阶微分，并和原始GFCC特征向量拼接在一起构成96维特征向量



#### 论文BreathPrint复现：

- Segmentation Algorithm: ![image-20210404144839270](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210404144839270.png)
  
  - 待定
  - 自己实现了一个refine.py，效果如下：![image-20210404144756847](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210404144756847.png)
    - 问题：处理时间过长，用户体验不好
  
- **特征提取：**

  - 论文：使用**32维GFCC特征，及其一阶微分和二阶微分**，最后使用**96维的特征向量作为分类器的输入**
    - 选用GFCC而不是MFCC的原因：GFCC在低频段部分比MFCC分辨率高，使得GFCC能更好的适应环境噪声、更好的检测低频声音
  - 复现：综合考虑多种语音特征，如MFCC、GFCC、PLP
    - 现有成果：使用spafe、librosa、python_speech_feature库实现了特征提取
    - **现存问题：**
      - **1.spafe似乎对音频信号的采样率有特殊的要求，现在只有设置sr=16000程序才能跑通**，考虑调整代码，使得使用原始采样率时也不会报错
      - **2.librosa提取的特征放入分类器中会直接报错..**
      - **3.GFCC的一阶微分和二阶微分部分还没实现**
      - **4.每次都需要提取特征比较费时间，对内存和CPU消耗也比较大，考虑将音频的特征矩阵提取之后保存**

- **分类器：**

  - 论文：使用了GMM、DTW和SVM模型，最后发现GMM表现最好
    - **GMM模型超参数**：
      - **高斯分布数目**：尝试了5、10、15、20、25、30，当30+时，分类准确率会快速下降到50%以下【可能是数据量较少的原因】
      - **协方差矩阵类型：实验和经验都指示diagonal效果最好**
  - 复现：
    - 现有成果：
      - 初步实现了GMM模型中User Model的部署
        - 高斯分布数目：32
        - 协方差矩阵类型：diagonal
    - 现存问题：
      - **预测时对每个用户只使用到了User Model， Others Model还未完成部署**，后续相关预测操作也没实现
      - GMM模型超参数中的**高斯分布数目最优值**还需要通过**实验或者细读论文**得到
      - 论文里面提到的DTW和SVM也可以尝试复现一下

  





#### 深度学习模型实现











#### 拓展部分功能

##### 求交集





##### 呼吸训练





##### 睡眠监测







#### 后端部分架设

