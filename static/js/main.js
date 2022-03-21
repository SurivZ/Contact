let btnDelete = document.getElementById('btn-delete');
console.log(btnDelete);

if(btnDelete){
	let btnArray = Array.from(btnDelete);
	btnArray.forEach((btn) => {
		btn.addEventListener('click', (e) => {
			if(!confirm('Are you sure you want to delete it?')){
				e.preventDefault();
			}
		});
	});
}
