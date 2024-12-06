<template>
    <div>
      <!-- 卡片化的标签页 -->
      <el-tabs type="card">
        <!-- 1、健康指数 -->
            <el-tab-pane label="健康指数">
                <el-card style=" height:80px; border: 1px solid #7f7f7f;" :body-style={padding:0} >         <!--:body-style={padding:0}取消卡片边距，btn就能在左上角 -->
                  <div class="card_label" style=" height: 28px;width: 100%; text-align: center;">健康指数</div>

                  <div class="form">                                                         <!-- inline="true"表单域在一行 -->
                    <el-form :inline="true"  :model="formInline1" class="demo-form-inline">
                      <el-form-item label="公司名称" style=" margin-right: 40px;">
                          <el-autocomplete
                              class="inline-input"
                              v-model="formInline1.company"
                              :fetch-suggestions="querySearch"
                              placeholder="公司名称"
                              size="mini"
                          ></el-autocomplete>

                        <el-input  v-model="formInline1.company" placeholder="请输入公司名称" size="mini"></el-input>
                      </el-form-item>

                      <el-form-item label="日期 " style=" margin-right: 40px;">
                        <quter-component v-model="formInline1.quarter_year" placeholder="选择季度" />
                      </el-form-item>
                      <el-form-item>
                        <el-button class="grayish_btn" @click="onSubmit1"  size="mini" style=" margin-right: 20px;">查询</el-button>
                      </el-form-item>
                      <el-form-item>
                        <el-button class="grayish_btn" @click="onSubmit2"  size="mini">清空</el-button>
                      </el-form-item>
                    </el-form>
                  </div>
                </el-card>

              <!-- 第一栏"健康指数"的表格 -->
            <div class="table">
              <el-table :data="tableData_1" :header-cell-style="{background: 'rgba(242, 242, 242)'}"
                      border  
                      height="250" 
                      :row-style="{height:'28px'}"
                      :cell-style="{padding:'3px'}"
                      header-row-class-name="active_header"
                      header-cell-class-name="active_header"
                      cell-class-name="content_center"
                      style="width: 100%; border: 1px solid #7f7f7f;">          <!-- style="width: 40%"               height="215"  -->
                    <el-table-column v-for='(val,key) in tableLabel_short' :prop="key" :label="val" /><!--插槽里面没有东西就可以用单标签  -->
                    <el-table-column
                            prop="scale"
                            label="操作">
                            <template slot-scope="scope">
                              <el-button type="primary" v-on:click="onSubmit3"  size="mini" >雷达图</el-button>
                              <el-button type="primary" @click="onSubmit4"  size="mini" >加入对比</el-button>
                              <el-button type="primary" @click="onSubmit5"  size="mini" >加入管理</el-button>
                            </template>
                    </el-table-column>
              </el-table>
              </div>
                <!--  第一栏"健康指数"的弹窗-单雷达图 -->
                <el-dialog  :visible.sync="detailsdialog"  width="80%" @open="open()">
                <el-card style=";">
                  <el-card style=" height:740px; border: 1px solid #7f7f7f;" :body-style={padding:0} >         <!--:body-style={padding:0}取消卡片边距，btn就能在左上角 -->
                      <div class="card_label" style=" height: 24px;width: 100%;text-align: left; padding-left:10px">雷达图对比</div>

                      <!-- 搜索框 -->
<!--                      <div class="form">                                                         &lt;!&ndash; inline="true"表单域在一行 &ndash;&gt;-->
<!--                        <el-form :inline="true"  :model="formInline_1" class="demo-form-inline">-->
<!--                          <el-form-item label="公司:" style=" margin-right: 40px;">-->
<!--                            <el-autocomplete-->
<!--                                class="inline-input"-->
<!--                                v-model="formInline2.company1"-->
<!--                                :fetch-suggestions="querySearch"-->
<!--                                placeholder="公司名称"-->
<!--                                size="mini"-->
<!--                            ></el-autocomplete>-->
<!--                          </el-form-item>-->
<!--                          <el-form-item>-->
<!--                            <el-button   class="grayish_btn" @click="onSubmit6"  size="mini" style=" margin-right: 20px;">查询</el-button>-->
<!--                          </el-form-item>-->
<!--                          -->
<!--                        </el-form>-->
<!--                      </div>-->
                  <!-- 雷达图 -->
                  <div class='radar' >
