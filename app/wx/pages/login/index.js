// pages/index/index.js
// 获取应用实例
var app = getApp()
Page({
  data: {
    spreakingAnimation: {},// 放大动画
    j: 1,// 帧动画初始图片
    isSpeaking: false,// 是否在录音状态
    recordPath: "", // 临时路径
    mode: 0 ,// 呼吸模式 0-未选择 1-sniff 2-deep
    currentSelectTripType: 'Sniff' // 呼吸模式
  },
  selectedSniff: function (e) {
    this.setData({
      currentSelectTripType: e.currentTarget.dataset.id
    })
  },
  selectedDeep: function(e) {
    this.setData({
      currentSelectTripType: e.currentTarget.dataset.id
    })
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
      //开始录音
      this.setData({
        isSpeaking: true
      })
      speaking.call(this);

      wx.startRecord({
        success: function (res) {
          //录音成功，保存路径
          var tempFilePath = res.tempFilePath;
          console.log(res)
          _this.setData({
            recordPath: tempFilePath
          });
        },
        fail: function (res) {
          //录音失败 
          wx.showModal({
            title: '提示',
            content: '录入失败',
            showCancel: false
          })
        }
      })
    } else {
      //停止录音
      clearInterval(this.timer)
      this.setData({
        isSpeaking: false,
        j: 1,
      })

      wx.stopRecord()
      // setTimeout(function () {
      //   var urls = " "; // 服务器地址
      //   wx.uploadFile({
      //     url: urls,
      //     filePath: _this.data.recordPath,
      //     name: 'file',
      //     formData: { },
      //     header: { 'content-type': 'multipart/form-data' },
      //     success: function (res) {
      //       console.log("录入成功")
      //     },
      //     fail: function (res) {
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
