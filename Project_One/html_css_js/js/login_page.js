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

