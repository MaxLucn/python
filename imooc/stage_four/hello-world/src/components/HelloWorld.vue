<template>
  <div class="hello">
    <h3>数字反转</h3>
    <p>{{ num }}</p>
    <button @click="reserveNum">点击此处实现数字反转</button>
    <h1>我的第一个全局组件</h1>
    <!-- 富文本的显示 -->
    <p v-html="rawHtml"></p>
    <p v-text='name'></p>
    <!-- v-bind 的使用 -->
    <a v-bind:href="url">跳转</a><br>
    <a :href="url">跳转2</a>

    <h3 :class='{"text-danger": result > 0}'>设置 css 的 class</h3>
    <h3 :style="{color: '#00f'}">设置 css 的 style</h3>
    <ul>
      <!-- 模版语法：显示普通文本 -->
      <li>
        内容 {{ name }}
      </li>
      <li>
        <!-- 模版语法：JS表达式 -->
        {{ name.split('').reverse().join('') }}
      </li>
      <li>{{ result > 0 ? 'YES' : 'NO' }}</li>
    </ul>
    <h3 v-if='weight >= 35'>BMI >= 35:重度肥胖</h3>
    <h3 v-else-if='weight >= 30'>BMI >= 30:中度肥胖</h3>
    <h3 v-else-if='weight >= 24'>BMI >= 24:过重</h3>
    <h3 v-else-if='weight >= 18.5'>BMI >= 18.5:正常</h3>
    <h3 v-else>BMI小于18.5:体重过轻</h3>
    
    <p>当前的数字是：{{ count }}</p>
    <input type="button" value='点击 + 1' v-on:click='count += 1'>
    <input type="button" value='加 2 再乘以 3' @click='calc'>
    <ul>
      <li v-for=" item in stuScoreList" :key="item.id" @click="addScore(item)">
        {{ item.name }} : {{  item.score }}
      </li>
    </ul>
    <h3>事件冒泡</h3>
    <div class="panel" @click='clickDiv'>
      <!-- .stop 阻止事件冒泡 -->
      <p @click.stop='clickP'>点击</p>
    </div>
    <h3>默认行为</h3>
    <a href="http://www.youtube.com" @click.prevent='clickDiv'>这是测试 .prevent 的（它的作用是阻止默认行为）</a>
    <h3>键盘事件</h3>
    <!-- 键盘事件修饰符
    监听回车键：keyup.enter
    监听删除/回车键：keyup.delete
     -->
    <input type="text" @keyup='submit'>
    <h3>表单输入绑定：用户登录</h3>
    <!-- v-model 实现双向绑定 -->
    <input type="text" v-model.trim="username"><br/>
    <input type="password" v-model="password"><br/>
    <!-- 选择 -->
    性别：（单选）
    <label for="">
      <input type="radio" value="男" v-model="sex">
      男
    </label>
    <label for="">
      <input type="radio" value="女" v-model="sex">
      女
    </label>
    <br>
    爱好：（下拉选择、多选）
    <!-- <select name="" id="" v-model="hobby">
      <option value="A">A</option>
      <option value="B">B</option>
      <option value="C">C</option>
      <option value="D">D</option>
    </select> -->
    <select v-model="hobby">
      <option value="option.value"
      v-for="(option, index) in options"
      :key='index'>
        {{ option.text }}
      </option>
    </select>
    <input type="button" value="登录" @click="login"><br/>
    <h2>组件内过滤器的使用</h2>
    <p>{{ price }}</p>
    <p>{{ price | priceFormat }}</p>
    <p v-bind:data-id='price | priceFormat'>{{ price | priceFormat }}</p>
    <h2>全局过滤器(定义在 main.js 中)的使用</h2>
    <p>{{ price|priceFormat2 }}</p>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  // data 必须是一个函数（在 Home.vue 中多次引用创建的组件的时候，
  // 可以自由更改其中某一个组件内的 data 值，而不会影响到其他组件）
  data(){
    return{
      num: '-694',
      'name': '组件名称',
      result: 10,
      rawHtml: '<h3 style="color:#f63000">HELLO</h3>',
      url: 'http://www.youtube.com',
      // 自由编程练习
      weight: 22,
      count: 0,
      // 有参数的点击事件，记录学生的成绩数组
      stuScoreList: [
        {id: 1, score: 0, name: '张三' },
        {id: 2, score: 0, name: '王武' },
        {id: 3, score: 0, name: '李四' }
        ],
      // 用户名、密码、性别、爱好
      username: '',
      password: '',
      sex: '男',
      hobby: [],
      options: [
        {text: '篮球', value: 'A'},
        {text: '足球', value: 'B'},
        {text: '排球', value: 'C'},
        {text: '网球', value: 'D'},
      ],
      price: 35
    }
  },
  /**
   * 没有参数的点击事件
   */
  methods:{
    calc() { 
      this.count = (this.count+2) * 3
      console.log('执行完成')
    },
    /**
     * 分数加 1
     */
    addScore(stu){
      stu.score += 1
      console.log(stu)
    },
    clickDiv() {
      window.alert('clickDIV')
    },
    clickP() {
      window.alert('clickP')
    },
    submit() {
      window.alert('键盘事件触发')
    },
    login() {
      console.log('用户名:', this.username)
      console.log('密码:', this.password)
    },
    reserveNum() {
      // if (this.num[0] != '-')
      //   {
      //     return this.data.split('').reverse.join('')
      //     }
      // else{
      //       let num = this.num.split('-')
      //       return num[0] + num[1].split('').reverse().join('')
      //     }
      this.num = this.num.split("").reverse().join("")
    },
  },
  // 过滤器的演示
  filters: {
    // 价格格式化
    priceFormat: function(price) {
      if (price === undefined || price === null || isNaN(price)) {
        return price
      }
      return '¥' + price.toFixed(2)
    },
    // reserveNum: function(num) {
    //   if (this.num[0] != '-')
    //     {
    //       return this.data.split('').reverse.join('')
    //       }
    //   else{
    //         // let num = this.num.split('-')
    //         return num[0] + num[1].split('').reverse().join('')
    //       }
    // }
  },
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="less">
.hello{
  h3 {
    margin: 40px 0 0;
  }
  ul {
    list-style-type: none;
    padding: 0;
      li {
        display: inline-block;
        margin: 0 10px;
      }
  }

  a {
    color: #42b983;
  }
}
.text-danger{
  color: #f00;
}
.panel{
  background-color: #42b983;
  padding: 50px;
  p {
    background-color: #f00;
    padding: 10px;
  }
}

</style>
