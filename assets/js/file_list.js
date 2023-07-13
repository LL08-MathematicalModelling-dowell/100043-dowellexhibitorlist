console.log('hello world')

const modalBtns = [...document.getElementsByClassName('modal-button')]
const startBtn = document.getElementById('delete_button')

const url = "http://100043.pythonanywhere.com/exhibitors/files/delete/"

modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click', ()=>{
    const id = modalBtn.getAttribute('data-id')

    startBtn.addEventListener('click', ()=>{
        window.location.href = url + id
    })
}))