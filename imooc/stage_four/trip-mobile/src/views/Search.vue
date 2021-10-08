<template>
  <!-- 搜索页面 -->
  <div class="page-search">
    <!-- 标题 -->
    <van-nav-bar title="搜索景点"/>
    <!-- 搜索框 -->
    <van-search
        v-model="sightName"
        show-action
        label="景点"
        placeholder="请输入搜索关键词"
        @search="onSearch"
    >
      <template #action>
        <div @click="onSearch">搜索</div>
      </template>
    </van-search>
    <!-- 景点列表 -->
    <div class="sight-list">
      <sight-item v-for="item in dataList"
                  :key="item.id"
                  :item="item"/>
    </div>
    <!-- 分页 -->
    <van-pagination v-model="currentPage"
                    :total-items="totalItems"
                    :items-per-page="perPage"/>
    <!-- 底部导航 -->
    <TripFooter/>
  </div>
</template>
<script>
import {ajax} from '@/utils/ajax'
import {SightApis} from '@/utils/apis'

// 景点列表的每一项
import SightItem from '@/components/common/ListSight'
// 底部导航
import TripFooter from '@/components/common/Footer'

export default {
  data () {
    return {
      // 景点名称
      sightName: '',
      // 景点列表的数据
      dataList: [],
      // 总记录数
      totalItems: 0,
      // 当前的页码
      currentPage: 1,
      // 每页的数据
      perPage: 4
    }
  },
  components: {
    SightItem,
    // 底部导航
    TripFooter
  },
  methods: {
    // 搜索框的实现
    onSearch () {
      console.log('onSearch')
      // 判断搜索内容是否为空
      if (!this.sightName) {
        this.$toast('请输入搜索词')
        return
      }
      // 重置数据
      this.dataList = []
      this.currentPage = 1
      // 执行查询
      this.getDataList()
    },
    // 景点列表的数据
    getDataList () {
      ajax.get(SightApis.sightListUrl, {
        params: {
          // is_top: 1
          page: this.currentPage,
          name: this.sightName,
          limit: this.perPage
        }
      }).then(({
        data: {
          meta,
          objects
        }
      }) => {
        this.dataList = objects
        // 总记录数
        this.totalItems = meta.total_count
      })
    },
    mounted () {
      this.getDataList()
    }
  },
  created () {
    this.getDataList()
  }
}
</script>
