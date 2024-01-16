//
// index.js
//


import { hello_world } from './functions.js';


function component() {
  const element = document.createElement('div');
  element.innerHTML = hello_world();
  return element;
}

document.body.appendChild(component());

 
