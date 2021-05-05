// pages/day/day.js
var timestamp = Date.parse(new Date());
//返回当前时间毫秒数
timestamp = timestamp / 1000;
//获取当前时间
var n = timestamp *1000;
var date = new Date(n);
//年
var Y =date.getFullYear();
//月
var M = (date.getMonth()+ 1 < 10 ? '0' + (date.getMonth() + 1) : date.getMonth() + 1);
//日
var D = date.getDate()< 10 ? '0' + date.getDate() : date.getDate();

var app=getApp();

Page({

  /**
   * 页面的初始数据
   */
  data: {
    circlesize:200,
    // tab 切换
    tabArr: {
      curHdIndex: 1,
      curBdIndex: 1
    },
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

    //设置时间
    this.setData({
      time: Y + "年" + M + "月" + D + '日',
    })
     // 获取系统信息
     wx.getSystemInfo({
      success: (res) => {
        console.log(res);
        this.setData({
          // 25:顶部控制切换的view高度
          contentHeight:res.windowHeight-25
        })
      }
    })
  },
  getUserProfile() {
    // 推荐使用wx.getUserProfile获取用户信息，开发者每次通过该接口获取用户个人信息均需用户确认
    // 开发者妥善保管用户快速填写的头像昵称，避免重复弹窗

    if(app.globalData.userInfo==null){
    wx.getUserProfile({
      desc: '用于完善会员资料', // 声明获取用户个人信息后的用途，后续会展示在弹窗中，请谨慎填写
      success: (res) => {
        //业务逻辑
        console.log(res);
        app.globalData.userInfo=res.userInfo;
        console.log(app.globalData.userInfo.nickName)
      },
      fail: function (err) {
        console.log("获取失败: ", err);
        wx.navigateBack({
          delta: 1
        })
      }
    })
  }
  },
  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  },
    // //  tab切换
    // swichNav: function( e ) {
    //   var that = this;
    //   if( this.data.currentTab === e.target.dataset.current ) {
    //       return false;
    //   } else {
    //       that.setData( {
    //           currentTab: e.target.dataset.current
    //       })
    //   }
    // },
    // bindChange: function( e ) {
    //   var that = this;
    //   that.setData( { currentTab: e.detail.current });
    // },
    // toChange: function() {
    //   let that = this;
    //   that.setData({
    //       isShow: !that.data.isShow
    //   })
    // },
})

//   data: {
//     swiperList:[]
//   },

//   onLoad: function(options) {
    
//     wx.request({
//       url: 'https://api-hmugo-web.itheima.net/api/public/v1/home/swiperdata',
//       success: (result) => {
//         // console.log(result); 
//         this.setData({
//           swiperList:result.data.message
//         })
//       }
//     });
      
//   },
  
// });
  