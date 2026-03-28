<script setup>
import {useRoute, useRouter} from "vue-router";

const route =useRoute() //取当前url的信息 即user_id
const router=useRouter() //打开一个新页面


</script>

<template>
个人空间:{{route.params.user_id}}
</template>

<style scoped>

</style>