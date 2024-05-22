let naam = '';

window.addEventListener('load',onLoad);
//alert('ingeladen!');
function onLoad(){
   // const divResult = document.getElementById('divResult');
    document.getElementById('buttonRes').addEventListener ('click',function () {
        const naam = document.getElementById('txtNaam').value;
        const naamA = naam.length;
        const check = (naamA<2)
            ? 'Sorry, ik heb u niet goed begrepen, uw naam moet langer zijn dan 2 tekens.'
                : (naamA>2)
                ? 'Welkom op deze pagina, ' + naam 
                    : 'u heeft maar 2 tekens ingevuld, dit is te weinig voor mij'
                    alert(check)
        divResult.innerHTML = check
    });
}
