<template>
  <div>
    <!-- 卡片化的标签页 -->
    <el-tabs type="card" @tab-click="handleTabClick">
      <!-- 利率风险 -->
      <el-tab-pane label="利率风险">
        <el-card style="height:80px; border: 1px solid #7f7f7f;" :body-style="{padding:0}">
          <div class="card_label" style="height: 28px; width: 100%; text-align: center;">利率风险</div>
          <div class="form">
            <el-form :inline="true"  :model="formInline" class="demo-form-inline">
              <el-form-item label="公司名称" style=" margin-right: 40px;">
                  <el-autocomplete
                      class="inline-input"
                      v-model="formInline.company"
                      :fetch-suggestions="querySearch1"
                      placeholder="公司名称"
                      size="mini"
                  ></el-autocomplete>
              </el-form-item>
              <el-form-item label="压力情景">
                <el-select   v-model="formInline.scenario" placeholder="选择压力情景" size="mini">
                  <el-option v-for="item in options_scenario1" :key="item.value" :label="item.label" :value="item.value"></el-option>
                </el-select>
              </el-form-item>
              <el-form-item>
                <el-button class="grayish_btn" @click="onSubmit1" size="mini" style="margin-right: 20px;">测试</el-button>
              </el-form-item>
            </el-form>
          </div>
        </el-card>
      </el-tab-pane>
      
      <!-- 汇率风险 -->
      <el-tab-pane label="汇率风险">
        <el-card style="height:80px; border: 1px solid #7f7f7f;" :body-style="{padding:0}">
          <div class="card_label" style="height: 28px; width: 100%; text-align: center;">汇率风险</div>
          <div class="form">
            <el-form :inline="true"  :model="formInline" class="demo-form-inline">
              <el-form-item label="公司名称" style=" margin-right: 40px;">
                  <el-autocomplete
                      class="inline-input"
                      v-model="formInline.company"
                      :fetch-suggestions="querySearch2"
                      placeholder="公司名称"
                      size="mini"
                  ></el-autocomplete>
              </el-form-item>
              <el-form-item label="压力情景">
                <el-select   v-model="formInline.scenario" placeholder="选择压力情景" size="mini">
                  <el-option v-for="item in options_scenario2" :key="item.value" :label="item.label" :value="item.value"></el-option>
                </el-select>
              </el-form-item>
              <el-form-item>
                <el-button class="grayish_btn" @click="onSubmit2" size="mini" style="margin-right: 20px;">测试</el-button>
              </el-form-item>
            </el-form>
          </div>
        </el-card>
      </el-tab-pane>
      
      <!-- 股票价格风险 -->
      <el-tab-pane label="股票价格风险">
        <el-card style="height:80px; border: 1px solid #7f7f7f;" :body-style="{padding:0}">
          <div class="card_label" style="height: 28px; width: 100%; text-align: center;">股票价格风险</div>
          <div class="form">
            <el-form :inline="true"  :model="formInline" class="demo-form-inline">
              <el-form-item label="公司名称" style=" margin-right: 40px;">
                  <el-autocomplete
                      class="inline-input"
                      v-model="formInline.company"
                      :fetch-suggestions="querySearch3"
                      placeholder="公司名称"
                      size="mini"
                  ></el-autocomplete>
              </el-form-item>
              <el-form-item label="压力情景">
                <el-select   v-model="formInline.scenario" placeholder="选择压力情景" size="mini">
                  <el-option v-for="item in options_scenario3" :key="item.value" :label="item.label" :value="item.value"></el-option>
                </el-select>
              </el-form-item>
              <el-form-item>
                <el-button class="grayish_btn" @click="onSubmit3" size="mini" style="margin-right: 20px;">测试</el-button>
              </el-form-item>
            </el-form>
          </div>
        </el-card>
      </el-tab-pane>
      
      <!-- 智能利率风险 -->
      <el-tab-pane label="智能利率风险">
        <el-card style="height:80px; border: 1px solid #7f7f7f;" :body-style="{padding:0}">
          <div class="card_label" style="height: 28px; width: 100%; text-align: center;">智能利率风险</div>
          <div class="form">
            <el-form :inline="true"  :model="formInline" class="demo-form-inline">
              <el-form-item label="公司名称" style=" margin-right: 40px;">
                  <el-autocomplete
                      class="inline-input"
                      v-model="formInline.company"
                      :fetch-suggestions="querySearch1"
                      placeholder="公司名称"
                      size="mini"
                  ></el-autocomplete>
              </el-form-item>
              <el-form-item label="压力情景">
                <el-select   v-model="formInline.scenario" placeholder="选择压力情景" size="mini">
                  <el-option v-for="item in options_scenario4" :key="item.value" :label="item.label" :value="item.value"></el-option>
                </el-select>
              </el-form-item>
              <el-form-item>
                <el-button class="grayish_btn" @click="onSubmit1" size="mini" style="margin-right: 20px;">测试</el-button>
              </el-form-item>
            </el-form>
          </div>
        </el-card>
      </el-tab-pane>
      
      <!-- 智能汇率风险 -->
      <el-tab-pane label="智能汇率风险">
        <el-card style="height:80px; border: 1px solid #7f7f7f;" :body-style="{padding:0}">
          <div class="card_label" style="height: 28px; width: 100%; text-align: center;">智能汇率风险</div>
          <div class="form">
            <el-form :inline="true"  :model="formInline" class="demo-form-inline">
              <el-form-item label="公司名称" style=" margin-right: 40px;">
                  <el-autocomplete
                      class="inline-input"
                      v-model="formInline.company"
                      :fetch-suggestions="querySearch2"
                      placeholder="公司名称"
                      size="mini"
                  ></el-autocomplete>
              </el-form-item>
              <el-form-item label="压力情景">
                <el-select   v-model="formInline.scenario" placeholder="选择压力情景" size="mini">
                  <el-option v-for="item in options_scenario4" :key="item.value" :label="item.label" :value="item.value"></el-option>
                </el-select>
              </el-form-item>
              <el-form-item>
                <el-button class="grayish_btn" @click="onSubmit2" size="mini" style="margin-right: 20px;">测试</el-button>
              </el-form-item>
            </el-form>
          </div>
        </el-card>
      </el-tab-pane>
      
      <!-- 智能股票价格风险 -->
      <el-tab-pane label="智能股票价格风险">
        <el-card style="height:80px; border: 1px solid #7f7f7f;" :body-style="{padding:0}">
          <div class="card_label" style="height: 28px; width: 100%; text-align: center;">智能股票价格风险</div>
          <div class="form">
            <el-form :inline="true"  :model="formInline" class="demo-form-inline">
              <el-form-item label="公司名称" style=" margin-right: 40px;">
                  <el-autocomplete
                      class="inline-input"
                      v-model="formInline.company"
                      :fetch-suggestions="querySearch3"
                      placeholder="公司名称"
                      size="mini"
                  ></el-autocomplete>
              </el-form-item>
              <el-form-item label="压力情景">
                <el-select   v-model="formInline.scenario" placeholder="选择压力情景" size="mini">
                  <el-option v-for="item in options_scenario4" :key="item.value" :label="item.label" :value="item.value"></el-option>
                </el-select>
              </el-form-item>
              <el-form-item>
                <el-button class="grayish_btn" @click="onSubmit3" size="mini" style="margin-right: 20px;">测试</el-button>
              </el-form-item>
            </el-form>
          </div>
        </el-card>
      </el-tab-pane>
      
    </el-tabs>
    <div class="chart-container">
      <div id="chart" style="width: 600px; height: 400px;"></div>
    </div>
  </div>
