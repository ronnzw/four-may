    //Navbar js
    let currentLocation = location.href;
    let navBarItem = document.getElementsByClassName('nav-link');
    

    for(let i = 0; i < navBarItem.length; i++){
        if(navBarItem[i].href == currentLocation){
            navBarItem[i].classList.add('active')
        }
        
    }