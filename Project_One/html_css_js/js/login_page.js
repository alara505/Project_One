// async function loginAttempt(){
//     //grab the sign in data from the webpage
//     let username = document.getElementById("username").value;
//     let password = document.getElementById("password").value;

//     //put it in a json and post it to http://127.0.0.1:5000/login
//     loginJson = JSON.stringify({"username":username, "password":password});
//     console.log(loginJson)
//     let url = "http://127.0.0.1:5000/employee/login";
//     let the_request = await fetch(url, {
//         method:"POST", headers: {'Content-Type': 'application/json'},
//         body:loginJson}).then(response => {return response.json()});

//     // store the information for the session 
//     sessionStorage.setItem("userId", the_request["employee_id"]);
//     sessionStorage.setItem("userName", the_request["username"]);
//     sessionStorage.setItem("password", the_request["secretword"]);
//     sessionStorage.setItem("name", the_request["first_name"] + the_request["last_name"]);

//     if(sessionStorage.getItem("username") === username){
//         if(sessionStorage.getItem("password") === password){
//             window.location.href = "employee_page.html";
//         }
//         else{
//             alert("Incorrect username or password, try again.");
//         }
//     }
// }

async function LoginManager(){
    let url = "http://127.0.0.1:5000/manager/login"
    const username = document.getElementById("username");
    const password = document.getElementById("password");

    sessionStorage.setItem("username", username.value);
    sessionStorage.setItem("password", password.value);
    console.log(username.value);
    console.log(password.value);
    managerJSON = JSON.stringify({"username": username.value.toLowerCase(), "password": password.value});
    console.log(managerJSON);

    let response = await fetch(url, {
        method: "POST",
        headers:{"Content-Type": 'application/json'},
        body:managerJSON}).then(response => {return response.json()});

    if (response.username == username.value.toLowerCase() && response.password == password.value){
        window.location.href = "../html/manager_page.html";
    }
    else{
        alert("Invalid username or password")
        console.log(response.username, response.password);
        }
    
}

async function Login(){
    let url = "http://127.0.0.1:5000/employee/login"
    const username = document.getElementById("username");
    const password = document.getElementById("password");

    sessionStorage.setItem("username", username.value);
    sessionStorage.setItem("password", password.value);
    console.log(username.value);
    console.log(password.value);
    employeeJSON = JSON.stringify({"username": username.value.toLowerCase(), "password": password.value});
    console.log(employeeJSON);

    let response = await fetch(url, {
        method: "POST",
        headers:{"Content-Type": 'application/json'},
        body:employeeJSON}).then(response => {return response.json()});

    if (response.username == username.value.toLowerCase() && response.password == password.value){
        window.location.href = "../html/employee_page.html";
    }
    else{
        LoginManager()
        }
        
}


// async function LoginManager(){
//     let url = "http://127.0.0.1:5000/manager/login"
//     const username = document.getElementById("username");
//     const password = document.getElementById("password");

//     sessionStorage.setItem("username", username.value);
//     sessionStorage.setItem("password", password.value);
//     console.log(username.value);
//     console.log(password.value);
//     managerJSON = JSON.stringify({"username": username.value.toLowerCase(), "password": password.value});
//     console.log(managerJSON);

//     let response = await fetch(url, {
//         method: "POST",
//         headers:{"Content-Type": 'application/json'},
//         body:managerJSON}).then(response => {return response.json()});

//     if (response.username == username.value.toLowerCase() && response.password == password.value){
//         window.location.href = "../html/manager_page.html";
//     }
//     else{
//         alert("Invalid username or password")
//     }
// }

