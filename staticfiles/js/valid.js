// document.forms[1].addEventListener("submit",(e)=>{
//   e.preventDefault();
//   signup(e);
// })
  function signup(e){
    e.preventDefault();
    Firstname = document.sign.firstname.value;
    Lastname = document.sign.lastname.value;
    Email=document.sign.email.value;
    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    Username = document.sign.username.value;
    Password= document.sign.password.value;
  
    if(Firstname == ""){
      alert("Please enter firstname");
      return false;
    }
    if(int.Firstname == true){
      alert("Enter firstname in alphabets");
      return false;
    }
    if(Lastname == ""){
      alert("Please enter lastname");
      return false;
    }
  
    if(Username == ""){
      alert("Please enter username");
      return false;
    }
    if(int.Username == true){
      alert("Enter username in alphabets");
      return false;
    }
    if(Email == ""){
      alert("Please enter email");
      return false;
    }
    if(!Email.match(mailformat)) {
      alert("Please Enter valid email");
      return false;
    }
  
    var pass = /^[\w*-]{5,15}$/;
    if(Password == ""){
      alert("Please enter password");
      return false;
    }
    if(!Password.match(pass)){
      alert("password must be greater than 5");
      return false;
    }
    return true;
  }

  // document.forms[0].addEventListener("submit",(e)=>{
  //   e.preventDefault();
  //   log(e);
  // })
  
  function log(e){
    e.preventDefault();
    Username = document.fill.username.value;
    Pass = document.fill.password.value;
  
    if(Username == ""){
      alert("Please enter username");
    }
    if(int.Username == true){
      alert("Enter username in alphabets");
    }
  
    var pass = /^[\w*-]{5,15}$/;
    if(Pass == ""){
      alert("Please enter password");
    }
    if(!Pass.match(pass)){
      alert("password must be greater than 5");
    }
    return true;
  }
  