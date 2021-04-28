## 个人任务清单

#### TODO-LIST

- 大创项目
  - 项目变更：项目内容扩展
    在实现基于呼吸声的用户身份认证的过程中，团队通过阅读相关论文及向指导老师咨询，发现了以呼吸声为中心的其他应用场景，如BreathRelax(通过对呼吸的指引，使用户得到一定程度的放松)，BreathHealth(通过呼吸声检测健康状况或睡眠质量)、BreathFriend (通过呼吸声和一些密码学算法进行交友匹配)等。 团队旨在打造一个围绕呼吸声，涵盖互联网+健康+安全的多功能应用系统
  - 中期材料



- 后端：
  - 数据库需要保存的信息：
    - 用户名
    - 密码
    - ....
  - 音频文件上传：
    - 1.上传到服务器之后服务器如何接受
    - 2.服务器怎么将接受的文件放入指定的文件夹
  - 模型训练
  - 验证





- 提纯问题：提纯之后可能会有维度对齐的问题，需要进行调整
  - 





#### 模型测试

##### GMM

- normal:

  - gmm_model, gmmorder=5,

    -  GMM_type1, 32维gfcc: ![image-20210408212139134](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210408212139134.png)

    - GMM_type1,96维gfcc:![image-20210408215157044](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210408215157044.png)

    - GMM_type1,13维mfcc:![image-20210408215325028](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210408215325028.png)

    - GMM_type2,32维gfcc:![image-20210409103236716](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409103236716.png)

      ![image-20210409152930902](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409152930902.png)

    - GMM_type2,96维gfcc:![image-20210409103414191](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409103414191.png)

    - GMM_type2,13维mfcc：![image-20210409102625950](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409102625950.png)

    - GMM_type3,32维gfcc:![image-20210409103549503](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409103549503.png)

    - GMM_type3,96维gfcc:![image-20210409103719302](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409103719302.png)

    - GMM_type3,13维mfcc:![image-20210409103835722](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409103835722.png)

    - GMM_type4,32维gfcc:![image-20210409104727189](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409104727189.png)

    - GMM_type4,96维gfcc:![image-20210409104905469](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409104905469.png)

    - GMM_type4,13维mfcc:![image-20210409104554414](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409104554414.png)

  - gmm_model , gmmorder=10:

    - GMM_type1,32维gfcc:![image-20210409105224812](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409105224812.png)
    - GMM_type1,96维gfcc:![image-20210409105407756](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409105407756.png)
    - GMM_type1,13维mfcc![image-20210409105619696](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409105619696.png)
    - GMM_type2,32维gfcc:![image-20210409105802130](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409105802130.png)
    - GMM_type2,96维gfcc:![image-20210409110024185](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409110024185.png)
    - GMM_type2,13维mfcc![image-20210409110225843](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409110225843.png)
    - GMM_type3,32维gfcc:![image-20210409110418805](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409110418805.png)
    - GMM_type3,96维gfcc:![image-20210409110552261](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409110552261.png)
    - GMM_type3,13维mfcc:![image-20210409110720106](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409110720106.png)
    - GMM_type4,32维gfcc:![image-20210409110914816](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409110914816.png)
    - GMM_type4,96维gfcc:![image-20210409111110301](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409111110301.png)
    - GMM_type4,13维mfcc:![image-20210409111313323](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409111313323.png)

  - gmm_model, gmmorder=15:

    - GMM_type1,32维gfcc:![image-20210409111509907](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409111509907.png)
    - GMM_type1,96维gfcc:![image-20210409111721774](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409111721774.png)
    - GMM_type1,13维mfcc![image-20210409111914952](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409111914952.png)
    - GMM_type2,32维gfcc:![image-20210409112119217](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409112119217.png)
    - GMM_type2,96维gfcc:![image-20210409112331634](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409112331634.png)
    - GMM_type2,13维mfcc![image-20210409112527865](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409112527865.png)
    - GMM_type3,32维gfcc:![image-20210409112819783](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409112819783.png)
    - GMM_type3,96维gfcc:![image-20210409113035576](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409113035576.png)
    - GMM_type3,13维mfcc:![image-20210409113307929](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409113307929.png)
    - GMM_type4,32维gfcc:![image-20210409113502352](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409113502352.png)
    - GMM_type4,96维gfcc:![image-20210409113649400](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409113649400.png)
    - GMM_type4,13维mfcc:![image-20210409113820757](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409113820757.png)

  - gmm_model, gmmorder=20:

    - GMM_type1,32维gfcc:![image-20210409125353380](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409125353380.png)

      

    - GMM_type1,96维gfcc:![image-20210409125540705](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409125540705.png)

    - GMM_type1,13维mfcc![image-20210409125721663](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409125721663.png)

    - GMM_type2,32维gfcc:![image-20210409125849177](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409125849177.png)

    - GMM_type2,96维gfcc:![image-20210409130903697](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409130903697.png)

    - GMM_type2,13维mfcc![image-20210409131256313](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409131256313.png)

    - GMM_type3,32维gfcc:![image-20210409130014985](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409130014985.png)

    - GMM_type3,96维gfcc:![image-20210409130613036](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409130613036.png)

    - GMM_type3,13维mfcc:![image-20210409131443230](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409131443230.png)

    - GMM_type4,32维gfcc:![image-20210409130203116](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409130203116.png)

    - GMM_type4,96维gfcc:![image-20210409130359984](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409130359984.png)

    - GMM_type4,13维mfcc:![image-20210409131711312](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409131711312.png)

  - gmm_model, gmmorder=25:

    - GMM_type1,32维gfcc:![image-20210409134122390](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409134122390.png)
    - GMM_type1,96维gfcc:![image-20210409132905272](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409132905272.png)
    - GMM_type1,13维mfcc![image-20210409132659946](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409132659946.png)
    - GMM_type2,32维gfcc:![image-20210409134019020](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409134019020.png)
    - GMM_type2,96维gfcc:![image-20210409133140388](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409133140388.png)
    - GMM_type2,13维mfcc![image-20210409132414113](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409132414113.png)
    - GMM_type3,32维gfcc:![image-20210409133759263](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409133759263.png)
    - GMM_type3,96维gfcc:![image-20210409133259497](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409133259497.png)
    - GMM_type3,13维mfcc:![image-20210409132151427](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409132151427.png)
    - GMM_type4,32维gfcc:![image-20210409133649968](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409133649968.png)
    - GMM_type4,96维gfcc:![image-20210409133428701](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409133428701.png)
    - GMM_type4,13维mfcc:![image-20210409132007609](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409132007609.png)

  - gmm_model, gmmorder=30:

    - GMM_type1,32维gfcc:![image-20210409134433291](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409134433291.png)
    - GMM_type1,96维gfcc:![image-20210409151831219](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409151831219.png)
    - GMM_type1,13维mfcc![image-20210409151940615](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409151940615.png)
    - GMM_type2,32维gfcc:![image-20210409134541982](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409134541982.png)
    - GMM_type2,96维gfcc:![image-20210409151647970](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409151647970.png)
    - GMM_type2,13维mfcc![image-20210409152046400](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409152046400.png)
    - GMM_type3,32维gfcc:![image-20210409150658225](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409150658225.png)
    - GMM_type3,96维gfcc:![image-20210409151458582](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409151458582.png)
    - GMM_type3,13维mfcc:![image-20210409152238643](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409152238643.png)
    - GMM_type4,32维gfcc:![image-20210409151001537](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409151001537.png)
    - GMM_type4,96维gfcc:![image-20210409151330573](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409151330573.png)
    - GMM_type4,13维mfcc:![image-20210409152400589](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210409152400589.png)

