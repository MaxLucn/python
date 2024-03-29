<template>
  <!-- 填写订单 -->
  <div class="page-order-submit">
    <!-- 页面导航 -->
    <van-nav-bar title="填写订单"
                 left-text="返回"
                 left-arrow
                 @click-left="goBack"/>
    <!-- 描述信息 -->
    <div class="order-info">
      <div class="left">
        <h3>{{ ticketDetail.name }}</h3>
        <div class="tips">{{ ticketDetail.desc }}</div>
        <div class="tags">
          <span>
            <van-icon name="clock-o"/>明日可定
          </span>
          <span>
            <van-icon name="clock-o"/>条件退
          </span>
        </div>
      </div>
      <div class="right">
        <div class="text-warning">￥{{ ticketDetail.sell_price }}/张</div>
        <van-button plain hairline type="info"
                    size="mini"
                    @click="showPopup=true">预订须知
        </van-button>
        <van-popup
            v-model="showPopup"
            closeable
            position="bottom"
            :style="{ height: '80%' }"
        >
          <TicketTips :ticketDetail="ticketDetail"/>
        </van-popup>
      </div>
    </div>
    <!-- //描述信息 -->
    <!-- 提交表单 -->
    <van-form @submit="onSubmit" class="form-box">
      <van-cell-group class="form-group">
        <van-cell title="选择出行日期"
                  :value="form.play_date"
                  @click="showCalendar = true"/>
        <van-calendar v-model="showCalendar" @confirm="onConfirm"/>
      </van-cell-group>
      <van-cell-group class="form-group">
        <van-cell title="购买数量">
          <van-stepper v-model="form.buy_count" integer min="1"/>
        </van-cell>
      </van-cell-group>
      <van-cell-group class="form-group">
        <van-field
            v-model="form.to_user"
            type="text"
            label="收件人"
            placeholder="输入收件人"
            :rules="[{ required: true, message: '请输入收件人' }]"
        />
        <van-field
            v-model="form.to_phone"
            type="text"
            label="手机号码"
            placeholder="输入手机号码"
            :rules="[{ required: true, message: '请输入手机号码' }]"
        />
      </van-cell-group>
      <van-submit-bar :price="totalPrice" button-text="提交订单"/>
    </van-form>
    <!-- //提交表单 -->
  </div>
</template>
<script>
import {OrderApis, SightApis} from '@/utils/apis'
import {ajax} from '@/utils/ajax'
import {mapState} from 'vuex'
import TicketTips from '@/components/sight/TicketTips'

export default {
  components: {
    TicketTips
  },
  data () {
    return {
      // 门票 ID
      id: '',
      // 预订须知弹框显示
      showPopup: false,
      // 日期选择弹框
      showCalendar: false,
      // 门票的详细信息
      ticketDetail: {},
      form: {
        play_date: '',
        buy_count: 1,
        to_user: '',
        to_phone: ''
      }
    }
  },
  computed: {
    /**
     * 计算总价
     */
    totalPrice () {
      return this.ticketDetail.sell_price * this.form.buy_count * 100
    },
    /**
     * 从vuex读取手机号码
     */
    ...mapState({
      phoneNum: state => state.user.username,
      nickname: state => state.user.nickname
    })
  },
  methods: {
    /**
     * 门票详情
     */
    getTicketDetail () {
      const url = SightApis.ticketDetailUrl.replace('#{id}', this.id)
      ajax.get(url).then(({data}) => {
        this.ticketDetail = data
      })
    },
    onSubmit () {
      console.log('提交表单')
      // ajax接口的调用
      ajax.post(OrderApis.ticketSubmitUrl, {
        ticket_id: this.id,
        ...this.form
      }).then(({data}) => {
        // 提示用户
        this.$notify({
          type: 'success',
          message: '提交成功，请支付'
        })
        // 跳转到待支付的页面
        this.$router.replace({
          name: 'OrderPay',
          params: {sn: data.sn}
        })
      })
    },
    formatDate (date) {
      return `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`
    },
    /**
     * 选择日期
     */
    onConfirm (date) {
      // 隐藏日历弹框
      this.showCalendar = false
      // 保存数据
      this.form.play_date = this.formatDate(date)
    },
    goBack () {
      this.$router.go(-1)
    }
  },
  created () {
    // 门票ID
    this.id = this.$route.params.id
    this.form.to_user = this.nickname || ''
    this.form.to_phone = this.phoneNum || ''
    // 获取门票信息
    this.getTicketDetail()
  }
}
</script>
<style lang="less">
.page-order-submit {
  // 门票信息
  .order-info {
    display: flex;
    padding: 10px;
    background: #fff;

    .left {
      flex: 1;
      text-align: left;

      h3 {
        margin: 0;
        padding: 5px 0;
      }

      .tips {
        padding: 10px 0;
        color: #999;
        font-size: 12px;
      }

      .tags {
        font-size: 12px;
      }
    }

    .right {
      width: 90px;
      text-align: right;
    }
  }

  // 表单区域
  .form-box {
    .form-group {
      margin-top: 10px;
      background: #ffffff;

      .van-cell__title {
        text-align: left;
      }
    }
  }
}
</style>