<!--                        <div class="quarter_change">-->
<!--                          <i class="el-icon-arrow-left"  border style="font-size: 50px;color:#7f7f7f"></i>-->
<!--                          <div>上一季度</div>-->
<!--                        </div>-->
                      
                        <div ref="echarts_3" style="height:500px;width:500px"></div>
                    </div>

                    <!-- "雷达图"表格 -->
                    <div class="table"  style="padding:20px">
                      <el-table :data="tableData_1"
                              border  
                              :row-style="{height:'28px'}"
                              :cell-style="{padding:'3px'}"
                              header-row-class-name="active_header"
                              header-cell-class-name="active_header"
                              cell-class-name="content_center"
                              style="width: 100%; border: 1px solid #7f7f7f">          <!-- style="width: 40%"               height="215"  -->
                              <el-table-column prop="name" label="名称"></el-table-column>
                            <el-table-column v-for='(val,key) in tableLabel_long' :prop="key" :label="val"><!--插槽里面没有东西就可以用单标签  -->
                          </el-table-column>
                      </el-table>
                    </div>

                  </el-card>
                  <!-- 历史健康指数 -->
                  <el-card style=" height:680px; border: 1px solid #7f7f7f;" :body-style={padding:0} >         <!--:body-style={padding:0}取消卡片边距，btn就能在左上角 -->
                      <div class="card_label" style=" height: 24px;width: 100%;text-align: left; padding-left:10px">历史健康指数</div>

                      <!-- 搜索框 -->
                      <div class="form">                                                         <!-- inline="true"表单域在一行 -->
                        <el-form :inline="true"  :model="formInline_2" class="demo-form-inline">
                          <el-form-item label="开始时间 " style=" margin-right: 40px;">
                          <quter-component label="开始时间" v-model="formInline_2.start_quarter" placeholder="选择季度" />
                          </el-form-item>
                          <el-form-item label="结束时间 " style=" margin-right: 40px;">
                          <quter-component label="结束时间" v-model="formInline_2.end_quarter" placeholder="选择季度" />
                          </el-form-item>
<!--                          <el-form-item label="起止时间 " style=" margin-right: 40px;">-->
<!--                            <el-select   v-model="formInline_2.start_quarter" placeholder="请选择开始时间" size="mini">-->
<!--                              <el-option v-for="item in options_quarter_year" :key="item.value" :label="item.label" :value="item.value"></el-option>-->
<!--                            </el-select>-->

<!--                            <el-select   v-model="formInline_2.end_quarter" placeholder="请选择结束时间" size="mini">-->
<!--                              <el-option v-for="item in options_quarter_year" :key="item.value" :label="item.label" :value="item.value"></el-option>-->
<!--                            </el-select>-->
<!--                          </el-form-item>-->

                          <el-form-item>
                            <el-button   class="grayish_btn" @click="onSubmit7"  size="mini" style=" margin-right: 20px;">查询</el-button>
                          </el-form-item>
                          
                        </el-form>
                      </div>
                      
                      <!-- 折线图 -->
                      <div class='line' >
                      
                      <div ref="echarts_4" style="height:500px;width:800px"></div>
                    </div>

                    

                </el-card>
              </el-card>
        
              </el-dialog>
              <!-- 加入对比还不知道怎么写,跳转吗 -->
              <!-- 加入管理,把这一行数据存入管理tab -->


          </el-tab-pane>

        <!-- 2、对比 -->
            <el-tab-pane label="对比">
                <!-- 2-1-雷达图对比 -->
                <el-card style=" height:850px; border: 1px solid #7f7f7f;" :body-style={padding:0} >         <!--:body-style={padding:0}取消卡片边距，btn就能在左上角 -->
                    <div class="card_label" style=" height: 24px;width: 100%;text-align: left; padding-left:10px">雷达图对比</div>

                    <!-- 搜索框 -->
                    <div class="form">                                                         <!-- inline="true"表单域在一行 -->
                      <el-form :inline="true"  :model="formInline2" class="demo-form-inline">
                        <el-form-item label="公司1:" style=" margin-right: 40px;">
                          <el-autocomplete
                              class="inline-input"
                              v-model="formInline2.company1"
                              :fetch-suggestions="querySearch"
                              placeholder="公司名称"
                          ></el-autocomplete>
                        </el-form-item>
                        <el-form-item label="公司2:" style=" margin-right: 40px;">
                          <el-autocomplete
                              class="inline-input"
                              v-model="formInline2.company2"
                              :fetch-suggestions="querySearch"
                              placeholder="公司名称"
                          ></el-autocomplete>
                          <el-form-item label="时间 " style=" margin-right: 40px;margin-left: 40px;">
                          <quter-component label="开始时间" v-model="formInline2.quarter_year" placeholder="选择季度" />
                          </el-form-item>
                        </el-form-item>
                        <el-form-item>
                          <el-button   class="grayish_btn" @click="onSubmit6"  size="mini" style=" margin-right: 20px;">查询</el-button>
                        </el-form-item>
                        
                      </el-form>
                    </div>
                
                    <!-- 雷达图 -->
                    <div class='radar' >
