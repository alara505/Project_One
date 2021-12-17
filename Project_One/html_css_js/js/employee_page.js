// Automatically get all employee information to pull up into single page



const table = document.getElementById("employeeTable");
const tableBody = document.getElementById("employeeBody");

async function getAllEmployeeData(){
    let url = "http://127.0.0.1:5000/employee/all";

    let response = await fetch(url);

    if(response.status === 200){
        let body = await response.json();
        populateData(body);
    }
    else{
        alert("There was a problem trying to get the employee information: apologies!");
    }

}

function populateData(responsebody){
    
    for (let employee of responsebody){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${employee.employeeId}</td><td>${employee.firstname}</td><td>${employee.lastname}</td><td>${employee.message}</td><td>${employee.reimbursenumber}</td>`
        tableBody.appendChild(tableRow);
    }
}
getAllEmployeeData()