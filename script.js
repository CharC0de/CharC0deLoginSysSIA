//document.querySelectorAll('.col')[0].querySelector('form').querySelector('input[name="username"]').value

const inp = document.getElementById('searchBar')
const colList = document.querySelectorAll('.col');


inp.addEventListener('keyup', () => {
    colList.forEach(col => {
        let nameVal= col.querySelector('form').querySelector('input[name="username"]').value
        if((nameVal.substring(0,nameVal.length-(nameVal.length-inp.value.length)).toUpperCase()!==inp.value.toUpperCase()) && inp.value.length>0){
            col=col.style.display = 'none'
        }
        else{
            col=col.style.display = 'block'
        }
    })
})