<!--                      <div class="quarter_change">-->
<!--                        <i class="el-icon-arrow-left"  border style="font-size: 50px;color:#7f7f7f"></i>-->
<!--                        <div>上一季度</div>-->
<!--                      </div>-->
                    
                      <div ref="echarts_1" style="height:500px;width:500px"></div>
                    </div>

                    <!-- "对比"表格 -->
                    <div class="table"  style="padding:20px">
                      <el-table :data="tableData_2_1" :header-cell-style="{background: 'rgba(242, 242, 242)'}"
                              border  
                              :row-style="{height:'28px'}"
                              :cell-style="{padding:'3px'}"
                              header-row-class-name="active_header"
                              header-cell-class-name="active_header"
                              cell-class-name="content_center"
                              style="width: 100%; border: 1px solid #7f7f7f">          <!-- style="width: 40%"               height="215"  -->
                              <el-table-column prop="name" label="名称"></el-table-column>
                            <el-table-column v-for='(val,key) in tableLabel_long' :prop="key" :label="val"><!--插槽里面没有东西就可以用单标签  -->
                          </el-table-column>
                      </el-table>
              </div>

                </el-card>
                <!-- 2-2-健康指数对比 -->
                <el-card style=" height:680px; border: 1px solid #7f7f7f;" :body-style={padding:0} >         <!--:body-style={padding:0}取消卡片边距，btn就能在左上角 -->
                    <div class="card_label" style=" height: 24px;width: 100%;text-align: left; padding-left:10px">健康指数对比</div>

                    <!-- 搜索框 -->
                    <div class="form">                                                         <!-- inline="true"表单域在一行 -->
                      <el-form :inline="true"  :model="formInline3" class="demo-form-inline">
<!--                        <el-form-item label="公司1:" style=" margin-right: 40px;">-->
<!--                          <el-input  v-model="formInline3.company1" placeholder="请输入公司名称" ></el-input>-->
<!--                        </el-form-item>-->

<!--                        <el-form-item label="公司2:" style=" margin-right: 40px;">-->
<!--                          <el-input  v-model="formInline3.company2" placeholder="请输入公司名称" ></el-input>-->
<!--                        </el-form-item>-->
                        <el-form-item label="开始时间 " style=" margin-right: 40px;">
                          <quter-component v-model="formInline3.start_quarter" placeholder="选择季度" />
                        </el-form-item>
                        <el-form-item label="结束时间 " style=" margin-right: 40px;">
                          <quter-component v-model="formInline3.end_quarter" placeholder="选择季度" />
                        </el-form-item>
<!--                        <el-form-item label="起止时间 " style=" margin-right: 40px;">-->
<!--                          <el-select   v-model="formInline3.start_quarter" placeholder="请选择开始时间" size="mini">-->
<!--                            <el-option v-for="item in options_quarter_year" :key="item.value" :label="item.label" :value="item.value"></el-option>-->
<!--                          </el-select>-->

