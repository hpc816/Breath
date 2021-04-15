Component({
  /**
   * 组件的属性列表
   */
  properties: {
    selected: {
      type:Number,
      value:0
    }
  },

  /**
   * 组件的初始数据
   */
  data: {
    selected_pic:true,
    selected_usr:false,
    tabBar: [
      {
        "pagePath": "../../pages/picture/picture",
        "text": "相册",
        // "iconPath": "../../icons" // 因为子页面点击图标的不需要变化，因为直接跳转到首页了
      },
      {
        "pagePath": "../../pages/user/user",
        "text": "用户",
        // "iconPath": "../../images/user_icon.png"
      }
    ]
  },

  /**
   * 组件的方法列表
   */
  methods: {
    navigateDetail: function (e) {
      wx.redirectTo({ // 关闭所有打开过的页面，跳转到相对于的页面
        url: e.currentTarget.dataset.url  // 获取tabbar.wxml中data-url传递的参数
      })
      // console.log(e);
    },
  //tab框
  selected: function (e) {
    let that = this
    console.log(e)
    let index = e.currentTarget.dataset.index
    console.log("index",index)
    if (index == 0) {
      that.setData({
        selected: 0
      })
    } else if (index == 1) {
      that.setData({
        selected: 1
      })
    } else {
      that.setData({
        selected: 2
      })
    } 
  }
  }
})



// ---------------------------------------------------
// Component({
//   data: {
//     selected: 0,
//     color: "#7A7E83",
//     selectedColor: "#3cc51f",
//     list: [
//       {
//         pagePath: "/pages/index/index",
//         text: "首页",
//         iconPath: "/../icons/home.png",
//         selectedIconPath: "/../icons/home-o.png"
//       },
//       {
//         pagePath: "/pages/indexcate/indexcate",
//         text: "发现",
//         iconPath: "/images/more2.png",
//         selectedIconPath: "/images/more2_b.png"
//       },
//       {
//         pagePath: "/pages/mycenter/mycenter",
//         text: "我的",
//         iconPath: "/images/my.png",
//         selectedIconPath: "/images/my_b.png"
//       }
//     ]
//   },
//   methods: {
//     switchTab(e) {
//       let data = e.currentTarget.dataset
//       let url = data.path
//       wx.switchTab({
//         url
//       })
//       this.setData({
//         selected: data.index
//       })
//     }
//   }
// })
