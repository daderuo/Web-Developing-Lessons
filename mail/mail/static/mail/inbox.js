document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);
  document.querySelector('#submit').addEventListener('click', send_email);

  // By default, load the inbox
  load_mailbox('inbox');

});

function single_email(id,mailbox){
  //console.log(mailbox);
  fetch(`/emails/`+id)
  .then(response => response.json())
  .then(email => {
    //console.log(email);
    showEmail(email);

    if (mailbox === "Sent"){
      document.querySelector('.email_archive_btn').style.display = 'none';
    }
    else{
      fetch('/emails/'+id, {
        method: 'PUT',
        body: JSON.stringify({
            read: true
        })
      });
    }
  });
}

function showEmail(email){
  //document.querySelector('#emails-view').innerHTML = "";

  document.querySelector('#single-emails-view').style.display = 'block';
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';

  document.querySelector('#single-emails-view').innerHTML = "";

  email_id = document.createElement('h3');
  email_id.innerHTML = email.id;
  email_id.style.display = "none";
  email_id.className = "email_id";


  email_sender = document.createElement('h4');
  email_sender.innerHTML = "<h3 style='display:inline'><strong>From: </strong></h3>" + email.sender;
  email_sender.style.display = "inline";
  email_sender.className = "email_sender2";

  email_recipients = document.createElement('h4');
  email_recipients.innerHTML = "<h3 style='display:inline'><strong>To: </strong></h3>" + email.recipients;
  email_recipients.style.display = "block";
  email_recipients.className = "email_recipients2";

  email_subject = document.createElement('h4');
  email_subject.innerHTML = "<h3 style='display:inline'><strong>Subject: </strong></h3>" + email.subject;
  email_subject.style.display = "block";
  email_subject.className = "email_subject2";

  email_time = document.createElement('h4');
  email_time.innerHTML = "<h3 style='display:inline'><strong>Timestamp: </strong></h3>" + email.timestamp;
  email_time.style.display = "block";
  email_time.className = "email_time2";

  email_archive_btn = document.createElement('button');
  if(email.archived){
    email_archive_btn.innerHTML = "Unarchive";
  }
  else{
    email_archive_btn.innerHTML = "Archive";
  }
  email_archive_btn.className = "email_archive_btn";
  email_archive_btn.addEventListener('click', function(){
    a = !email.archived;
    fetch('/emails/'+email.id , {
      method: 'PUT',
      body: JSON.stringify({
          archived: a
      })
    })   

    setTimeout(function() {
      load_mailbox('inbox');
    },200);
  });

  email_reply_btn = document.createElement('button');
  email_reply_btn.innerHTML = "Reply";
  email_reply_btn.className = "email_reply_btn";
  email_reply_btn.addEventListener('click', function(){
    compose_email();

    if (email.subject.includes("Re:")){
      document.querySelector('#compose-subject').value = email.subject;
    }
    else{
      document.querySelector('#compose-subject').value = "Re: " + email.subject;
    }

    document.querySelector('#compose-recipients').value = email.sender;
    
    document.querySelector('#compose-body').value = "On " + email.timestamp + " " + email.sender + " wrote: " + email.body;

  })

  email_body = document.createElement('h4');
  email_body.innerHTML = email.body + "\n";
  email_body.style.display = "block";
  email_body.className = "email_body2";

  document.querySelector('#single-emails-view').append(email_id);
  document.querySelector('#single-emails-view').append(email_sender);
  document.querySelector('#single-emails-view').append(email_recipients);
  document.querySelector('#single-emails-view').append(email_subject);
  document.querySelector('#single-emails-view').append(email_time);
  document.querySelector('#single-emails-view').append(email_archive_btn);
  document.querySelector('#single-emails-view').append(email_reply_btn);
  document.querySelector('#single-emails-view').append(document.createElement('hr'));
  document.querySelector('#single-emails-view').append(email_body);
  
}

function send_email(){

  recipients = document.querySelector('#compose-recipients').value;
  subject = document.querySelector('#compose-subject').value;
  body = document.querySelector('#compose-body').value;

  console.log(recipients);
  console.log(subject);
  console.log(body);
 
  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
        recipients: recipients,
        subject: subject,
        body: body
    })
  })
  .then(response => response.json())
  .then(result => {
      // Print result
      
      console.log(result);
  });
}

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#single-emails-view').style.display = 'none';
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').innerHTML = '';
  document.querySelector('#single-emails-view').style.display = 'none';
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  p = document.querySelector('#emails-view');
  n =document.createElement('h3');
  n.id = 'inbox_name';
  n.innerHTML = mailbox.charAt(0).toUpperCase() + mailbox.slice(1);
  p.append(n);
  //document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  fetch(`/emails/`+mailbox)
  .then(response => response.json())
  .then(emails => {
    //console.log(emails);
    emails.forEach(showEmails);
    
  });

  /*if (mailbox === "sent"){
    a = document.querySelector('.email_archive_btn');
    console.log(a);
    document.querySelector('.email_archive_btn').style.display = 'none';
  }*/

}

function showEmails(emails){
  //console.log(emails.archived);

  mailbox = document.querySelector('#inbox_name').innerHTML;

  const email = document.createElement('div');
  email.id = "email";
  email.addEventListener('click', function() {
    single_email(emails.id, mailbox);
  });
  //console.log(emails);

  if (emails.read){
    email.style.backgroundColor = "rgb(160, 160, 160)";
  }
  else{
    email.style.backgroundColor = "white";
  }

  email_id = document.createElement('h3');
  email_id.innerHTML = emails.id;
  email_id.style.display = "none";
  email_id.className = "email_id";

  email_sender = document.createElement('h3');
  email_sender.innerHTML = emails.sender;
  email_sender.style.display = "inline";
  email_sender.className = "email_sender";

  email_subject = document.createElement('h3');
  email_subject.innerHTML = emails.subject;
  email_subject.style.display = "inline";
  email_subject.className = "email_subject";

  email_time = document.createElement('h4');
  email_time.innerHTML = emails.timestamp;
  email_time.style.display = "inline";
  email_time.className = "email_time";

  email.append(email_id);
  email.append(email_sender);
  email.append(email_subject);
  email.append(email_time);

  document.querySelector('#emails-view').append(email);
  
}