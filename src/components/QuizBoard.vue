<template>
	<div class="quiz-board">
		<div class="header">
			<button @click="previousMode" class="btn-home">
				<i class="fas fa-arrow-left"></i>
			</button>
			<h2>Would<br>You Rather</h2>
			<div></div>
		</div>
		<ChoiceBoard
			:question="questions[sharedState.currentQuestionIndex]"
			@vote="isVoted=true"/>
		<div class="footer">
			<button @click="nextQuestion" class="btn btn-next">Next</button>
		</div>

		<!-- 
			Todo: 
				- Move to seperate template
		-->
		<QuizModal v-show="error" @close="error = false">
			<div class="choice-error">
				<p>Please make a choice to go the next question</p>
				<button @click="error = false" class="modal-btn">ok</button>
			</div>
		</QuizModal>

		<!-- 
			Todo: 
				- Move to seperate template
		-->
		<QuizModal v-show="quizEnd" @close="quizEnd=false">
			<div class="quiz-end">
				<h2><span class="crown">👑</span><br>Congratulations</h2>
				<p>You finished answering all the questions. wow! you're really jobless, well in the meantime go do something productive.... or not.</p>
				<div style="margin: 30px 0 20px;">
					<button class="modal-btn" @click="resetQuiz">Play Again</button>
				</div>
			</div>
		</QuizModal>
	</div>
</template>

<script>
	import { store } from '../store.js';
	import questions from '../questions.json';

	import ChoiceBoard from './ChoiceBoard.vue';
	import QuizModal from './QuizModal.vue';


	export default {
		name: 'QuizBoard',
		components: {
			ChoiceBoard,
			QuizModal
		},
		data() {
			return {
				questions,
				isVoted: false,
				error: false,
				quizEnd: false,
				sharedState: store.state,
				currentQuestionIndex: store.state.currentQuestionIndex
			}
		},
		methods: {
			previousMode() {
				store.previousMode();
			},
			nextQuestion() {
				if (!this.isVoted) return this.error = true;
				if (this.sharedState.currentQuestionIndex == this.questions.length - 1) return this.quizEnd = true;
				
				store.nextQuestion()
				this.isVoted = false
			},
			resetQuiz() {
				this.quizEnd = false;
				store.resetLevel()
				this.isVoted = false;
			}
		}
	}
</script>

<style>
	.quiz-board {
		height: inherit;
		display: flex;
		flex-direction: column;
		padding: 0 25px;
		align-items: center;
	}
	.btn-next {
		background: transparent;
		color: #fff;
		font-size: 14px;
		padding: 8px 30px;
		text-transform: uppercase;
	}
	.header {
		text-align: center;	
		margin: 20px 0 12px;
		display: flex;
		width: 100%;
		justify-content: space-between;
		align-items: center;
	}
	.header h2 {
		line-height: 1.2;
		color: #fff;
		font-size: 26px;
		font-family: 'Pacifico', cursive;
		text-shadow: -5px -5px 8px rgba(0,0,0,.2), 
			5px 5px 8px rgba(0,0,0,.2);
		letter-spacing: 1px;
	}
	.footer {
		margin: 12px 0 20px;
	}
	.btn-home {
		border: 0;
		display: inline-block;
		background: none;
		color: #fff;
		cursor: pointer;
		font-size: 24px;
		font-weight: 900;
	}
	.back {
		font-size: 20px;
	}
	.choice-error, .quiz-end {
		text-align: center;
	}
	.choice-error p {
		font-size: 16px;
		color: #444;
		margin-bottom: 14px;
	}
	.crown {
		font-size: 55px;
		line-height: 1.2;
	}
	.choice-error button {
		padding: 4px 15px;
		font-size: 14px;
	}
	.quiz-end h2 {
		font-size: 25px;
		margin-bottom: 20px;
		letter-spacing: 1px;
		color: #673ab7;
		font-family: 'Pacifico', cursive;
	}
	.quiz-end p {
		text-align: center;
		color: #9e9e9e;
		font-size: 16px;
	}
	.quiz-end button {
		padding: 8px 20px;
	}
</style>