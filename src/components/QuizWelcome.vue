<template>
	<div style="height: inherit">
		<div class="welcome-block">
			<h3 class="welcome-title">Would<br>you rather</h3>
			<div>
				<button class="btn btn-play" @click="play">Play!</button>
				<button @click="showDetails=true" class="btn btn-details">This is pointless</button>
			</div>
		</div>
		<WelcomeDetails
			@close="showDetails=false"
			v-if="showDetails"/>
	</div>
</template>

<script>
	import { store } from '../store.js';
	import WelcomeDetails from './WelcomeDetails.vue'

	export default {
		name: 'QuizWelcome',
		components: {
			WelcomeDetails
		},
		data() {
			return {
				showDetails: false,
			}
		},
		methods: {
			play() {
				store.nextMode()
			}
		}
	}
</script>

<style>
	.welcome-block {
		height: inherit;
		padding: 0 16px;
		display: flex;
		text-align: center;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
	.welcome-title {
		font-size: 40px;
		line-height: 1.2;
		color: #fff;
		font-family: 'Pacifico', cursive;
		letter-spacing: 2px;
		text-shadow: 3px 3px 2px #f64b85;
		margin-bottom: 40px;
	}
	.btn {
		display: inline-block;
		padding: 10px 22px;
		border: 3px solid #fff;
		border-radius: 22px;
		cursor: pointer;
		color: #fff;
		font-weight: 600;
		font-size: 16px;
		letter-spacing: .5px;
		font-family: 'Nunito', 'Helvetica', sans-serif;
	}
	.btn-play {
		background-color: #803df7;
		margin-right: 5px;
	}
	.btn-details {
		background-color: #f64b85;
	}
</style>