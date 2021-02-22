//Capturando el evento submit (envío del formulario)
const form = document.getElementById('transactionForm')
//console.log(form)
//Detectando el evento submit (cuando se presiona agregar)
form.addEventListener('submit', function(event){
        //console.log(event);
        //alert('Se detecto un envio del formulario')
        
        //Evitando que se recargue la página con el evento
        //y que se envíe el formulario al servidor
        event.preventDefault();
        //Obteniendo los datos del formulario
        let transactionFormData = new FormData(form)
        //Convirtiendo los datos del FormData en un objeto
        let transactionObj = convertFormDataToTransactionObj(transactionFormData)
        //Guardando los datos en el Local Storage
        saveTransactionObj(transactionObj)
        //Insertando la fila en la tabla
        insertRowInTransactionTable(transactionObj)

        //Borrando los datos del formulario que ya se agregaron a la tabla
        form.reset()
    }
)

//Detectando el evento DOMContentLoaded (cuando el documento html ha sido completamente cargado y parseado)
document.addEventListener('DOMContentLoaded', function(event){
        //Convirtiendo en array el objeto en el Local storage
        let transactionObjArr = JSON.parse(localStorage.getItem('transactionData')) || []
        //Se recorre cada elemento del array
        transactionObjArr.forEach(function(arrElement){
            //Se inserta en la tabla la fila actual
            insertRowInTransactionTable(arrElement)
        });
    }
)

function getNewTransactionId(){
    //Obteniendo el Id desde el local storage, si es vacío se le asigna -1
    let lastTransactionId = localStorage.getItem('lastTransactionId') || '-1'
    //Sumando 1 al Id
    let newTransactionId = JSON.parse(lastTransactionId) + 1
    //Guardando en el local storage
    localStorage.setItem('lastTransactionId', JSON.stringify(newTransactionId))
    
    return newTransactionId
}

function convertFormDataToTransactionObj(transactionFormData){
    let transactionType = transactionFormData.get('transactionType')
    let transactionAmount = transactionFormData.get('transactionAmount')
    let transactionCategory = transactionFormData.get('transactionCategory')
    let transactionDescription = transactionFormData.get('transactionDescription')
    let transactionId = getNewTransactionId()

    return {
        "transactionType": transactionType, 
        "transactionAmount": transactionAmount, 
        "transactionCategory": transactionCategory, 
        "transactionDescription": transactionDescription,
        "transactionId": transactionId
    }
}

function insertRowInTransactionTable(transactionObj){

    //Obteniendo referencia de la tabla
    let transactionTableRef = document.getElementById('transactionTable')
    //Insertando nueva fila a la tabla
    let newTransactionRowRef = transactionTableRef.insertRow(-1)
    newTransactionRowRef.setAttribute('data-transaction-id', transactionObj['transactionId'])
    //Insertando las celdas en esa fila
    let newTypeCellRef = newTransactionRowRef.insertCell(0)
    newTypeCellRef.textContent = transactionObj['transactionType']

    newTypeCellRef = newTransactionRowRef.insertCell(1)
    newTypeCellRef.textContent = transactionObj['transactionAmount']

    newTypeCellRef = newTransactionRowRef.insertCell(2)
    newTypeCellRef.textContent = transactionObj['transactionCategory']

    newTypeCellRef = newTransactionRowRef.insertCell(3)
    newTypeCellRef.textContent = transactionObj['transactionDescription']

    let newDeleteCell = newTransactionRowRef.insertCell(4)
    //Creando el botón
    let deleteButton = document.createElement('button')
    //Dándole un texto al botón
    deleteButton.textContent = 'Eliminar'
    //Agregando el botón a la celda
    newDeleteCell.appendChild(deleteButton)

    //Capturando el evento del botón
    deleteButton.addEventListener('click', () => {
        //Accediendo al elemento (botón), luego al td (columna) y luego al tr (fila)
        let transactionRow = event.target.parentNode.parentNode
        //Obteniendo el id de esa fila
        let transactionId = transactionRow.getAttribute('data-transaction-id')
        //Removiendo la fila del html
        transactionRow.remove()
        //Removiendo la fila del local storage
        deleteTransactionObj(transactionId)
    })
}

function deleteTransactionObj(transactionId){
    //Obteniendo todas las transacciones
    let transactionObjArr = JSON.parse(localStorage.getItem('transactionData'))
    //Se busca el índice que se desea eliminar del array
    let transactionIndexInArr = transactionObjArr.findIndex(element => element.transactionId === transactionId)
    //Eliminando el elemento del array
    transactionObjArr.splice(transactionIndexInArr, 1)
    //Convirtiendo el array de transacción a json
    let transactionArrJSON = JSON.stringify(transactionObjArr)
    //Se guarda nuevamente el array en el locar storage
    localStorage.setItem('transactionData', transactionArrJSON)
}

function saveTransactionObj(transactionObj){
    //Revisando si en el Local Storage hay un array y cargándolo
    let myTransactionArr = JSON.parse(localStorage.getItem('transactionData')) || []
    //Añadiendo la transacción a un array
    myTransactionArr.push(transactionObj)
    //Convirtiendo el array de transacción a json
    let transactionArrJSON = JSON.stringify(myTransactionArr)
    //Guardando el array en el Local Store
    localStorage.setItem('transactionData', transactionArrJSON)
}