// pages/index/index.js
// 获取应用实例
var app = getApp()
const recorderManager = wx.getRecorderManager()

Page({
  data: {
    spreakingAnimation: {},// 放大动画
    upSuccess: false,
    j: 1,// 帧动画初始图片
    isSpeaking: false,// 是否在录音状态
    // recordPath: "", // 临时路径
    mode: 0 ,// 呼吸模式 0-未选择 1-sniff 2-deep
    uid:'',
    recordingTimeqwe: 0, //录音计时
    auth:false,
    currentSelectTripType: 'Sniff' // 呼吸模式
  },

    //录音计时器
    recordingTimer: function() {
      var that = this;
      //将计时器赋值给setInter
      that.data.setInter = setInterval(
        function() {
          var time = that.data.recordingTimeqwe + 1;
          that.setData({
            recordingTimeqwe: time
          })
        }, 1000);
    },
  
  selectedSniff: function (e) {
    this.setData({
      currentSelectTripType: e.currentTarget.dataset.id
    }),
    console.log(this.data.currentSelectTripType);
  },
  selectedDeep: function(e) {
    this.setData({
      currentSelectTripType: e.currentTarget.dataset.id
    });
    console.log(this.data.currentSelectTripType);
  },
  onReady: function () {
    this.animation1 = wx.createAnimation({ duration: 1000, })
    this.animation2 = wx.createAnimation({ duration: 1000, })
    this.animation3 = wx.createAnimation({ duration: 1000, })
  },
  onLoad: function () {
      
  },
  //点击录音按钮
  startSpeak: function () {
    var _this = this;
    if (!this.data.isSpeaking) {
      var that=this;
      //开始录音
      this.setData({
        isSpeaking: true
      })
      speaking.call(this);
      
      const options = {
        sampleRate: 16000, //采样率
        numberOfChannels: 1, //录音通道数
        format: 'wav', //音频格式，有效值 aac/mp3
      }

      //开始录音计时
      that.recordingTimer();
      //开始录音
      recorderManager.start(options);
      recorderManager.onStart(() => {
        console.log('开始录音')
      });
      //错误回调
      recorderManager.onError((res) => {
        console.log(res);
      })

      // wx.startRecord({
      //   success: function (res) {
      //     //录音成功，保存路径
      //     var tempFilePath = res.tempFilePath;
      //     console.log(res)
      //     _this.setData({
      //       recordPath: tempFilePath
      //     });
      //   },
      //   fail: function (res) {
      //     //录音失败 
      //     wx.showModal({
      //       title: '提示',
      //       content: '录入失败',
      //       showCancel: false
      //     })
      //   }
      // })

    } else {
      recorderManager.stop();

      recorderManager.onStop((res) => {
        const that = this
        // let timestamp = util.formatTime2(new Date());

        console.log('停止录音', res.tempFilePath)
        const {
          tempFilePath
        } = res;
        
        var selected_mode=(_this.data.currentSelectTripType=='Sniff'?'sniff':'deep');
        var urls = `http://47.97.21.75/auth/${selected_mode}/hpc`; // 服务器地址
        // var urls = `http://47.97.21.75/auth/${selected_mode}/${app.globalData.userInfo.nickName}`; // 服务器地址
        //train
        var urltrain = `http://47.97.21.75/train/${selected_mode}`; 
        console.log('authbegin',urls);
        console.log('train',urltrain);
        console.log(`${app.globalData.upload_filepath}`);
        
        if(app.globalData.upload_filepath!=null){
          wx.request({
            url: urltrain,
            method: 'POST',
            data:{},
            success: function (res) {
              console.log(res.data);

              wx.request({
                url: urls,
                method: 'POST',
                header: {
                  'content-type':'application/json',
                  'Accept': 'application/json'
                },
                data:{
                  "filepath":app.globalData.upload_filepath
                },    //参数为键值对字符串
                
                success: function (res) {
                  console.log(res.data)
                  that.setData({upSuccess:true,auth:true});
                }
      
              })

            },
            fail: function (res) {
              console.log(res);
              wx.showModal({
                title: '提示',
                content: "网络请求失败，请确保网络是否正常",
                showCancel: false,
                success: function (res) {
                }
              });
              wx.hideToast();
            }
          })


      }
      else{
        console.log('have not upload...')
      }
      // 上传文件
      // setTimeout(function () {
      //   var selected_mode=(_this.data.currentSelectTripType=='Sniff'?'sniff':'deep');
      //   var urls = `http://47.97.21.75/auth/${selected_mode}/${app.globalData.userInfo.nickName}`; // 服务器地址
      //   console.log('authbegin',urls);

      //   wx.uploadFile({
      //     url: urls,
      //     filePath: tempFilePath,
      //     name: 'wav',
      //     formData: {
      //     },
      //     header: { 'content-type': 'multipart/form-data' },
      //     success: function (res) {
      //       console.log(res);
      //       console.log("录入成功");
      //       that.setData({upSuccess:true,auth:true});
      //     },
      //     fail: function (res) {
      //       console.log(res);
      //       wx.showModal({
      //         title: '提示',
      //         content: "网络请求失败，请确保网络是否正常",
      //         showCancel: false,
      //         success: function (res) {
      //         }
      //       });
      //       wx.hideToast();
      //     }
      //   });
      // }, 1000)
        
        // wx.cloud.uploadFile({
        //   cloudPath: "sounds/"+timestamp + '-' + this.randomNum(10000, 99999) + '.mp3',
        //   filePath: tempFilePath,
        //   // 成功回调
        //   success: res => {
        //     console.log('上传成功', res)
        //     that.setData({
        //       soundUrl: res.fileID,
        //       // time: util.formatTime1(new Date())
        //     })
        //   },
        // })

      })
      //停止录音
      clearInterval(this.timer)
      this.setData({
        isSpeaking: false,
        j: 1,
      })

      // wx.stopRecord()
      // setTimeout(function () {
      //   var selected_mode=(_this.data.currentSelectTripType=='Sniff'?'sniff':'deep');
      //   var urls = `https://47.97.21.75/upload/${selected_mode}/${app.globalData.userInfo.nickName}`; // 服务器地址
      //   console.log(urls);

        // wx.uploadFile({
        //   url: urls,
        //   filePath: _this.data.recordPath,
        //   name: 'wav',
        //   formData: {
        //   },
        //   header: { 'content-type': 'multipart/form-data' },
        //   success: function (res) {
        //     console.log(res);
        //     console.log(_this.data.recordPath);
        //     console.log("录入成功");
        //   },
        //   fail: function (res) {
        //     console.log(urls);
        //     wx.showModal({
        //       title: '提示',
        //       content: "网络请求失败，请确保网络是否正常",
        //       showCancel: false,
        //       success: function (res) {
        //       }
        //     });
        //     wx.hideToast();
        //   }
        // });
      // }, 1000)
    }
  },
})


