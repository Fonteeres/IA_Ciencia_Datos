function saludar() {
    alert("HOLA A TODOS");
}

function sumar() {
    
    var v1 = document.getElementById("v1").value;
    var v2 = document.getElementById("v2").value;
    var v3 = parseInt(v1) + parseInt(v2);

    if(isNaN(v3)==true) {
        alert("ERROR: INGRESE NUMEROS");
    }else {
        document.getElementById("v3").value = v3;
    }
}

function generarTabla(valor) {
   var res = "";
   var n = 1;
   while(n<13) {
       res = res + "<h2>" + valor + " x " + n + " = " + valor * n + "</h2>";
       n++;
   }
   document.getElementById("res").innerHTML=res;
}