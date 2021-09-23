/**
 * 存放项目中所有的接口地址
 */

const apiHost = 'http://localhost:8080/api'
/**
 *用户账户相关的接口
 */
const AccountsApis = {
  loginUrl: '/',
  logoutUrl: ''
}

/**
 * 系统模块的接口
 */
const SystemApis = {
  // 轮播图列表
  sliderListUrl: apiHost + '/system/slider/list/'
}

/**
 * 景点模块的接口
 */
const SightApis = {
  // 景点列表
  sightListUrl: apiHost + '/sight/sight/list/'
}

export {
  AccountsApis,
  SystemApis,
  SightApis
}
