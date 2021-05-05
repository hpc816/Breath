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
    boundaryGap: false,
    data: ['4/10', '4/15', '4/20', '4/25', '4/30', '5/05', '5/10'],
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
    data: ['50', '60', '70', '80', '90', '100'],
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
      }
    }
  },
    series: [{
      data: ['90', '70', '80','70', '80', '90', "70"],
      type: 'line',
      smooth: true,
      symbol: 'none',
      areaStyle: {
        normal: {
          color: 'rgba(73, 117, 240, 0.24)' //改变区域颜色
        }
      },
      itemStyle : { 
        normal : { 
          lineStyle:{ 
            color:'#1C52F0FF', //改变折线颜色
            width:1.5
          } 
        } 
      },
      symbolSize: 7
    }]
  }
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
