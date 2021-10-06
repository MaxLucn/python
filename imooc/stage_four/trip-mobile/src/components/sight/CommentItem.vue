<template>
  <!-- 评论列表的每一项 -->
  <div class="comment-item-box">
    <div class="cmt-header">
      <div class="rate">
        <van-rate v-model="value"
                  readonly
                  allow-half
                  void-icon="star"
                  void-color="#eee"/>
      </div>
      <div class="user">张三*** 2021-10-6</div>
    </div>
    <div class="cmt-content">
      <p>评论内容：中国科学院华南植物园是我国历史悠久的植物学研究机构，
        前身为国立中山大学农林植物研究所，由著名植物学家陈焕镛院士于1929年创建。
        1954年改隶中国科学院易名中国科学院华南植物研究所，1956年建立华南植物园和我国第一个自然保护区―鼎湖山国家级自然保护区，
        2003年10月更名为中国科学院华南植物园。2018年以来，华南植物园实现整体进入中国科学院核心植物园，
        部分进入南海生态环境工程创新研究院、种子创新研究院和药物创新研究院的“率先行动计划”总目标。 </p>
    </div>
    <!-- 图片列表 -->
    <div class="cmt-images" @click="show=true">
      <van-image width="100" height="100" src="https://img.yzcdn.cn/vant/cat.jpeg"/>
      <van-image width="100" height="100" src="https://img.yzcdn.cn/vant/cat.jpeg"/>
      <van-image width="100" height="100" src="https://img.yzcdn.cn/vant/cat.jpeg"/>
    </div>
    <van-image-preview v-model="show" :images="images" @change="onChange">
      <template v-slot:index>第{{ index + 1 }}页</template>
    </van-image-preview>
    <!-- // 图片列表 -->
  </div>
</template>
<script>
export default {
  data () {
    return {
      show: false,
      index: 0,
      images: [
        'https://img.yzcdn.cn/vant/apple-1.jpg',
        'https://img.yzcdn.cn/vant/apple-2.jpg'
      ],
      value: 4.5
    }
  },
  methods: {
    onChange (index) {
      this.index = index
    }
  }
}
</script>
<style lang="less">
.comment-item-box {
  padding: 5px 10px;
  border-bottom: 1px solid #f6f6f6;

  .cmt-header {
    display: flex;
    justify-content: space-between;

    .user {
      font-size: 12px;
    }
  }

  .cmt-content {
    color: #616161;
    padding: 5px 0;
    text-align: left;
    font-size: 12px;
    line-height: 2.0;
  }

  .cmt-images {
    padding: 5px;
    text-align: left;
    margin-right: 5px;
  }
}
</style>
