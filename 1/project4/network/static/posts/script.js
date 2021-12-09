
let paginator_page = 1;


document.addEventListener('DOMContentLoaded', function () {
    var path = window.location.pathname;
    var page = path.split("/");

    paginator_page=1;

    if (page[1] === ""){
        load_10();
        next_button = document.getElementById('NEXT_PAGE');
        next_button.onclick = function(){
            paginator_page = paginator_page + 1;
            clearBox("posts");
            load_10();
        }
        previous_button = document.getElementById('PREVIOUS_PAGE');
        previous_button.onclick = function(){
            paginator_page = paginator_page - 1;
            clearBox("posts");
            load_10();
        }
    }
    if(page[1] == "p_f"){
        load_10_followed();
        next_button = document.getElementById('NEXT_PAGE');
        next_button.onclick = function(){
            paginator_page = paginator_page + 1;
            clearBox("posts");
            load_10_followed();
        }
        previous_button = document.getElementById('PREVIOUS_PAGE');
        previous_button.onclick = function(){
            paginator_page = paginator_page - 1;
            clearBox("posts");
            load_10_followed();
        }
    }   
    if (page[1] === "profile"){
        user = page[2];
        load_profile(user);
        follower_bar(user);
        next_button = document.getElementById('NEXT_PAGE');
        next_button.onclick = function(){
            paginator_page = paginator_page + 1;
            clearBox("posts");
            load_profile();
        }
        previous_button = document.getElementById('PREVIOUS_PAGE');
        previous_button.onclick = function(){
            paginator_page = paginator_page - 1;
            clearBox("posts");
            load_profile();
        }

        
        button = document.getElementById('FOLLOW_BUTTON');
        
        
        button.onclick = function(){
            if (button.innerHTML === "Unfollow"){
                remove_follow(user);
            }
            if (button.innerHTML === "Follow"){
                add_follow(user);
            }
        }
    
    }  
    
    document.addEventListener('click', event =>{
        const element = event.target;

        if (element.className === "like_button"){
            var t = false;
            var l = true;
            post = element.parentElement;
            //console.log(post);
            update_post(post,t,l);            
        }

        if (element.id === "send"){
            var t = true;
            var l = false;
            post = element.parentElement;
            //console.log(post);
            update_post(post,t,l);            
        }

        if (element.id === "edit"){
            post = element.parentElement;
            //console.log(post);
            post.querySelector('#edit').style.display = "none";
            post.querySelector('.text').style.display = "none";
            post.querySelector('#task').style.display = "block";
            post.querySelector('#send').style.display = "block";
        }
    });
    
});

function update_post(post,ut,ul){    
    t = post.querySelector('.text').innerHTML;    
    a = post.querySelector('.AUTHOR').innerHTML;
    d = post.querySelector('.date').innerHTML;
    l = post.querySelector('.like').innerHTML;
  //console.log(ut);
    if (ut){
        new_t = post.querySelector('#task').value;
        //console.log(new_t);
        new_l = l;

        fetch(`/update?a=${a}&t=${t}&d=${d}&l=${l}&new_t=${new_t}&new_l=${new_l}`)
        .then(response => response.json())
        .then(data =>{
            post.querySelector('#edit').style.display = "block";
            post.querySelector('.text').style.display = "block";
            post.querySelector('#task').style.display = "none";
            post.querySelector('#send').style.display = "none";
            post.querySelector('.text').innerHTML = data.post.text;
            post.querySelector('.date').innerHTML = data.post.date;                        
        })
    }
    if(ul){
        new_t = t;
        if (post.querySelector('.like_button').innerHTML === "Like"){
            new_l = l + 1;
        }
        else{
            new_l = l - 1;
        }
        fetch(`/update?a=${a}&t=${t}&d=${d}&l=${l}&new_t=${new_t}&new_l=${new_l}`)
        .then(response => response.json())
        .then(data =>{
            post.querySelector('.like').innerHTML = data.post.like;
            if (data.post.liked){
                post.querySelector('.like_button').innerHTML = "Unlike";
            }
            else{
                post.querySelector('.like_button').innerHTML = "Like";
            }                                   
        })
    }
}

