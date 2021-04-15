//Page Object
Page({
  data: {
    swiperList:[]
  },
  //options(Object)
  
  //页面加载的时候就会触发
  onLoad: function(options) {
    // 异步请求获取轮播图
    wx.request({
      url: 'https://api-hmugo-web.itheima.net/api/public/v1/home/swiperdata',
      success: (result) => {
        // console.log(result); 
        this.setData({
          swiperList:result.data.message
        })
      }
    });
      
  },
  onReady: function() {
    
  },
  onShow: function() {
    
  },
  onHide: function() {

  },
  onUnload: function() {

  },
  onPullDownRefresh: function() {

  },
  onReachBottom: function() {

  },
  onShareAppMessage: function() {

  },
  onPageScroll: function() {

  },
  //item(index,pagePath,text)
  onTabItemTap:function(item) {

  }
});
  