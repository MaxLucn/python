import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: {},
    profile: {}
  },
  mutations: {
    /**
     * 设置用户登录的信息
     */
    updateUserInfo (state, {
      user,
      profile
    }) {
      state.user = {
        ...state.user,
        ...user
      }
      state.profile = {
        ...state.profile,
        ...profile
      }
    },
    /**
     * 删除用户信息
     */
    deleteUserInfo (state) {
      state.user = {}
      state.profile = {}
    }
  },
  actions: {},
  modules: {}
})