<!--                          <el-select   v-model="formInline3.end_quarter" placeholder="请选择结束时间" size="mini">-->
<!--                            <el-option v-for="item in options_quarter_year" :key="item.value" :label="item.label" :value="item.value"></el-option>-->
<!--                          </el-select>-->
<!--                        </el-form-item>-->

                        <el-form-item>
                          <el-button   class="grayish_btn" @click="onSubmit10"  size="mini" style=" margin-right: 20px;">查询</el-button>
                        </el-form-item>
                        
                      </el-form>
                    </div>
                    <!-- 折线图 -->
                    <div class='line' >
                      <div ref="echarts_2" style="height:500px;width:800px"></div>
                    </div>

                    

                </el-card>
                <!-- 2-3-交叉对比 -->
                <el-card style=" height:740px; border: 1px solid #7f7f7f;" :body-style={padding:0} >         <!--:body-style={padding:0}取消卡片边距，btn就能在左上角 -->
                    <div class="card_label" style=" height: 24px;width: 100%;text-align: left; padding-left:10px;">交叉对比</div>
                    <el-tabs type="card" style='padding-top:10px;padding-left:10px;'>
                    <!-- 2-3-1 行业-->
                      <el-tab-pane label="行业">
                        <el-card style=" height:80px; border: 1px solid #7f7f7f;" :body-style={padding:0} >
                          <div class="card_label" style=" height: 24px;width: 100%;text-align: left; padding-left:10px;">条件查询</div>
                          <!-- 搜索框 -->
                          <div class="form">                                                         <!-- inline="true"表单域在一行 -->
                            <el-form :inline="true"  :model="formInline4" class="demo-form-inline">
                              <el-form-item label="日期 " style=" margin-right: 40px;">
                                <quter-component v-model="formInline4.quarter_year" placeholder="选择季度" />
                              </el-form-item>
                                <el-form-item label="行业名称 " style=" margin-right: 40px;">
                                  <el-select   v-model="formInline4.industry" placeholder="请选择行业名称" >
                                    <el-option v-for="item in options_industry" :key="item.value" :label="item.label" :value="item.value"></el-option>
                                  </el-select>
                                </el-form-item>
                                <el-form-item>
                                  <el-button   class="grayish_btn" @click="onSubmit8"  size="mini" style=" margin-right: 20px;">查询</el-button>
                                </el-form-item>
                            </el-form>
                          </div>
                        </el-card>
                        <!-- "对比-交叉对比-行业"表格 -->
                        <div class="table"  style="  padding: 20px 10px 2px 0px;"><!--返回表格添加间隙 上 右 -->
                          <el-table :data="tableData_2_2" :header-cell-style="{background: 'rgba(242, 242, 242)'}"
                                  border  
                                  :row-style="{height:'28px'}"
                                  :cell-style="{padding:'3px'}"
                                  header-row-class-name="active_header"
                                  header-cell-class-name="active_header"
                                  cell-class-name="content_center"
                                  style="width: 100%; border: 1px solid #7f7f7f">          <!-- style="width: 40%"               height="215"  -->
                                
                                  <el-table-column prop="name" label="名称"></el-table-column>
                                  <el-table-column v-for='(val,key) in tableLabel_long' :prop="key" :label="val"  sortable><!--插槽里面没有东西就可以用单标签  -->
                                  </el-table-column>
                          </el-table>
                        </div>
                      </el-tab-pane>
                    <!-- 2-3-2 地域 -->
                      <el-tab-pane label="地域">
                        <el-card style=" height:80px; border: 1px solid #7f7f7f;" :body-style={padding:0} >
                          <div class="card_label" style=" height: 24px;width: 100%;text-align: left; padding-left:10px;">条件查询</div>
                          <!-- 搜索框 -->
                          <div class="form">                                                         <!-- inline="true"表单域在一行 -->
                            <el-form :inline="true"  :model="formInline5" class="demo-form-inline">
                              <el-form-item label="开始时间">
                                <el-date-picker  v-model="formInline5.start_date" type="date" placeholder="年-月-日" size="mini"></el-date-picker>
                              </el-form-item>

                              <el-form-item label="结束时间">
                                <el-date-picker v-model="formInline5.end_date" type="date" placeholder="年-月-日" size="mini"></el-date-picker>
                              </el-form-item>

                              <el-form-item label="省份 " style=" margin-right: 40px;">
                                <el-select   v-model="formInline5.province" placeholder="请选择省份" size="mini">
                                  <el-option v-for="item in options_province" :key="item.value" :label="item.label" :value="item.value"></el-option>
                                </el-select>
                              </el-form-item>

                              <el-form-item>
                                <el-button   class="grayish_btn" @click="onSubmit9"  size="mini" style=" margin-right: 20px;">查询</el-button>
                              </el-form-item>
                              
                            </el-form>
                          </div>
                        </el-card>
                        
                        <!-- "对比-交叉对比-地域"表格 -->
                        <div class="table"  style="  padding: 20px 10px 2px 0px;"><!--返回表格添加间隙 上 右 -->
                          <el-table :data="tableData_2_3" :header-cell-style="{background: 'rgba(242, 242, 242)'}"
                                  border  
                                  :row-style="{height:'28px'}"
                                  :cell-style="{padding:'3px'}"
                                  header-row-class-name="active_header"
                                  header-cell-class-name="active_header"
                                  cell-class-name="content_center"
                                  style="width: 100%; border: 1px solid #7f7f7f">          <!-- style="width: 40%"               height="215"  -->
                                
                                  <el-table-column prop="name" label="名称"></el-table-column>
                                  <el-table-column v-for='(val,key) in tableLabel_long' :prop="key" :label="val"  sortable><!--插槽里面没有东西就可以用单标签  -->
                                  </el-table-column>
                          </el-table>
                        </div>
                      </el-tab-pane>
                      
                    </el-tabs>
                </el-card>
            </el-tab-pane><!-- 2对比-end -->

             <!-- 3、我的管理 -->
            <el-tab-pane label="我的管理">
            <!-- 第三栏"我的管理"的表格 -->
            <div class="table">
              <el-table :data="tableData_3" :header-cell-style="{background: 'rgba(242, 242, 242)'}"


                      border  
                      height="250" 
                      :row-style="{height:'28px'}"
                      :cell-style="{padding:'3px'}"
                      header-row-class-name="active_header"
                      header-cell-class-name="active_header"
                      cell-class-name="content_center"
                      style="width: 100%; border: 1px solid #7f7f7f;">          <!-- style="width: 40%"               height="215"  -->
                    <el-table-column v-for='(val,key) in tableLabel_short' :prop="key" :label="val" /><!--插槽里面没有东西就可以用单标签  -->
                    <el-table-column
                            prop="scale"
                            label="操作">
                            <template slot-scope="scope">
                              <el-button type="primary" v-on:@click="onSubmit3"  size="mini" >雷达图</el-button>
                              <el-button type="primary" @click="onSubmit4"  size="mini" >加入对比</el-button>
                              <el-button type="primary" @click="onSubmit5"  size="mini" >加入管理</el-button>
          
                            </template>
                    </el-table-column>
              </el-table>

            </div>
              

          </el-tab-pane>

       
      </el-tabs>
    </div>
  </template>
  
