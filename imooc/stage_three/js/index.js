let provinces = [
    {
        name: '北京市',
        cities: ['朝阳区', '西城区']
    },
    {
        name: '河北省',
        cities: ['石家庄', '邯郸市']
    },
    {
        name: '天津市',
        cities: ['西青区', '武清区']
    },
    {
        name: '河南省',
        cities: ['郑州市', '开封市']
    },
];

function init() {
    let provinceDOM = document.getElementById('province');
    let cityDOM = document.getElementById('city');
    provinceDOM.options.add(new Option('-- 请选择 --'));
    cityDOM.options.add(new Option('-- 请选择 --'));
    provinces.forEach(function (province) {
        provinceDOM.options.add(new Option(province.name));
    })
}

/**
 * 目的：当省份被选择的时候，要修改省份下面对应的城市列表
 * 1、获取当前被选择的省份
 * 2、把对应的城市列表添加到对应的省份下面
 *  （1）要拿到对应的省份下面有哪些城市
 *  （2）往列表中添加城市
 */
function onSelected() {
    let selectedDOM = document.getElementById('province');
    let selectedIndex = selectedDOM.selectedIndex;
    let selectedProvince = selectedDOM.options[selectedIndex].text;

    let cityDOM = document.getElementById('city');
    cityDOM.options.length = 0;
    cityDOM.options.add(new Option('-- 请选择 --'))

    provinces.forEach(function (province) {
        if (selectedProvince === province.name) {
            province.cities.forEach(function (city) {
                cityDOM.options.add(new Option(city))
            })
        }
    })

    // for (let index in provinces){
    //     if(provinces.hasOwnProperty(index)){
    //         console.log(provinces[index].name)
    //     }
    // }

    // for (let i = 0; i < provinces.length; ++i) {
    //     console.log(provinces[i].name)
    //     console.log(provinces[i].cities)
    // }

}
