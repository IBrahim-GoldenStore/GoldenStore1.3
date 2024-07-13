document.addEventListener('DOMContentLoaded',function() {
    // menu deroulant
    const nav= document.querySelector('header nav')
    const menu_bar= document.querySelector('.menu-bar') //  selection de "menu_list"
    menu_bar.onclick= function(){    // on ajoute a menu_list un ajouteur d'un evenement ".onclick" ensuite on definie une fonction pour reagir dondc tout les scripts suivant n'agisse que si l'evenement se produit 
        menu_bar.classList.toggle("active")  // ".classList.toggle("nom_selecteur_css") ajoute la classe  specifie comme argument si elle est presente sinon elle l'enleve"
        nav.classList.toggle('menu')
    }
    
})


document.addEventListener('DOMContentLoaded',function(){
    const btn= document.querySelector('.form_btn')
    const form= document.querySelector('.form')
    btn.onclick= function(){
        form.classList.toggle('active_form')
    }
})