<script>
import quterComponent from "@/components/quterComponent";
import * as echarts from "echarts"
import http from '../utils/request'
export default {
  name:'health',
  components:{
    quterComponent
},
  data() {
    return {
      // 雷达图数据
      radarData:[],
// 雷达图弹窗
  detailsdialog:false,
// 【分页组件的数据】
        total:10,
        page_size:1,
        currentPage:2,
// 【整合接收数据】
      formInline1: {
      // 第1栏"健康指数"
        company: '',
        quarter_year: '',
      },
      formInline2: {
      // 第2栏"对比"-"雷达图对比、健康指数共用"
        tableData1:[],
        tableData2:[],
        radarData1:[],
        radarData2:[],
        company1: '',
        company2: '',
        quarter_year: '',
      },
      formInline3: {
      // 第2栏"对比"-"健康指数对比"
        company1: '',
        company2: '',
        start_quarter:'',
        end_quarter:'',
      },
      formInline4: {
      // 第2栏"对比"-"交叉对比"- 行业
        quarter_year:'',
        end_date:'',
        industry:'',//行业独有
    },
    formInline5: {
      // 第2栏"对比"-"交叉对比"-地域共用
        start_date:'',
        end_date:'',
        province:'',//地域独有
    },
    // 健康指数点击雷达图后显示弹窗
    formInline_1: {
      company:'',
    },
    formInline_2: {
      start_quarter:'',
      end_quarter:'',
    },
// 【搜索栏】

    // 第2栏"对比"-"交叉对比"搜索栏(行业)
      options_industry: [
        {value: "房地产业",
        label: "房地产业"}, 
        {value: "信息传输、软件和信息技术服务业",
        label: "信息传输、软件和信息技术服务业"}, 
        {value: "水利、环境和公告设施管理业",
        label: "水利、环境和公告设施管理业"}, 
        {value: "制造业",
        label: "制造业"}, 
        {value: "综合",
        label: "综合"}, 
        {value: "建筑业",
        label: "建筑业"}, 
        {value: "批发和零售业",
        label: "批发和零售业"}, 
        {value: "电力、热力、燃气及水生产和供应业",
        label: "电力、热力、燃气及水生产和供应业"}, 
        {value: "银行",
        label: "银行"}, 
      ],
    // 第2栏"对比"-"交叉对比"搜索栏(地域省份)
      options_province:[
      {value: "北京市",
      label: "北京市"}, 
      {value: "山西省",
      label: "山西省"}, 
      {value: "河北省",
      label: "河北省"}, 
      {value: "河南省",
      label: "河南省"}, 
      {value: "山东省",
      label: "山东省"}, 
      {value: "安徽省",
      label: "安徽省"}, 
      ],

// 【表格】
// [table-label]
tableLabel_short: {
        name: '公司名称',
        level: '健康等级',
        健康指数: '健康指数',
      },
tableLabel_long: {
        // name: '名称',
      健康指数: '健康指数',
  财务状态:'财务状态',
  运行状态:'运行状态',
  规模扩张:'规模扩张',
  声誉风险:'声誉风险',
  外部环境:'外部环境',
  操盘模式:'操盘模式',
      },
// [table-data]
      // 第1栏"健康指数"表格
      tableData_1: [
        // { name: '中国银行',
        //   index: 1,
        //   level: "中等",},
      ],
      // 第2栏"对比"表格
      tableData_2_1: [

      ],
      // 第2栏"对比"-"交叉对比"表格_行业
      tableData_2_2: [
        { name: '中国银行',
          index: 1,},

        { name: '北京银行',
          index: 3,},
      ],
      // 第2栏"对比"-"交叉对比"表格_地域
      tableData_2_3: [
        { name: '中国银行',
          index: 1,},

        { name: '北京银行',
          index: 3,},
      ],
      // 第3栏"我的管理"
      tableData_3: [
      {   name: '中国银行',
          index: 1,
          level: "中等",},
      ],
      // 第1栏"健康指数"-点击“雷达图”
      tableData_4: [
      {   name: '中国银行',
          index: 1,
          level: "中等",},
      ],


    }
  },

  methods:{
// 联想
    querySearch(queryString, cb) {
      console.log(queryString)
      // console.log(cb)
      http.get(
          "/search/search_health/?keyword="+queryString,

          // paramsSerializer: params => {
          //   return qs.stringify(params, { indices: false })
      ).then(response => {
        // console.log(response.data)
        // console.log(cb)
        let result=response.data
        let re=[]
        for (let i of result){
          re.push({"value":i})
        }
        cb(re)
      })},
    // 健康指数
    onSubmit1(){
      console.log("健康指数查询")

        http.get(
                "/health/health_search/",
                {params:{
                    name: this.formInline1.company,//公司名
                    date: this.formInline1.quarter_year,//时间（年份+季度）
        }}).then(response => {
          if (response.data.data) {


            this.tableData_1 = Array(response.data.data)
            if (this.tableData_1['等级'] === 1)
              this.tableData_1[0].level = '严重'
            else if (this.tableData_1['等级'] === 2)
              this.tableData_1[0].level = '中等'
            else
              this.tableData_1[0].level = '良好'
            // console.log(response)
            this.tableData_1[0].name = this.formInline1.company
            // console.log(this.tableData_1)
            if (this.radarData) {
              this.radarData.length = 0
            }
            for (let i in response.data.data) {
              // console.log(i)
              if (i !== '健康指数' && i !== '等级' && typeof response.data.data[i] === 'number') this.radarData.push(response.data.data[i])
            }
            // console.log(this.radarData)
          }
          else {
            this.$notify.info({
              title: '提示',
              message: '暂无数据'
            });
          }
        }
        )

    },
    // 

    onSubmit2(){
      console.log("清空")
    },

    onSubmit3(){
      console.log("雷达图")
      this.detailsdialog = true//打开弹窗
    },
    onSubmit4(){
            console.log("加入对比")      
    },
    onSubmit5(){
            console.log("加入管理")
    },
    
    onSubmit6(){
      if (this.tableData_2_1 || this.formInline2.radarData1 ||this.formInline2.radarData2){
        this.formInline2.radarData1.length=0
        this.formInline2.radarData2.length=0
        this.tableData_2_1.length=0
      }
      const request1= http.get(
          "/health/health_search/",
          {params:{
              name: this.formInline2.company1,//公司名
              date: this.formInline2.quarter_year,//时间（年份+季度）
            }})
      const request2=http.get("/health/health_search/",
          {params:{
              name: this.formInline2.company2,//公司名
              date: this.formInline2.quarter_year,//时间（年份+季度）
            }})
      Promise.all([request1,request2]).then((res)=>{
        const response1=res[0]
        const response2=res[1]
            this.formInline2.tableData1= response1.data.data
        if (this.formInline2.tableData1['等级']===1)
          this.formInline2.tableData1.level='严重'
        else if (this.formInline2.tableData1['等级']===2)
          this.formInline2.tableData1.level='中等'
        else
          this.formInline2.tableData1.level='良好'
        this.formInline2.tableData1.name=this.formInline2.company1
        this.tableData_2_1.push( this.formInline2.tableData1)
        for (let i in response1.data.data){
          if (i !=='健康指数' && i !=='等级' && typeof response1.data.data[i]==='number') this.formInline2.radarData1.push(response1.data.data[i])}


        this.formInline2.tableData2= response2.data.data
        if (this.formInline2.tableData2['等级']===1)
          this.formInline2.tableData2.level='严重'
        else if (this.formInline2.tableData2['等级']===2)
          this.formInline2.tableData2.level='中等'
        else
          this.formInline2.tableData2.level='良好'
        // console.log(response)
        this.formInline2.tableData2.name=this.formInline2.company2
        for (let i in response2.data.data)
          if (i !=='健康指数' && i !=='等级' && typeof response2.data.data[i]==='number') this.formInline2.radarData2.push(response2.data.data[i])
        console.log(this.formInline2.radarData2)
        console.log(this.formInline2.radarData1)

        this.tableData_2_1.push( this.formInline2.tableData2)
      }).then(()=>{
        const echarts1 = echarts.init(this.$refs.echarts_1)
        const option1 = {
          // 右上角存图
          toolbox: {
            feature: {
              saveAsImage: {}
            }
          },
          title: {
            text: this.formInline2.quarter_year,
            x:'center',//水平安放位置，默认为'left'，可选为：'center' | 'left' | 'right' | {number}（x坐标，单位px）
            y:"bottom",
            padding:[ 0,10,10,10],

          },
          legend: {
            data: ['中国银行']
          },
          radar: {
            // shape: 'circle',
            indicator: [
              { name: '投资关系', max: 100 },
              { name: '操盘模式', max: 100 },
              { name: '财务状态', max: 100 },
              { name: '运行状态', max: 100 },
              { name: '规模扩张', max: 100 },
              { name: '声誉风险', max: 100 },
              { name: '外部环境', max: 100 }
            ]
          },
          series: [
            {
              name: 'Budget vs spending',
              type: 'radar',
              data: [
                {
                  value:  this.formInline2.radarData1,
                  name:   this.formInline2.company1
                },
                {
                  value:  this.formInline2.radarData2,
                  name:   this.formInline2.company2
                },
              ]
            }
          ]
        };
        echarts1.setOption(option1)
      })


    },
    onSubmit10(){
      let echarts1 = echarts.init(this.$refs.echarts_2)
      http.get(
          "/health/line_chart/",
          {params:{
              name1: this.formInline2.company1,//公司名
              name2:this.formInline2.company2,
              sdate: this.formInline3.start_quarter,//时间（年份+季度）
              edate:this.formInline3.end_quarter,
            }}).then(response => {
        let time=response.data.data['date']
        let index1=response.data.data['value1']
        let index2=response.data.data['value2']
        // 折线图
        const option= {
          // 右上角存图
          toolbox: {
            feature: {
              saveAsImage: {}
            }
          },
          title: {
            text: '健康指数',
            x:'center',//水平安放位置，默认为'left'，可选为：'center' | 'left' | 'right' | {number}（x坐标，单位px）

          },
          tooltip: {
            trigger: 'axis'
          },
          legend: {
            data: [this.formInline2.company1,this.formInline2.company2],
            x:'center',//水平安放位置，默认为'left'，可选为：'center' | 'left' | 'right' | {number}（x坐标，单位px）
            y:"bottom",
            padding:0,
          },
          grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
          },
          xAxis: {
            type: 'category',
            boundaryGap: false,
            data: time,
            axisLabel: {
              interval:0,
              rotate:40}
          },
          yAxis: {
            type: 'value',
          },
          series: [
            {
              name: this.formInline2.company1,
              type: 'line',
              stack: 'Total',
              data: index1
            },
            {
              name: this.formInline2.company2,
              type: 'line',
              stack: 'Total',
              data: index2
            },
          ]
        };
        echarts1.setOption(option)
      })
    },
    onSubmit7(){
            console.log("健康 历史")
      http.get(
          "/health/line_chart/",
          {params:{
              name1: this.formInline1.company,//公司名
              sdate: this.formInline_2.start_quarter,//时间（年份+季度）
              edate:this.formInline_2.end_quarter,
            }}).then(response => {
              let time=response.data.data['date']
              let index=response.data.data['value1']
        // 折线图
        const echarts4 = echarts.init(this.$refs.echarts_4)
        const option_4 = {
          // 右上角存图
          toolbox: {
            feature: {
              saveAsImage: {}
            }
          },
          title: {
            text: '健康指数',
            x:'center',//水平安放位置，默认为'left'，可选为：'center' | 'left' | 'right' | {number}（x坐标，单位px）

          },
          tooltip: {
            trigger: 'axis'
          },
          legend: {
            data: [this.formInline1.company],
            x:'center',//水平安放位置，默认为'left'，可选为：'center' | 'left' | 'right' | {number}（x坐标，单位px）
            y:"bottom",
            padding:0,
          },
          grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
          },
          xAxis: {
            type: 'category',
            boundaryGap: false,
            data: time,
            axisLabel: {
              interval:0,
              rotate:40}
          },
          yAxis: {
            type: 'value',


          },
          series: [
            {
              name: this.formInline1.company,
              type: 'line',
              stack: 'Total',
              data: index
            },
            // {
            //   name: '北京银行',
            //   type: 'line',
            //   stack: 'Total',
            //   data: [220, 182, 191, 234, 290, 330, 310]
            // },

          ]
        };
        echarts4.setOption(option_4)
      })


    },
    onSubmit8(){
            console.log("交叉对比-行业 查询")
      http.get(
          "/health/health_indus/",
          {params:{
              ind: this.formInline4.industry,//公司名
              date: this.formInline4.quarter_year,//时间（年份+季度）
            }}).then(response => {
            this.tableData_2_2= Array(response.data.data)
             console.log(this.tableData_2_2)})
            // if (this.formInline2.tableData1['等级']===1)
            //   this.formInline2.tableData1.level='严重'
            // else if (this.formInline2.tableData1['等级']===2)
            //   this.formInline2.tableData1.level='中等'
            // else
            //   this.formInline2.tableData1.level='良好'
            // this.formInline2.tableData1.name=this.formInline2.company1
            // this.tableData_2_1.push( this.formInline2.tableData1)
    },
    onSubmit9(){
            console.log("交叉对比-地域 查询")
    },

    // 弹窗显示echarts
    initEcharts() {
        // 弹窗的雷达图与折线图
          // 雷达图
          const echarts3 = echarts.init(this.$refs.echarts_3)
          const option_3 = {
            // 右上角存图
            toolbox: {
              feature: {
                saveAsImage: {}
              }
            },
            title: {
              text: this.formInline1.quarter_year.slice(0,4)+'年第'+this.formInline1.quarter_year.slice(6,)+'季度',
              x:'center',//水平安放位置，默认为'left'，可选为：'center' | 'left' | 'right' | {number}（x坐标，单位px）
              y:"bottom",
              padding:[ 0,10,10,10],
              
            },
            legend: {
              data: ['中国银行']
            },
            radar: {
              // shape: 'circle',
              indicator: [
                { name: '投资关系', max: 100 },
                { name: '操盘模式', max: 100 },
                { name: '财务状态', max: 100 },
                { name: '运行状态', max: 100 },
                { name: '规模扩张', max: 100 },
                { name: '声誉风险', max: 100 },
                { name: '外部环境', max: 100 }
              ]
            },
            series: [
              {
                name: 'Budget vs spending',
                type: 'radar',
                data: [
                  {
                    value:  this.radarData,
                    name:   this.formInline1.company
                  },
                ]
              }
            ]
          };
          echarts3.setOption(option_3)
      },
      open(){
        this.$nextTick(() => {
        //  执行echarts方法
          this.initEcharts()
        })
      },

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
  .table{
    // 和选项框隔开
    margin-top:10px;
    font-size: 12px;


    // 调整表头间隔、设置表头下方边框颜色
    /deep/ .el-table td.el-table__cell, .el-table th.el-table__cell.is-leaf {
    border-bottom: 1px solid #333333 !important;
    padding: 1px 0; 
    min-width: 0;
    }
    // 去除表格cell间隔
    .el-table .el-table__cell {
      padding: 0px 0; 
      min-width: 0;
      border-color:#333333;

    }
    /deep/ .active_header{//表头
      color: #333333;
      font-size: 13px;
      text-align: center !important;
      border-color:#333333;

      // height: 1px;
    }
    /deep/ .content_center{//表的内容
      text-align: center !important;
      font-size: 13px;
      border-color:#333333;
    }
  }

  // 雷达图
  .radar{
    display:flex;
    justify-content:center;
    margin-right: 200px;
        
        /deep/ .quarter_change{
          display:column;
          justify-content:center;
          margin-top: 200px;
          margin-left: 0px;
          margin-right: 150px;
          margin-bottom: 20px;

    }
  }
  .line{
    display:flex;
    justify-content:center;
  }
  .grayish_btn{//浅灰色按钮
    color: #fff;//文字颜色
    background-color: #aaaaaa;//背景颜色
  }
</style>
  