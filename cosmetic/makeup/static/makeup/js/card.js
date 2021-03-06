var updateBtn=document.getElementsByClassName('updated-cart')

for(i=0; i< updateBtn.length;i++){
    updateBtn[i].addEventListener('click',function(){
        var productId=this.dataset.product
        var action=this.dataset.action
        console.log('productId: ',productId,'action: ',action)
        console.log('User: ',user)
        if(user==='AnonymousUser'){
            console.log('Not Log In')
        }else{
            updateUserOrder(productId,action)
        }
    })
}


function updateUserOrder(productId,action){
    console.log('User is logged in, sending data...')

    var url='/updateItem/'

    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId': productId,'action': action})
    })

    .then((response) =>{
        return response.json()
    })

     .then((data) =>{
        console.log('data: ',data);
//        location.reload();

    });
}