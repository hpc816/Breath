// components/my-water/my-water.js
Component({
    /**
     * 组件的属性列表
     */
    properties: {
        size:{
            type:String,
            value:'20'
        }
    },

    /**
     * 组件的初始数据
     */
    data: {
        cirsize:407
    },

    /**
     * 组件的方法列表
     */
    methods: {

    },
    lifetimes: {
        created() {
            var self = this;
            wx.getSystemInfo({
                complete: (res) => {
                    var rpx = res.windowWidth/375/2;  
                    self.setData({
                        cirsize:self.data.cirsize*rpx
                    })  
                },
              })
        }
            
       
      }
})