- deep:

  - gmm_model, gmmorder=5
    - GMM_type1,32维gfcc:
    - GMM_type1,96维gfcc:
    - GMM_type1,13维mfcc
    - GMM_type2,32维gfcc:
    - GMM_type2,96维gfcc:
    - GMM_type2,13维mfcc
    - GMM_type3,32维gfcc:
    - GMM_type3,96维gfcc:
    - GMM_type3,13维mfcc:
    - GMM_type4,32维gfcc:
    - GMM_type4,96维gfcc:
    - GMM_type4,13维mfcc:
  - gmm_model , gmmorder=10:
    - GMM_type1,32维gfcc:
    - GMM_type1,96维gfcc:
    - GMM_type1,13维mfcc
    - GMM_type2,32维gfcc:
    - GMM_type2,96维gfcc:
    - GMM_type2,13维mfcc
    - GMM_type3,32维gfcc:
    - GMM_type3,96维gfcc:
    - GMM_type3,13维mfcc:
    - GMM_type4,32维gfcc:
    - GMM_type4,96维gfcc:
    - GMM_type4,13维mfcc:
  - gmm_model, gmmorder=15:
    - GMM_type1,32维gfcc:
    - GMM_type1,96维gfcc:
    - GMM_type1,13维mfcc
    - GMM_type2,32维gfcc:
    - GMM_type2,96维gfcc:
    - GMM_type2,13维mfcc
    - GMM_type3,32维gfcc:
    - GMM_type3,96维gfcc:
    - GMM_type3,13维mfcc:
    - GMM_type4,32维gfcc:
    - GMM_type4,96维gfcc:
    - GMM_type4,13维mfcc:
  - gmm_model, gmmorder=20:
    - GMM_type1,32维gfcc:
    - GMM_type1,96维gfcc:
    - GMM_type1,13维mfcc
    - GMM_type2,32维gfcc:
    - GMM_type2,96维gfcc:
    - GMM_type2,13维mfcc
    - GMM_type3,32维gfcc:
    - GMM_type3,96维gfcc:
    - GMM_type3,13维mfcc:
    - GMM_type4,32维gfcc:
    - GMM_type4,96维gfcc:
    - GMM_type4,13维mfcc:
  - gmm_model, gmmorder=25:
    - GMM_type1,32维gfcc:
    - GMM_type1,96维gfcc:
    - GMM_type1,13维mfcc
    - GMM_type2,32维gfcc:
    - GMM_type2,96维gfcc:
    - GMM_type2,13维mfcc
    - GMM_type3,32维gfcc:
    - GMM_type3,96维gfcc:
    - GMM_type3,13维mfcc:
    - GMM_type4,32维gfcc:
    - GMM_type4,96维gfcc:
    - GMM_type4,13维mfcc:
  - gmm_model, gmmorder=30:
    - GMM_type1,32维gfcc:
    - GMM_type1,96维gfcc:
    - GMM_type1,13维mfcc
    - GMM_type2,32维gfcc:
    - GMM_type2,96维gfcc:
    - GMM_type2,13维mfcc
    - GMM_type3,32维gfcc:
    - GMM_type3,96维gfcc:
    - GMM_type3,13维mfcc:
    - GMM_type4,32维gfcc:
    - GMM_type4,96维gfcc:
    - GMM_type4,13维mfcc:

