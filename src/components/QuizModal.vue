<template>
	<div class="modal-overlay">
		<div class="modal"> 
			<div class="modal-header">
				<button @click="close" class="modal-close">&times;</button>
			</div>
			<div class="modal-content">
				<slot></slot>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		name: 'QuizModal',
		methods: {
			close() {
				this.$emit('close');
			}
		}
	}
</script>

<style>
	.modal-overlay {
		position: fixed;
		z-index: 1;
		left: 0;
		top: 0;
		padding: 0 22px;
		width: 100%;
		height: 100%;
		overflow: auto;
		display: flex;
		justify-content: center;
		align-items: center;
		background-color: rgba(0,0,0,.66);
	}
	.modal {
		width: 100%;
		max-width: 500px;
		margin: 0 auto;
		z-index: 1000;
	}
	.modal-content {
		background: #fff;
		border-radius: 5px;
		padding: 18px 14px;
		box-shadow: 0 6px #ccc;
	}	
	.modal-header {
		text-align: right;
		padding-right: 12px;
		margin-bottom: 5px;
	}
	.modal-close {
		display: inline-block;
		background: none;
		color: #ccc;
		font-weight: 400;
		font-size: 28px;
		border: none;
		cursor: pointer;
	}
	.modal-btn {
		border: 0;
		position: relative;
		display: inline-block;
		top: 0;
		padding: 12px 30px;
		background: #673ab7;
		cursor: pointer;
		color: #fff;
		font-weight: 600;
		font-size: 14px;
		text-transform: uppercase;
		border-radius: 8px;
		box-shadow: 0 6px #472582;
		transition: .2s ease;
		font-family: 'Nunito', 'Helvetica', sans-serif;
	}
	.modal-btn:active {
		top: 4px;
		box-shadow: 0 0px #472582;
	}

</style>