<template>
	<QuizModal @close="close">
		<div class="welcome-details-block">
			<h2>Would you rather Be a dick OR Play the fucking game?</h2>
			<button class="modal-btn" @click="play">Play Game</button>
		</div>
	</QuizModal>
</template>

<script>
	import { store } from '../store.js';
	import QuizModal from './QuizModal.vue';

	export default {
		name: 'WelcomeDetails',
		components: {
			QuizModal,
		},
		methods: {
			close() {
				this.$emit('close');
			},
			play() {
				this.$emit('close') // close the modal
				store.nextMode();
			}
		}
	}	
</script>

<style>
	.welcome-details-block {
		text-align: center;
	}

	.welcome-details-block h2 {
		font-size: 18px;
		margin-bottom: 25px;
		color: #444;
	}
</style>