# 慕旅游网的接口文档
RESTful 风格接口。
* 200 请求数据成功
* 201 提交数据成功
* 400 参数错误
* 401 未登录
* 403 没有权限
* 500 服务器正忙

## 接口请求的地址
1、测试环境的地址
http://test.xxx.com/
2、生产环境额地址

## 错误代码及文字提示
```
{
    "error_code": "400000",
    "error_msg": "该字段不能为空",
    "error_list": {
        "password": [
            "该字段不能为空"
        ]
    }
}
```

## 请求头添加内容

## 分页处理
### 分页请求的参数
<table>
    <thead>
    <tr>
        <th>字段</th>
        <th>类型</th>
        <th>说明</th>
    </tr> 
    </thead>
    <tbody>
    <tr>
        <td>page</td>
        <td>int</td>
        <td>当前页（默认第一页）</td>
    </tr>
    </tbody>
</table>

### 分页响应的参数


## 总共的接口列表
### 1、系统模块
* [1、1 轮播图接口](./system/slider_list.md)
* [1、1 轮播图接口](./system/slider_list.md)

### 2、 景点模块
