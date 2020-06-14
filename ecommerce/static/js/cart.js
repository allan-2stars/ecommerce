const updateBtns = document.getElementsByClassName('update-cart')
console.log(updateBtns)
for (let i=0; i<updateBtns.length;i++){
    updateBtns[i].addEventListener('click', function(){
        productId = this.dataset.product
        action = this.dataset.action
        console.log('productId:',productId, 'action:', action)

        console.log('USER:', user)
        if (user == 'AnonymousUser'){
            console.log('User is not authenticated')
        }else{
            console.log('User is authenticated, sending data ...')
        }
    })
}


