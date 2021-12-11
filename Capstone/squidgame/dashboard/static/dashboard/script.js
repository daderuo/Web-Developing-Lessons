document.addEventListener('DOMContentLoaded', function() {

    // Use buttons to toggle between views
    document.querySelector('#home').addEventListener('click', () => load_view('home'));
    document.querySelector('#ranking').addEventListener('click', () => load_view('ranking'));
  
    // By default, load home
    load_view('home');
  
  });


  function load_view(view){
    game_view = document.querySelector('#game-view');
    ranking_view = document.querySelector('#ranking-view');


    if (view === 'home'){
        game_view.style.display = 'block';
        ranking_view.style.display = 'none';
        load_game_list();
    }
    else if (view === 'ranking'){
        game_view.style.display = 'none';
        ranking_view.style.display = 'block';
    }
}

function load_game_list(){
    fetch(`/games`)
    .then(response => response.json())
    .then(g => {
        g.forEach(a);   
    });
}

function a(g){
    console.log(g);
    console.log(g.name);
    console.log(g.single_player);
    console.log(g.multiplayer);

    game = document.createElement('div');
    game.className = 'game';
    title = document.createElement('h4');
    title.className = 'game-title';
    title.innerHTML = g.name;
    game.append(title);
    document.querySelector('#game-list').append(game);
}