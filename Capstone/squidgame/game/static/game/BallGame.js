if(!localStorage.getItem('turn')){
    localStorage.setItem('turn',0);
}
if(!localStorage.getItem('computer_ball_n')){
    localStorage.setItem('computer_ball_n',10);
}
if(!localStorage.getItem('user_ball_n')){
    localStorage.setItem('user_ball_n',10);
}

var turn = parseInt(localStorage.getItem('turn'));
var computer_ball_n = parseInt(localStorage.getItem('computer_ball_n'));
var user_ball_n = parseInt(localStorage.getItem('user_ball_n'));
if (turn > 1 || turn < 0 ){
    turn = 0;
    computer_ball_n = 10;
    userball_n = 10;
    //console.log(turn);
}
if (computer_ball_n < 0 || computer_ball_n > 20){
    computer_ball_n = 10;
}
if (user_ball_n < 0 || user_ball_n > 20){
    user_ball_n = 10;
}

var computer_ball_select = 0;
var guess = false;
var computer_ball_text = "";
var user_ball_text = "";
var even_button = "";
var odd_button = "";
var user_ball_select = 0;
var user_ball_select_bar = "";
var user_ball_select_button = "";
var game_container = "";


document.addEventListener('DOMContentLoaded', function(){

    game_container = document.querySelector('#game-container');

    computer_ball_text = document.querySelector("#computer-ball");
    user_ball_text = document.querySelector("#user-ball");

    user_ball_select_bar = document.querySelector('#user-ball-select');
    
    user_ball_select_button = document.querySelector('#select');
    user_ball_select_button.addEventListener('click', function() {
        user_ball_select = parseInt(user_ball_select_bar.value);
        //console.log(user_ball_select);
        var computer_guess = getRandomInt(1);
        if (computer_guess === 0){
            guess = GuessCheck(user_ball_select,true);
        }
        else{
            guess = GuessCheck(user_ball_select,false);
        }
        TurnChange(guess);
    });

    even_button = document.querySelector("#even");
    even_button.addEventListener('click', function(){
        guess = GuessCheck(computer_ball_select,true);
        //console.log(guess);
        TurnChange(guess);
    });
    odd_button = document.querySelector("#odd");
    odd_button.addEventListener('click', function(){
        guess = GuessCheck(computer_ball_select,false);
        //console.log(guess);
        TurnChange(guess);
    });

    PageUpdate();
    fade('container',true);
});

function fade(e,d) {
    let id = null;
    const elem = document.getElementById(e);   
    //let pos = 0;
    let op = 0;
    let f_op = 100;
    if(d)
    {
        op = 0;
        f_op = 100;
    }
    else{
        op = 100;
        f_op = 0;
    }
    clearInterval(id);
    id = setInterval(frame, 15);   
    
    function frame() {
        if (op == f_op) {
        clearInterval(id);
        } else {
        if(d){
            op++;
        }
        else{
            op--;
        }         
        elem.style.opacity = op + "%"; 
        }
    }
  }

function PageUpdate(){
    //Controllo se c'è un vincitore
    if(computer_ball_n <= 0){
        computer_ball_n = 0;
        fade('container', false);
        setTimeout(function(){
            game_container.innerHTML = "";
            document.querySelector('#Welcome').innerHTML = "";
            end = document.createElement('h1');
            end.innerHTML = "User Win";
            game_container.append(end);
            fade('container', true);
        },3000);        
        turn = 2;
        localStorage.clear();                        
    }
    else if(user_ball_n <= 0){
        user_ball_n = 0;
        fade('container', false);
        setTimeout(function(){
            game_container.innerHTML = "";
            document.querySelector('#Welcome').innerHTML = "";
            end = document.createElement('h1');
            end.innerHTML = "User Lose";
            game_container.append(end);
            fade('container', true);
        },3000);        
        turn = 2;
        localStorage.clear();               
    }
    else{
        //aggiorno quantità di biglie
        computer_ball_text.innerHTML = "Computer: " + computer_ball_n + " ball";
        const value = JSON.parse(document.getElementById('user').textContent);
        user_ball_text.innerHTML = value + ": " + user_ball_n + " ball";
    }   

    // turn = 0 è il turno di user, turn = 1 è il turno di computer
    if (turn === 0){
        //è il turno di user
        //console.log("è il turno di user");
        even_button.style.display = 'inline';
        odd_button.style.display = 'inline';
        user_ball_select_bar.style.display = 'none';
        user_ball_select_button.style.display = 'none';        

        computer_ball_select = getRandomInt(computer_ball_n);
        if (computer_ball_select === 0){
            computer_ball_select = 1;
        }
        //console.log("Computer select " + computer_ball_select);
    }
    else if (turn === 1){
        //Se è il turno di computer 
        //console.log("è il turno di computer");
        even_button.style.display = 'none';
        odd_button.style.display = 'none';
        user_ball_select_bar.max = user_ball_n;
        user_ball_select_bar.style.width = (user_ball_select_bar.max * 15) + "px";
        datalist = document.querySelector('#tickmarks');
        datalist.innerHTML = "";
        for (let i = 1; i <= user_ball_n; i++){
            option = document.createElement('option');
            option.value = i;
            option.label = i;
            datalist.append(option);
        }
        user_ball_select_bar.style.display = 'inline';
        user_ball_select_button.style.display = 'inline';
    }
}

function TurnChange(guess){
    if(turn === 0){
        //turno di user
        if(guess){
            //console.log (computer_ball_n);
            //console.log (user_ball_n);
            computer_ball_n = computer_ball_n - computer_ball_select;
            user_ball_n = user_ball_n + computer_ball_select;
            //console.log("user win");
            //console.log (computer_ball_n);
            //console.log (user_ball_n);
        }
        else{
            //console.log (computer_ball_n);
            //console.log (user_ball_n);
            computer_ball_n = computer_ball_n + computer_ball_select;
            user_ball_n = user_ball_n - computer_ball_select;
            //console.log("user lose");
            //console.log (computer_ball_n);
            //console.log (user_ball_n);
        }
        turn = 1;
    }
    else if (turn === 1) {
        //turno di computer
        if(guess){
            //console.log (computer_ball_n);
            //console.log (user_ball_n);
            user_ball_n = user_ball_n - user_ball_select;
            computer_ball_n = computer_ball_n + user_ball_select;
            
            //console.log("computer win");
            ////console.log (user_ball_select);
            //console.log (user_ball_n);
            //console.log (computer_ball_n);
        }
        else{
            //console.log (computer_ball_n);
            //console.log (user_ball_n);
            user_ball_n = user_ball_n + user_ball_select;
            computer_ball_n = computer_ball_n - user_ball_select;
            //console.log("computer lose");
            //console.log (computer_ball_n);
            //console.log (user_ball_n);
        }
        turn = 0;
    }

    localStorage.setItem('turn',turn);
    localStorage.setItem('computer_ball_n',computer_ball_n);
    localStorage.setItem('user_ball_n',user_ball_n);

    setTimeout(PageUpdate,300);
    //PageUpdate();
}


function getRandomInt(max) {
    return Math.floor(Math.random() * max);
  }

function GuessCheck(ball_selected,guess){ 
    // even_odd true = pari(even), false = dispari(odd)
    let even_odd = false;
    if ((ball_selected % 2) == 0){
        even_odd = true;
    }
    else{
        even_odd = false;
    }
    if (even_odd === guess){
        return true;
    }
    else{
        return false;
    }
}