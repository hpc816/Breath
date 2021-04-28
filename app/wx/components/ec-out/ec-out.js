// components/ec-out/ec-out.js
import * as echarts from '../ec-canvas/echarts';
function initChart(canvas, width, height) {
  const chart = echarts.init(canvas, null, {
    width:width,
    height: height
  });
  canvas.setChart(chart);

  var option = {

    grid:{
      y:40,
      y2:40,
  },
  xAxis: {
    type: 'category',
    // boundaryGap: false,
    data: ['6/14', '6/15', '6/16', '6/17', '6/18', '6/19', '6/20'],
    axisLine:{
      show:false
    },
    axisTick:{
      show:false
    }
},
yAxis: {
    type: 'category',
    boundaryGap: false,
    data: ['05:00', '06:00', '07:00', '08:00', '09:00', '10:00'],
    axisLine:{
      show:false
    },
    axisTick:{
      show:false
    },
    splitLine: {
      show: true,
      lineStyle:{
         color: ['#EDEDEDFF'],
         width: 0.5,
         type: 'solid'
    },
　　}
},
series: [{
  data: ['09:00', '07:00', '08:00','07:00', '08:00', '09:00', "08:00"],
    type: 'bar',
    itemStyle: { 
      normal: {
          //柱形图圆角，初始化效果
          barBorderRadius:[15, 15, 0, 0],
          color:'#577EEC',
      }
    },
    barWidth : 13.5
}]
  };
  chart.setOption(option);
  return chart;
}
Component({
  /**
   * 组件的属性列表
   */
  properties: {

  },

  /**
   * 组件的初始数据
   */
  data: {
    ec: {
      onInit: initChart
    }
  },

  /**
   * 组件的方法列表
   */
  methods: {

  }
})
