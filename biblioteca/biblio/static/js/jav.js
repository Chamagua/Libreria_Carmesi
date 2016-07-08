/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */



var user=prompt("Ingrese su nombre");
var pass=prompt("Ingrese su contraseña");

while(user!=="admin"&& pass!=="admin")
{
    var user=prompt("Ingrese su nombre");
    var pass=prompt("Ingrese su contraseña");
}

alert("Bienvenido"+user);
sayHello("\n\n Martin");
sayHello("\n\n Gatoman");
sayHello("\n\n Danonino");

function sayHello(name){
   document.write("hi"+ name+"\n");
   document.write("CODIGO JAVASCRIPT")
}





