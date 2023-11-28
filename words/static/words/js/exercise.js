new Vue({
	delimiters: ['[[', ']]'],
	el: '#word',	
	data: {
		word:'Kolbasa',
		// letters:[],
		// voices:{},
		// entered_letter:'',
		// actual_position:0,
		// number_letters:100,
		// imgEnd:'http://192.168.1.3:8000/media/games/img/romashka.png',
		// theEnd:false,
	},
	created: function (){
		const vm=this;
		const myWord="колбаса";
		vm.word = response.data[0];
		vm.number_letters=vm.word.name.toUpperCase().length;
		for (const item of vm.word['letters']){
			vm.voices[item['name']]=item['voice'];
		}

	},

})