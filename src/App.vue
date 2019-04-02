<template>
  <div id="app">
    <QuizWelcome
      v-if="sharedState.mode==1"/>
    <QuizBoard v-else/>
  </div>
</template>

<script>
import QuizWelcome from './components/QuizWelcome.vue';
import QuizBoard from './components/QuizBoard.vue'

import { store } from './store.js'

export default {
  name: 'app',
  components: {
    QuizWelcome,
    QuizBoard,
  },
  data() {
    return {
      sharedState: store.state
    }
  }
}
</script>

<style>
  * {
    margin: 0;
    padding: 0;
    outline: 0;
    box-sizing: border-box;
  }

  html, body {
    height: 100%;
  }

  #app {
    height: inherit;
    font-family: 'Nunito', Helvetica, Arial, sans-serif;
    background-color: #35383a;
    background: url(./assets/bg.png);
    background-size: 50%;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  button {
    /* disable blue highlight on screen touch/press */
    -webkit-tap-highlight-color: rgba(0,0,0,0);
    -webkit-tap-highlight-color: transparent;
  }
</style>
