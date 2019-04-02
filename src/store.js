export const store = {
	state: {
		mode: JSON.parse(localStorage.getItem('mode')) || 1, // screen mode
		currentQuestionIndex: JSON.parse(localStorage.getItem('current_level')) || 0
	},
	nextMode() {
		this.state.mode += 1;
		localStorage.setItem('mode', this.state.mode);
	},
	previousMode() {
		this.state.mode -= 1;
		localStorage.setItem('mode', this.state.mode);
	},
	resetLevel() {
		this.state.currentQuestionIndex = 0;
		localStorage.setItem('current_level', this.state.currentQuestionIndex);
	},
	nextQuestion() {
		this.state.currentQuestionIndex+= 1;
		localStorage.setItem('current_level', this.state.currentQuestionIndex);
	}
}