function add_follow(u){
    fetch(`/add_follow?profile=` + u )
    .then(response => response.json())
    .then(data =>{
        follower_bar(u);
    });
}

function remove_follow(u){
    fetch(`/remove_follow?profile=` + u )
    .then(response => response.json())
    .then(data =>{
        follower_bar(u);
    });
}


function follower_bar(u){
    clearBox('F_BAR');

    fetch(`/follow?profile=` + u )
    .then(response => response.json())
    .then(data =>{
        
        //console.log(data);
        const follow_bar = document.createElement('div');
        follow_bar.className = 'FOLLOW';
        follower = document.createElement('h2');    
        follower.innerHTML = "Follower: " + data.follow.follower;
        followed = document.createElement('h2');
        followed.innerHTML = "Following: " + data.follow.followed;

        

        follow_bar.appendChild(follower);
        follow_bar.appendChild(followed);

        var follow_button = document.getElementById("FOLLOW_BUTTON"); 
        //console.log(follow_button);

        if (data.follow.logged && data.follow.myself){            
            follow_button.style.display = "block";
            
            if (data.follow.already=== true){
                follow_button.innerHTML="Unfollow";
            }
            else{
                follow_button.innerHTML="Follow";
            }
        }
        else{
            follow_button.style.display = "none";
        }
        
        //post.appendChild(date);
        //post.appendChild(like);

        document.querySelector('#F_BAR').append(follow_bar);
        
    })
}

function load_profile(u) {
    fetch(`/posts?profile=`+ u)
    .then(response => response.json())
    .then(data =>{
        data.post.forEach(element => {
            const post = document.createElement('div');
            post.className = 'POST';
            author = document.createElement('h1'); 
            author.className = 'AUTHOR';   
            author.innerHTML = element.author;
            //author.href = "profile/"+ author.innerHTML;

            text = document.createElement('h2');
            text.className = "text";
            text.innerHTML = element.text;
            date = document.createElement('h4');
            date.className = "date";
            date.innerHTML = element.date;
            like = document.createElement('h6');
            like.className = "like";
            like.style.display = "inline";
            like.innerHTML = element.like;
            like_text = document.createElement('h6')
            like_text.style.display = "inline";
            if(element.like > 0){
                like_text.innerHTML= " Likes";
            }
            else{
                like_text.innerHTML=" Like";
            }      

            post.appendChild(author);
            post.appendChild(text);

            like_button = document.createElement('button');
            like_button.className = 'like_button';

            //console.log(data.user);
            if (data.user !== ""){
                like_button.style.display = "block";
                if (element.liked){                    
                    like_button.innerHTML = "Unlike";
                }
                else{
                    like_button.innerHTML = "Like";
                }
            }
            else{
                like_button.style.display = "none";
            }

            
            //post.appendChild(form);

            if(element.author === data.user){
                text_area = document.createElement('textarea');
                text_area.value = element.text;
                text_area.id = "task";
                text_area.type = 'text';
                text_area.style.display = "none";
                save_button = document.createElement('button');
                save_button.id = "send";
                save_button.innerHTML = "save";
                save_button.style.display = "none";
                edit_button = document.createElement('button');
                edit_button.id = "edit";
                edit_button.innerHTML = "edit";
                post.appendChild(text_area);
                post.appendChild(save_button);
                post.appendChild(edit_button);
            }

            post.appendChild(date);
            post.appendChild(like);
            post.appendChild(like_text);
            post.appendChild(like_button);

            document.querySelector('#posts').append(post);

            
        });

        if (data.next_button) {
            document.getElementById('NEXT_PAGE').style.display = "block";
        }
        else{
            document.getElementById('NEXT_PAGE').style.display = "none";
        }

        if (data.previous_button) {
            document.getElementById('PREVIOUS_PAGE').style.display = "block";
        }
        else{
            document.getElementById('PREVIOUS_PAGE').style.display = "none";
        }

    })
};

