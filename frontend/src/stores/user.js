import {defineStore} from "pinia";
import {ref} from "vue";

export const useUserStore =defineStore('user',()=>{
    const id=ref(1)
    const username=ref('wyh')
    const photo=ref('http://127.0.0.1:8000/media/user/photos/default.jpg')
    const profile=ref('111')
    const accessToken=ref('111')

// (a,b,c) =>{
//
// }匿名函数：等价于定义了如下的一个函数
//
// function foo(a,b,c){
//
// }

    function isLogin(){
        return !!accessToken.value //!!:看后面是不是空的，空的是false 非空是true  必须带value！！！！不然永远不空 永远登录
    }

    function setAccessToken(token){
        accessToken.value=token
    }

    function setUserInfo(data){
        id.value = data.user_id
        username.value=data.username
        photo.value=data.photo
        profile.value=data.profile
    }
    function logout(){
        id.value=0
        username.value=''
        photo.value=''
        profile.value=''
        accessToken.value=''
    }

    return{
        id,
        username,
        photo,
        profile,
        accessToken,//千万不要忘了！！
        setAccessToken,
        setUserInfo,
        logout,
        isLogin,
    }
})

