<!--<template>-->
<!--  &lt;!&ndash; 景点图片 &ndash;&gt;-->
<!--  <div class="page-sight-image">-->
<!--    &lt;!&ndash; 顶部导航 &ndash;&gt;-->
<!--    <van-nav-bar title="景点图片" left-text="返回" left-arrow @click-left="goBack"/>-->
<!--    &lt;!&ndash; 图片列表 &ndash;&gt;-->
<!--    <van-pull-refresh v-model="refreshing" @refresh="onRefresh">-->
<!--      <van-list-->
<!--          class="sight-image"-->
<!--          v-model="loading"-->
<!--          :finished="finished"-->
<!--          finished-text="没有更多了"-->
<!--          :error.sync="error"-->
<!--          error-text="请求失败，点击重新加载"-->
<!--          @load="getImageList"-->
<!--      >-->
<!--        <van-row>-->
<!--          <van-col span="12" v-for="(item, index) in imageList" :key="index">-->
<!--            <van-image width="100%" height="100%" :src="item.img" @click="showPreview=true"/>-->
<!--          </van-col>-->
<!--        </van-row>-->
<!--      </van-list>-->
<!--    </van-pull-refresh>-->
<!--    &lt;!&ndash; //图片列表 &ndash;&gt;-->

<!--    &lt;!&ndash; 图片预览 &ndash;&gt;-->
<!--    <van-image-preview v-model="showPreview" :images="imgUrlList" @change="onChange">-->
<!--      <template v-slot:index>第{{ index + 1 }}页 / 共{{ imageList.length }}张</template>-->
<!--    </van-image-preview>-->
<!--    &lt;!&ndash; // 图片预览 &ndash;&gt;-->
<!--  </div>-->
<!--</template>-->
<!--<script>-->
<!--import {ajax} from '@/utils/ajax'-->
<!--import {SightApis} from '@/utils/apis'-->

<!--export default {-->
<!--  components: {},-->
<!--  data () {-->
<!--    return {-->
<!--      // 图片列表-->
<!--      imageList: [],-->
<!--      // 图片预览-->
<!--      index: 0,-->
<!--      showPreview: false,-->
<!--      // 当前的页码-->
<!--      currentPage: 1,-->
<!--      // 正在加载中-->
<!--      loading: false,-->
<!--      // 所有的内容加载完-->
<!--      finished: false,-->
<!--      // 请求失败-->
<!--      error: false,-->
<!--      // 是否正在下拉刷新中-->
<!--      refreshing: false-->
<!--    }-->
<!--  },-->
<!--  methods: {-->
<!--    /**-->
<!--     * 预览切换图片-->
<!--     */-->
<!--    onChange (index) {-->
<!--      this.index = index-->
<!--    },-->
<!--    goBack () {-->
<!--      this.$router.go(-1)-->
<!--    },-->
<!--    /**-->
<!--     * 下拉刷新执行-->
<!--     */-->
<!--    onRefresh () {-->
<!--      // 清空数据-->
<!--      this.imageList = []-->
<!--      this.currentPage = 1-->

<!--      this.finished = false-->
<!--      this.error = false-->
<!--    },-->
<!--    /**-->
<!--     * 图片列表-->
<!--     */-->
<!--    getImageList () {-->
<!--      const url = SightApis.sightImageUrl.replace('#{id}', this.id)-->
<!--      ajax.get(url, {-->
<!--        params: {-->
<!--          page: this.currentPage-->
<!--        }-->
<!--      }).then(({-->
<!--        data: {-->
<!--          meta,-->
<!--          objects-->
<!--        }-->
<!--      }) => {-->
<!--        this.imageList = this.imageList.concat(objects)-->
<!--        // 加载状态结束-->
<!--        this.loading = false-->
<!--        // 设置下一页的页码-->
<!--        this.currentPage = meta.current_page + 1-->
<!--        // 数据全部加载完成： 当前页面 == 总页数-->
<!--        if (meta.current_page === meta.page_count) {-->
<!--          this.finished = true-->
<!--        }-->
<!--        this.refreshing = false-->
<!--      }).catch(() => {-->
<!--        this.loading = false-->
<!--        this.error = true-->
<!--        this.refreshing = false-->
<!--      })-->
<!--    }-->
<!--  },-->
<!--  computed: {-->
<!--    /**-->
<!--     * 图片地址-->
<!--     */-->
<!--    imgUrlList () {-->
<!--      return this.imageList.map(item => item.img)-->
<!--    }-->
<!--  },-->
<!--  mounted () {-->
<!--    this.id = this.$route.params.id-->
<!--  }-->
<!--}-->
<!--</script>-->
<!--<style lang="less">-->
<!--.page-sight-image {-->
<!--  padding: 5px;-->

<!--  .van-col {-->
<!--    padding: 5px;-->
<!--  }-->
<!--}-->
<!--</style>-->
<template>
  <!-- 景点图片 -->
  <div class="page-sight-image">
    <!-- 顶部导航 -->
    <van-nav-bar title="景点图片" left-text="返回" left-arrow @click-left="goBack" fixed/>
    <!-- 图片列表 -->
    <van-pull-refresh v-model="refreshing" @refresh="onRefresh">
      <van-list
          class="sight-image"
          v-model="loading"
          :finished="finished"
          finished-text="没有更多了"
          error-text="请求失败，点击重新加载"
          :error.sync="error"
          @load="getImageList"
      >
        <van-row>
          <van-col span="12" v-for="(item, index) in imageList" :key="index">
            <van-image width="100%" height="100%" :src="item.img" @click="showPreview=true"/>
          </van-col>
        </van-row>
      </van-list>
    </van-pull-refresh>
    <!-- //图片列表 -->

    <!-- 图片预览 -->
    <van-image-preview v-model="showPreview" :images="imgUrlList" @change="onChange">
      <template v-slot:index>第{{ index + 1 }}张 / 共{{ imageList.length }}张</template>
    </van-image-preview>
    <!-- // 图片预览 -->
  </div>
