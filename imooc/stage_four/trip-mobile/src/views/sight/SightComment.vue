<template>
  <!-- 景点评论 -->
  <div class="page-sight-comment">
    <!-- 页面头部 -->
    <van-nav-bar
        left-text="返回"
        title="景点评论"
        left-arrow
        @click-left="goBack"
    />
    <div class="sight-comment">
      <comment-item v-for="item in commentList" :key="item.pk" :item="item"/>
    </div>
  </div>
</template>
<script>
import {ajax} from '@/utils/ajax'
import {SightApis} from '@/utils/apis'
// 评论项组件
import CommentItem from '@/components/sight/CommentItem'

export default {
  components: {
    CommentItem
  },
  data () {
    return {
      // 评论列表
      commentList: []
    }
  },
  methods: {
    goBack () {
      this.$router.go(-1)
    },
    /**
     * 评论列表
     */
    getCommentList () {
      const url = SightApis.sightCommentUrl.replace('#{id}', this.id)
      ajax.get(url).then(({data: {objects}}) => {
        this.commentList = objects
      })
    }
  },
  mounted () {
    this.id = this.$route.params.id
    this.getCommentList()
  }
}
</script>
<style lang="less">
.page-sight-comment {
  background-color: #fff;
}
</style>
