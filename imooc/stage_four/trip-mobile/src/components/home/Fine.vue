<template>
    <!-- 精选景点 -->
    <div class="home-fine-box">
      <!-- 顶上导航 -->
      <van-cell
        title="精选景点"
        icon="location-o"
        is-link
        title-style="text-align:left"
        value="更多" />
      <!-- // 顶上导航 -->
      <!-- 景点的列表 -->
      <div class="box-main">
        <sight-item v-for="item in dataList"
          :key="item.id"
          :item="item"/>
      </div>
      <!-- // 景点的列表 -->
    </div>
</template>
<script>
import { ajax } from '@/utils/ajax'
import { SightApis } from '@/utils/apis'
import SightItem from '@/components/common/ListSight'
export default ({
  components: {
    SightItem
  },
  data () {
    return {
      dataList: []
    }
  },
  methods: {
    /**
    * 查询精选景点的数据
    */
    getDataList () {
      ajax.get(SightApis.sightListUrl, {
        params: {
          is_top: 1
        }
      }).then(({ data }) => {
        this.dataList = data.objects
      })
    }
  },
  created () {
    this.getDataList()
    // this.dataList = [
    //   { id: 1, name: '景点名称', score: 5, price: 98 },
    //   { id: 2, name: '景点名称', score: 4.5, price: 98 },
    //   { id: 3, name: '景点名称', score: 4, price: 98 },
    //   { id: 4, name: '景点名称', score: 4.5, price: 98 },
    //   { id: 5, name: '景点名称', score: 5, price: 98 },
    //   { id: 6, name: '景点名称', score: 4.5, price: 98 },
    //   { id: 7, name: '景点名称', score: 4, price: 98 }
    // ]
  }
})
</script>

<style lang="less">
.home-fine-box {
  padding: 0 10px;
  .van-cell {
    padding: 10px 0;
  }
  .box-main {
    padding-bottom: 50px;
  }
}
</style>