</template>

<script>
import http from '@/utils/request'; // 引入封装的http实例
import * as echarts from 'echarts';

export default {
  name: 'StressTesting',
  data() {
    return {
      formInline: {
        company: '',
        scenario: ''
      },
      companyValid: true, // 用于存储公司名称是否有效的标志
      weightedResults: [], // 用于存储返回的加权结果
      options_scenario1: [
        {value: 0.05},
        {value: 0.10},
        {value: -0.05},
        {value: -0.10},
      ].map(item => ({
        label: `${item.value > 0 ? '上升' : '下降'}${(Math.abs(item.value) * 100) % 1 === 0 ? Math.abs(item.value) * 100 : (Math.abs(item.value) * 100).toFixed(2)}%`,
        value: item.value
      })),
      options_scenario2: [
        {value: 0.05},
        {value: 0.10},
        {value: -0.05},
        {value: -0.10},
      ].map(item => ({
        label: `${item.value > 0 ? '外币升值' : '外币贬值'}${(Math.abs(item.value) * 100) % 1 === 0 ? Math.abs(item.value) * 100 : (Math.abs(item.value) * 100).toFixed(2)}%`,
        value: item.value
      })),
      options_scenario3: [
        {value: 0.10},
        {value: 0.20},
        {value: -0.10},
        {value: -0.20},
      ].map(item => ({
        label: `${item.value > 0 ? '上升' : '下降'}${(Math.abs(item.value) * 100) % 1 === 0 ? Math.abs(item.value) * 100 : (Math.abs(item.value) * 100).toFixed(2)}%`,
        value: item.value
      })),
      options_scenario4: [],
    };
  },
  methods: {
    querySearch1(queryString, cb) {
      http.get('/interest_rate_risk/search', { params: { company: queryString } })
        .then(response => {
          const re = response.data.map(item => ({ value: item }));
          cb(re);
          this.companyValid = true; // 设置标志
        })
        .catch(error => {
          if (error.response && error.response.status === 404) {
            this.$message.error('公司名称不存在');
            this.companyValid = false; // 设置标志
            this.clearChart(); // 清空图表
          }
        });
    },
    querySearch2(queryString, cb) {
      http.get('/currency_risk/search', { params: { company: queryString } })
        .then(response => {
          const re = response.data.map(item => ({ value: item }));
          cb(re);
          this.companyValid = true; // 设置标志
        })
        .catch(error => {
          if (error.response && error.response.status === 404) {
            this.$message.error('公司名称不存在');
            this.companyValid = false; // 设置标志
            this.clearChart(); // 清空图表
          }
        });
    },
    querySearch3(queryString, cb) {
      http.get('/stock_price_risk/search', { params: { company: queryString } })
        .then(response => {
          const re = response.data.map(item => ({ value: item }));
          cb(re);
          this.companyValid = true; // 设置标志
        })
        .catch(error => {
          if (error.response && error.response.status === 404) {
            this.$message.error('公司名称不存在');
            this.companyValid = false; // 设置标志
            this.clearChart(); // 清空图表
          }
        });
    },
    onSubmit1() {
      if (!this.formInline.company || !this.companyValid) {
        this.$message.error('请选择正确的公司名称');
        return;
      }
      if(!this.formInline.scenario){
        this.$message.error('请选择压力情景');
        return;
      }
      http.post('/interest_rate_risk/test', this.formInline)
        .then(response => {
          this.weightedResults = response.data;
          this.renderChart1();
        })
        .catch(error => {
          console.error("利率风险测试失败", error);
        });
    },
    onSubmit2() {
      if (!this.formInline.company || !this.companyValid) {
        this.$message.error('请选择正确的公司名称');
        return;
      }else if(!this.formInline.scenario){
        this.$message.error('请选择压力情景');
        return;
      }
      http.post('/currency_risk/test', this.formInline)
        .then(response => {
          this.weightedResults = response.data;
          this.renderChart2();
        })
        .catch(error => {
          console.error("汇率风险测试失败", error);
        });
    },
    onSubmit3() {
      if (!this.formInline.company || !this.companyValid) {
        this.$message.error('请选择正确的公司名称');
        return;
      }else if(!this.formInline.scenario){
        this.$message.error('请选择压力情景');
        return;
      }
      http.post('/stock_price_risk/test', this.formInline)
        .then(response => {
          this.weightedResults = response.data;
          this.renderChart3();
        })
        .catch(error => {
          console.error("股票价格风险测试失败", error);
        });
    },
    renderChart1() {
      // 按年份排序
      this.weightedResults.sort((a, b) => a.year - b.year);

      const chartDom = document.getElementById('chart');
      const myChart = echarts.init(chartDom);
      const option = {
        title: {
          text: `${this.formInline.company}压力测试结果`,
          left: 'center'
        },
        tooltip: {},
        legend: {
          data: ['净利息收入变动'],
          top: '10%'
        },
        xAxis: {
          type: 'category',
          data: this.weightedResults.map(item => item.year)
        },
        yAxis: {
          type: 'value'
        },
        series: [{
          name: '净利息收入变动',
          type: 'line',
          data: this.weightedResults.map(item => item.weighted_sum)
        }]
      };
      myChart.setOption(option);
    },
    renderChart2() {
      // 按年份排序
      this.weightedResults.sort((a, b) => a.year - b.year);

      const chartDom = document.getElementById('chart');
      const myChart = echarts.init(chartDom);
      const option = {
        title: {
          text: `${this.formInline.company}压力测试结果`,
          left: 'center'
        },
        tooltip: {},
        legend: {
          data: ['外币损益'],
          top: '10%'
        },
        xAxis: {
          type: 'category',
          data: this.weightedResults.map(item => item.year)
        },
        yAxis: {
          type: 'value'
        },
        series: [{
          name: '外币损益',
          type: 'line',
          data: this.weightedResults.map(item => item.weighted_sum)
        }]
      };
      myChart.setOption(option);
    },
    renderChart3() {
      // 按年份排序
      this.weightedResults.sort((a, b) => a.year - b.year);

      const chartDom = document.getElementById('chart');
      const myChart = echarts.init(chartDom);
      const option = {
        title: {
          text: `${this.formInline.company}压力测试结果`,
          left: 'center'
        },
        tooltip: {},
        legend: {
          data: ['经济资本'],
          top: '10%'
        },
        xAxis: {
          type: 'category',
          data: this.weightedResults.map(item => item.year)
        },
        yAxis: {
          type: 'value'
        },
        series: [{
          name: '经济资本',
          type: 'line',
          data: this.weightedResults.map(item => item.weighted_sum)
        }]
      }; 
      myChart.setOption(option);
    },
    handleTabClick(tab) {
      // 重置表单数据
      this.formInline.company = '';
      this.formInline.scenario = '';
      const chartDom = document.getElementById('chart');
      const myChart = echarts.init(chartDom);
      myChart.clear(); // 清空图表
      if (tab.label === '智能利率风险') {
        this.calculateScenario1();
      }else if (tab.label === '智能汇率风险') {
        this.calculateScenario2();
      }else if (tab.label === '智能股票价格风险') {
        this.calculateScenario3();
      }
    },
    calculateScenario1() {
      http.post('/smart_interest_rate_risk', {scenarios: this.options_scenario1})
        .then(response => {
          this.options_scenario4 = response.data.scenarios;
        })
        .catch(error => {
          console.error("智能利率风险压力测试失败", error);
        });
    },
    calculateScenario2() {
      http.post('/smart_currency_risk', {scenarios: this.options_scenario2})
        .then(response => {
          this.options_scenario4 = response.data.scenarios;
        })
        .catch(error => {
          console.error("智能汇率风险压力测试失败", error);
        });
    },
    calculateScenario3() {
      http.get('/smart_stock_price_risk')
        .then(response => {
          this.options_scenario4 = response.data.scenarios;
        })
        .catch(error => {
          console.error("智能股票价格风险压力测试失败", error);
        });
    },
    clearChart() {
      const chartDom = document.getElementById('chart');
      const myChart = echarts.init(chartDom);
      myChart.clear(); // 清空图表
    }
  }
};
</script>

<style lang="less" scoped>
.grayish_btn{//浅灰色按钮
  color: #fff;//文字颜色
  background-color: #aaaaaa;//背景颜色
}
.card_label{
  font-size: 13px;
  // padding:10px; 
  color:#fff;
  background-color: #7f7f7f;
}
.form{//产品搜索栏
    display:flex;
    justify-content:space-between;//左右贴边
    margin-top:5px; 
    // height: 40px;
    padding-left: 40px;
    // padding: 30px;

}
.chart-container {
  display: flex;
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
  margin-top: 20px;
}
</style>




