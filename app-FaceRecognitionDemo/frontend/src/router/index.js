import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

import RecogOldFace from '@/components/RecogOldFace';

import AddNewFace from '@/components/AddNewFace'

Vue.use(Router);

// Vue.http.options.emulateJson=true

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld,
    },
    {
      path: '/RecogOldFace',
      name: 'RecogOldFace',
      component: RecogOldFace
    },
    {
      path: '/AddNewFace',
      name: 'AddNewFace',
      component: AddNewFace
    }

  ]
})