- sniff:

  - gmm_model, gmmorder=5
    - GMM_type1,32维gfcc:
    - GMM_type1,96维gfcc:
    - GMM_type1,13维mfcc
    - GMM_type2,32维gfcc:
    - GMM_type2,96维gfcc:
    - GMM_type2,13维mfcc
    - GMM_type3,32维gfcc:
    - GMM_type3,96维gfcc:
    - GMM_type3,13维mfcc:
    - GMM_type4,32维gfcc:
    - GMM_type4,96维gfcc:
    - GMM_type4,13维mfcc:
  - gmm_model , gmmorder=10:
    - GMM_type1,32维gfcc:
    - GMM_type1,96维gfcc:
    - GMM_type1,13维mfcc
    - GMM_type2,32维gfcc:
    - GMM_type2,96维gfcc:
    - GMM_type2,13维mfcc
    - GMM_type3,32维gfcc:
    - GMM_type3,96维gfcc:
    - GMM_type3,13维mfcc:
    - GMM_type4,32维gfcc:
    - GMM_type4,96维gfcc:
    - GMM_type4,13维mfcc:
  - gmm_model, gmmorder=15:
    - GMM_type1,32维gfcc:
    - GMM_type1,96维gfcc:
    - GMM_type1,13维mfcc
    - GMM_type2,32维gfcc:
    - GMM_type2,96维gfcc:
    - GMM_type2,13维mfcc
    - GMM_type3,32维gfcc:
    - GMM_type3,96维gfcc:
    - GMM_type3,13维mfcc:
    - GMM_type4,32维gfcc:
    - GMM_type4,96维gfcc:
    - GMM_type4,13维mfcc:
  - gmm_model, gmmorder=20:
    - GMM_type1,32维gfcc:
    - GMM_type1,96维gfcc:
    - GMM_type1,13维mfcc
    - GMM_type2,32维gfcc:
    - GMM_type2,96维gfcc:
    - GMM_type2,13维mfcc
    - GMM_type3,32维gfcc:
    - GMM_type3,96维gfcc:
    - GMM_type3,13维mfcc:
    - GMM_type4,32维gfcc:
    - GMM_type4,96维gfcc:
    - GMM_type4,13维mfcc:
  - gmm_model, gmmorder=25:
    - GMM_type1,32维gfcc:
    - GMM_type1,96维gfcc:
    - GMM_type1,13维mfcc
    - GMM_type2,32维gfcc:
    - GMM_type2,96维gfcc:
    - GMM_type2,13维mfcc
    - GMM_type3,32维gfcc:
    - GMM_type3,96维gfcc:
    - GMM_type3,13维mfcc:
    - GMM_type4,32维gfcc:
    - GMM_type4,96维gfcc:
    - GMM_type4,13维mfcc:
  - gmm_model, gmmorder=30:
    - GMM_type1,32维gfcc:
    - GMM_type1,96维gfcc:
    - GMM_type1,13维mfcc
    - GMM_type2,32维gfcc:
    - GMM_type2,96维gfcc:
    - GMM_type2,13维mfcc
    - GMM_type3,32维gfcc:
    - GMM_type3,96维gfcc:
    - GMM_type3,13维mfcc:
    - GMM_type4,32维gfcc:
    - GMM_type4,96维gfcc:
    - GMM_type4,13维mfcc:

  



- 仓库同步问题：这两项修改不涉及核心代码部分，不要同步到仓库，同步了之后反而会让其他成员需要重新配置pycharm![image-20210404172224095](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210404172224095.png)





- 1.spafe似乎对音频信号的采样率有特殊的要求，现在只有设置sr=16000程序才能跑通，考虑调整代码，使得使用原始采样率时也不会报错



- 2.每次都需要提取特征比较费时间，对内存和CPU消耗也比较大，考虑将音频的特征矩阵提取之后保存
  - 新增两个函数task_login和task_logout,分别用于保存音频文件特征向量和使用保存的特征向量进行模型训练
    - 运行结果：成功运行，音频文件特征向量成功保存在了本地，同时使用本地保存的特征向量文件也可以训练出模型![image-20210405115811003](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210405115811003.png)
      - ![image-20210405120606537](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210405120606537.png)
      - **预测准确率和验证通过率都是100%，但是可以看到区分度还是不太大**![image-20210405120650156](C:\Users\hpc\AppData\Roaming\Typora\typora-user-images\image-20210405120650156.png)





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

