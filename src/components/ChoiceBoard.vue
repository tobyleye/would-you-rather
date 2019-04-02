<template>
	<div class="choice-board">
		<button @click="chooseOption(1)"
			class="choice" :disabled="selected">
			{{ question.options[0].text }}
			<span v-if="selected == 1" class="selected">
				<i class="fas fa-check"></i>
			</span>
		</button>
		<button @click="chooseOption(2)"
			class="choice" :disabled="selected">
			{{ question.options[1].text }}
			<span v-if="selected == 2" class="selected">
				<i class="fas fa-check"></i>
			</span>
		</button>
		<div class="choice-separator">or</div>
		<div v-show="selected" 
			class="results">
			<div :style="`width: ${question.options[0].votes}%`">{{ `${question.options[0].votes}%`	 }}</div>
			<div :style="`width: ${question.options[1].votes}%`">{{ `${question.options[1].votes}%` }}</div>
		</div>
	</div>
</template>

<script>
	export default {
		name: 'ChoiceBoard',
		props: {
			question: Object,
		},
		data() {
			return {
				selected: undefined,
			}
		},
		watch: {
			question() {
				this.selected = undefined;
			}
		},
		methods: {
			chooseOption(option) {
				this.selected = option;
				this.$emit('vote');
			}
		}
	}
</script>

<style>
	.choice-board {
		background: #fff;
		flex: 1;
		max-width: 620px;
		width: 100%;
		position: relative;
		display: flex;
		flex-direction: column;
		padding: 18px 12px;
		border-radius: 20px;
		box-shadow: 0px 8px 2px 2px rgba(0,0,0,.3);
	}

	.choice {
		border: 0;
		position: relative;
		display: flex;
		flex: 1;
		border-radius: 12px;
		justify-content: center;
		align-items: center;
		padding: 20px;
		color: #fff;
		font-size: 18px;
		text-align: center;
		font-weight: 800;
		line-height: 1.2;
		cursor: pointer;
		font-family: 'Nunito', 'Helvetica', sans-serif;
		/* disable blue highlight on screen touch/press */
		-webkit-tap-highlight-color: rgba(0,0,0,0);
		-webkit-tap-highlight-color: transparent;
	}

	.choice .selected {
		position: absolute;
		font-size: 14px;
		right: 12px;
		bottom: 22px;
		width: 30px;
		height: 30px;
		color: #fff;
		display: inline-flex;
		justify-content: center;
		align-items: center;
		background: rgba(0,0,0,.2);
		border-radius: 100%;
	}

	.choice:nth-child(1) {
		margin-bottom: 20px;
		background: #f64b85;
	}

	.choice:nth-child(2) {
		background: #803df7;
	}

	.choice:nth-child(1):active {
		background: #e64d81;
	}

	.choice:nth-child(2):active {
		background: #673ab7;
	}

	.choice-separator {
		display: inline-flex;
		justify-content: center;
		align-items: center;
		border-radius: 100%;
		width: 45px;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		height: 45px;
		background: #fff;
		position: absolute;
		font-weight: 800;
		font-size: 18px;
		color: #444;
		box-shadow: 0px 5px 2px 2px rgba(0,0,0,.2)
	}

	.results {
		position: absolute;
		width: 80%;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		height: 50px;
		border: 3px solid #fff;
		border-radius: 12px;
		display: flex;
		/*z-index: 100;*/
		box-shadow: 0px 5px 2px 2px rgba(0,0,0,.2);
	}

	.results div {
		color: #fff;
		display: flex;
		font-weight: 800;
		justify-content: center;
		align-items: center;
		}

	.results div:first-child {
		background: #f64b85;
		border-bottom-left-radius: 9px;
		border-top-left-radius: 9px;
	}

	.results div:last-child {
		background: #803df7;
		border-top-right-radius: 9px;
		border-bottom-right-radius: 9px;
	}
</style>