function load_10() {   

    fetch(`/posts?page=${paginator_page}`)
    .then(response => response.json())
    .then(data =>{
        data.post.forEach(element => {
            const post = document.createElement('div');
            post.className = 'POST';
            author = document.createElement('a');  
            author.className = 'AUTHOR';   
            author.innerHTML = element.author;
            author.href = "profile/"+ author.innerHTML;
            text = document.createElement('h2');
            text.className = "text";
            text.innerHTML = element.text;
            date = document.createElement('h4');
            date.className = "date";
            date.innerHTML = element.date;
            like = document.createElement('h6');
            like.style.display = "inline"; 
            like.className = "like";
            like.innerHTML = element.like;
            like_text = document.createElement('h6')
            like_text.style.display = "inline";
            if(element.like > 0){
                like_text.innerHTML= " Likes";
            }
            else{
                like_text.innerHTML=" Like";
            } 

            like_button = document.createElement('button');
            like_button.className = 'like_button';

            //console.log(data.user);
            if (data.user !== ""){
                like_button.style.display = "block";
                if (element.liked){                    
                    like_button.innerHTML = "Unlike";
                }
                else{
                    like_button.innerHTML = "Like";
                }
            }
            else{
                like_button.style.display = "none";
            }

            post.appendChild(author);
            post.appendChild(text);
           
            //console.log(element.liked);

            if(element.author === data.user){
                text_area = document.createElement('textarea');
                text_area.value = element.text;
                text_area.id = "task";
                text_area.type = 'text';
                text_area.style.display = "none";
                save_button = document.createElement('button');
                save_button.id = "send";
                save_button.innerHTML = "save";
                save_button.style.display = "none";
                edit_button = document.createElement('button');
                edit_button.id = "edit";
                edit_button.innerHTML = "edit";
                post.appendChild(text_area);
                post.appendChild(save_button);
                post.appendChild(edit_button);
            }

            post.appendChild(date);
            post.appendChild(like);
            post.appendChild(like_text);
            post.appendChild(like_button);

            document.querySelector('#posts').append(post);
        });

        if (data.next_button) {
            document.getElementById('NEXT_PAGE').style.display = "block";
        }
        else{
            document.getElementById('NEXT_PAGE').style.display = "none";
        }

        if (data.previous_button) {
            document.getElementById('PREVIOUS_PAGE').style.display = "block";
        }
        else{
            document.getElementById('PREVIOUS_PAGE').style.display = "none";
        }
    })
};


function clearBox(elementID)
{
    document.getElementById(elementID).innerHTML = "";
}

function load_10_followed() {

    fetch(`/posts?page=${paginator_page}&f=true`)
    .then(response => response.json())
    .then(data =>{
        data.post.forEach(element => {
            const post = document.createElement('div');
            post.className = 'POST';
            author = document.createElement('a');  
            author.className = 'AUTHOR';   
            author.innerHTML = element.author;
            author.href = "profile/"+ author.innerHTML;
            text = document.createElement('h2');
            text.innerHTML = element.text;
            date = document.createElement('h4');
            date.className = "date";
            date.innerHTML = element.date;
            like = document.createElement('h6');
            like.style.display = "inline"; 
            like.className = "like";
            like.innerHTML = element.like;
            like_text = document.createElement('h6')
            like_text.style.display = "inline";
            if(element.like > 0){
                like_text.innerHTML= " Likes";
            }
            else{
                like_text.innerHTML=" Like";
            } 
            
            like_button = document.createElement('button');
            like_button.className = 'like_button';

            //console.log(data.user);
            if (data.user !== ""){
                like_button.style.display = "block";
                if (element.liked){                    
                    like_button.innerHTML = "Unlike";
                }
                else{
                    like_button.innerHTML = "Like";
                }
            }
            else{
                like_button.style.display = "none";
            }

            post.appendChild(author);
            post.appendChild(text);
            post.appendChild(date);
            post.appendChild(like);
            post.appendChild(like_text);
            post.appendChild(like_button);

            document.querySelector('#posts').append(post);
        });
    })
};