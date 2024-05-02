//  ! SWIPER JS CODES ! \\

const swiper = new Swiper('.swiper', {

  loop: true,


effect:'cube',
grabCursor : true,
cubeEffect: {
shadow :true,
slideShadows:true,
shadowOffset:2,
shadowScale:0.1,
},


  pagination: {
    el: '.swiper-pagination',
  },


  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },


  scrollbar: {
    el: '.swiper-scrollbar',
  },
});


//  ! FOOTER POP OVERS JQUERY + BOOTSTRAP CODES ! \\

$(document).ready(function(){
$('[data-toggle="popover"]').popover();
});

// !!! DARK MODE LIGHT MODE CONST !!! \\


const changecolor = document.getElementById('toggleDark')



const body = document.querySelector('body')


//  !DARK MODE LIGHT MODE CODE ! \\


changecolor.addEventListener('click', function(){

    this.classList.toggle('bi-moon')


    if(this.classList.toggle('bi-emoji-sunglasses')){

        body.style.background ='white'

    }else{

        body.style.background ='black'

    }

})



// !! VARIABLES !! \\

const fromCur = document.querySelector(".from select");
const toCur = document.querySelector(".to select");
const getBtn = document.querySelector("form button");
const exIcon = document.querySelector("form .reverse");
const amount = document.querySelector("form input");
const exRateTxt = document.querySelector("form .result");



// !! EVENT LISTENERS FOR SELECT !! \\

[fromCur, toCur].forEach((select, i) => {
    for (let curCode in Country_List) {
        const selected = (i === 0 && curCode === "USD") || (i === 1 && curCode === "GBP") ? "selected" : "";
        select.insertAdjacentHTML("beforeend", `<option value="${curCode}" ${selected}>${curCode}</option>`);
    }
    select.addEventListener("change", () => {
        const code = select.value;
        const imgTag = select.parentElement.querySelector("img");
        imgTag.src = `https://flagcdn.com/48x36/${Country_List[code].toLowerCase()}.png`;
    });
});

// !! API FUNCTION !! \\

async function getExchangeRate() {
    const amountVal = amount.value || 1;
    exRateTxt.innerText = "Getting exchange rate...";
    try {
        const response = await fetch(`https://v6.exchangerate-api.com/v6/b937a96007775fa59b350a83/latest/${fromCur.value}`);
        const result = await response.json();
        const exchangeRate = result.conversion_rates[toCur.value];
        const totalExRate = (amountVal * exchangeRate).toFixed(2);
        exRateTxt.innerText = `${amountVal} ${fromCur.value} = ${totalExRate} ${toCur.value}`;
        exRateTxt.classList.add('text-primary');
    } catch (error) {
        exRateTxt.innerText = "Something went wrong...";
    }
}

// !! EVENT LISTENERS FOR BUTTON AND EXCHANGE ICON CLICK !! \\

window.addEventListener("load", getExchangeRate);
getBtn.addEventListener("click", (e) => {
    e.preventDefault();
    getExchangeRate();
});

exIcon.addEventListener("click", () => {
    [fromCur.value, toCur.value] = [toCur.value, fromCur.value];
    [fromCur, toCur].forEach((select) => {
        const code = select.value;
        const imgTag = select.parentElement.querySelector("img");
        imgTag.src = `https://flagcdn.com/48x36/${Country_List[code].toLowerCase()}.png`;
    });
    getExchangeRate();
});


// ! PROFILE PAGE ANIMATION JS ! \\

$('.toggle-button').on('click', function() {
    $('.left-sidebar').toggleClass('minimize'); 
  });
  
  $('.user-profile').on('click', function() {
    $('.left-sidebar').toggleClass('minimize'); 
  });
  
  $('.close-chat-btn').on('click', function() {
    $('.direct-messaging ').addClass('minimize'); 
  });
  
  $('.open-chat-btn').on('click', function() {
    $('.direct-messaging ').toggleClass('minimize'); 
  });
  
  $('.open-music-btn').on('click', function() {
    $('.music-player').toggleClass('show'); 
  });
  
  $('.open-timer-btn').on('click', function() {
    $('.timer-display').toggleClass('show'); 
  });