function speaking() {
  //话筒帧动画
  var i = 1;
  this.timer = setInterval(function () {
    i++;
    i = i % 5;
    _this.setData({
      j: i
    })
    return
  }, 200);
  //波纹放大,淡出动画
  var _this = this;
  setTimeout(function () {
    animationFun(_this,1,1000)
  }, 0)
  setTimeout(function () {
    animationFun(_this, 2, 1000)
  }, 250)
  setTimeout(function () {
    animationFun(_this, 3, 1000)
  }, 500)
   
}
function animationFun(_this,index,time){ 
  //波纹放大,淡出动画
  if (_this.data.isSpeaking) {
    setTimeout(function () {
      animationFun(_this, index, time)
    }, time)
  }
  switch (index){
    case 1:
      _this.animation1.scale(1, 1).opacity(1).step({ duration: 0 });//还原
      _this.setData({
        spreakingAnimation1: _this.animation1.export()
      })
      break;
    case 2:
      _this.animation2.scale(1, 1).opacity(1).step({ duration: 0 });//还原
      _this.setData({
        spreakingAnimation2: _this.animation2.export()
      })
      break;
    case 3:
      _this.animation3.scale(1, 1).opacity(1).step({ duration: 0 });//还原
      _this.setData({
        spreakingAnimation3: _this.animation3.export()
      })
      break;
  }
  setTimeout(
    () => {
      switch (index) {
        case 1:
          _this.animation1.scale(3, 3).opacity(0).step();//修改透明度,放大
          _this.setData({
            spreakingAnimation1: _this.animation1.export()
          })
          break;
        case 2:
          _this.animation2.scale(3, 3).opacity(0).step();//修改透明度,放大
          _this.setData({
            spreakingAnimation2: _this.animation2.export()
          })
          break;
        case 3:
          _this.animation3.scale(3, 3).opacity(0).step();//修改透明度,放大
          _this.setData({
            spreakingAnimation3: _this.animation3.export()
          })
          break;
      }
    },100
  );
}
