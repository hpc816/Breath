// 开始录音
Page({
  // 开始录音
  data: {
    selectType:'',
    startRecording:false,
    showVoiceMask:false,
    recordAnimationNum:[],
    buttons: [{ id: 1, name: 'sniff' }, { id: 2, name: 'deep' }],
  },

  onLoad: function (options) {
    this.data.buttons[0].checked = true;
    this.setData({
      buttons: this.data.buttons,
    })
  },

  radioButtonTap: function (e) {
    console.log(e);
    let id = e.currentTarget.dataset.id;
    console.log(id);
    for (let i = 0; i < this.data.buttons.length; i++) {
      if (this.data.buttons[i].id == id) {
        //当前点击的位置为true即选中
        this.data.buttons[i].checked = true;
      }
      else {
        //其他的位置为false
        this.data.buttons[i].checked = false;
      }
    }
    this.setData({
      buttons: this.data.buttons,
      msg: "id:"+id
    })
  },

  //触发录音界面
  createRecording:function(e){
    this.setData({
      showVoiceMask:true
    })
  },
   startRecording:function (e) {
        console.log('开始录音');
        this.setData({
          selectType: 'voice',
          startRecording:true
        })
    
        this.startVoiceRecordAnimation();
        var that = this;
        const recorderManager = wx.getRecorderManager();
        recorderManager.start({ 
          format: 'wav',   
        });
    
        recorderManager.onStart(() => {  
          console.log('recorder start')  
        })    
      },
    
      // 结束录音
      stopRecording: function (e) {  
        console.log('结束录音');  
        var that = this;  
        const recorderManager = wx.getRecorderManager();  
        recorderManager.stop();  
        recorderManager.onStop((res) => { 
          console.log('recorder stop', res)
          const { tempFilePath } = res;    
          if (res.duration < 1000) {   
            wx.showToast({   
              title: '说话时间太短!',   
              icon:'none'   
            })
    
            this.stopVoiceRecordAnimation();
    
            that.setData({ 
              startRecording: false
            })
            return;
    
          }
    
          if (this.data.cancleRecording === false) {
            if (tempFilePath.length !== 0) {
              var recordLength = 0;
              if (res.duration / 1000 < 22) {
                recordLength = 160;
              } else {
                recordLength = (res.duration / 1000) / 60 * 440;
              }
    
              var recordTime = (res.duration / 1000).toFixed(0);
              console.log('recordLength' + recordLength);
              that.setData({
                recordingLength: recordLength,
                recordingTime: recordTime,
                voiceTempFilePath: tempFilePath,
                selectResource: true,
                showVoiceMask: false,
                startRecording: false
              })
    
              that.stopVoiceRecordAnimation();
    
            }
    
          } else {
    
            that.setData({
              selectResource: false,
              showVoiceMask: false,
              startRecording: false,
              cancleRecording:false 
            })
    
            that.stopVoiceRecordAnimation();
    
          }
    
        })
    
      },
    
      //向上滑动取消录音
    
      moveToCancle: function (event) {
    
        let currentY = event.touches[0].pageY;
    
        if (this.data.lastVoiceYPostion !== 0) {
    
          if (currentY - this.data.lastVoiceYPostion < 0 && currentY < 470) {
    
            this.setData({
    
              cancleRecording:true
    
            })
    
          }
    
        }
    
        this.setData({
    
          lastVoiceYPostion: currentY
    
        })
    
      },
    
      //麦克风帧动画 
    
      startVoiceRecordAnimation:function () {
    
        var that = this;
    
        //话筒帧动画 
    
        var i = 1;
    
        that.data.recordAnimationSetInter = setInterval(function () {
    
          i++;
    
          i = i % 5;
    
          that.setData({
    
            recordAnimationNum: i
    
          })
    
        }, 300);
    
      },
    
      // 停止麦克风动画计时器
    
      stopVoiceRecordAnimation:function () {
    
        var that = this;
    
        clearInterval(that.data.recordAnimationSetInter);
    
      } 
});