</template>
<script>
import {ajax} from '@/utils/ajax'
import {SightApis} from '@/utils/apis'

export default {
  components: {},
  data () {
    return {
      id: 1,
      // 图片列表
      imageList: [],
      // 图片预览
      index: 0,
      showPreview: false,
      // 当前的页码
      currentPage: 1,
      // 正在加载中
      loading: false,
      // 所有的内容加载完
      finished: false,
      // 请求失败
      error: false,
      // 是否正在下拉刷新中
      refreshing: false
    }
  },
  methods: {
    /**
     * 预览切换图片
     */
    onChange (index) {
      this.index = index
    },
    goBack () {
      this.$router.go(-1)
    },
    /**
     * 下拉刷新执行
     */
    onRefresh () {
      // 清空数据
      this.imageList = []
      this.currentPage = 1

      this.finished = false
      this.error = false
      this.getImageList()
    },
    /**
     * 图片列表
     */
    getImageList () {
      const url = SightApis.sightImageUrl.replace('#{id}', this.id)
      // console.log('xx:', this.currentPage)
      ajax.get(url, {
        params: {
          page: this.currentPage
        }
      }).then(({
        data: {
          meta,
          objects
        }
      }) => {
        this.imageList = this.imageList.concat(objects)
        // 加载状态结束
        this.loading = false
        // 设置下一页的页码
        // this.currentPage += 1
        this.currentPage = meta.current_page + 1
        // 数据全部加载完成： 当前页面 == 总页数
        if (meta.current_page === meta.page_count) {
          this.finished = true
          // this.error = false
        }
        // this.error = false
        this.refreshing = false
      }).catch(() => {
        this.loading = false
        this.error = true
        this.refreshing = false
      })
    }
  },
  computed: {
    /**
     * 图片地址
     */
    imgUrlList () {
      return this.imageList.map(item => item.img)
    }
  },
  mounted () {
    this.id = this.$route.params.id
    // this.error = false
  }
}
</script>
<style lang="less">
.page-sight-image {
  padding: 50px 5px 0 5px;

  .van-col {
    padding: 5px;
  }
}
</style>



