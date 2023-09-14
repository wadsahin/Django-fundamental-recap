let container = document.querySelector('.container');
let btn = document.querySelector('button');
btn.addEventListener('click', effectFun);


function effectFun(){
    let div = document.createElement('div');
    let h4  = document.createElement('h4');
    h4.className = 'heading-4';
    h4.innerHTML = 'Sahin Alom is a Web Application Developer';
    div.appendChild(h4);
    container.appendChild(div)
    

}