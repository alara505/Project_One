// Automatically get all employee information to pull up into single page
const employeeTable = document.getElementById("employeeTable");
const employeeTableBody = document.getElementById("employeeBody");
const reimbursementTable = document.getElementById("reimbursementTable");
const reimbursementTableBody = document.getElementById("reimbursementBody");
const username = sessionStorage.getItem("username");
/******************************************************************** Below is Create Employee Reimbursement */
const reimbursementId = 0
const employeeId = document.getElementById("employeeIdInput");
const managerId = document.getElementById("managerIdInput");
const requestReimbursement = document.getElementById("requestReimbursementInput");
const reason = document.getElementById("reason");
const approval = "Pending";
const managerComment = "";

function logout(){
    sessionStorage.clear();
    window.location.href = "../html/login.html"
}

async function employeeCreateReimbursement(){
    let response = await fetch(
        "http://127.0.0.1:5000/reimbursement", {
            method: "POST", headers: {"Content-Type": "application/json"},
            body: JSON.stringify({"reimbursementId":reimbursementId, "employeeId":employeeId.value, "managerId":managerId.value, "reimbursement":requestReimbursement.value, "reason":reason.value, "approval":approval, "managerComment":managerComment})

        }
    )
    if(response.status === 200){
        let body = await response.json();
    }
    else{
        alert("There was a problem trying to request a reimbursement form: apologies!");
    }
}

async function getAllEmployeeData(){
    let url = "http://127.0.0.1:5000/employee/" + username.toLowerCase();
    let response = await fetch(url);

    if(response.status === 200){
        let body = await response.json();
        console.log(body);
        populateEmployeeData(body);
        getAllReimbursementInfo();
    }
    else{
        alert("There was a problem trying to get the employee information: apologies!");
    }

}

//this function to grab all the reimbursement data.
async function getAllReimbursementInfo(){
    let employeeID = sessionStorage.getItem("employeeId");
    let url = "http://127.0.0.1:5000/employee/reimbursement/" + employeeID;
    let response = await fetch(url);
    
    if(response.status === 200){
        let body = await response.json();
        console.log(body);
        populateReimbursementsData(body);
    }
    else{
        alert("There was a problem trying to receive the reimbursement information: apologies!");
    }
}


//function to grab the employee...
function populateEmployeeData(employee){
    let tableRow = document.createElement("tr");
    tableRow.innerHTML = ''
    tableRow.innerHTML = `<td>${employee.employeeId}</td><td>${employee.firstName}</td><td>${employee.lastName}</td><td>${employee.username}</td>`;
    employeeTableBody.appendChild(tableRow);
    sessionStorage.setItem("employeeId", employee.employeeId);

}

//function to grab the reimbursement for the employee...
function populateReimbursementsData(responseBody){
    for(let reimbursement of responseBody){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${reimbursement.reimbursementId}</td><td>${reimbursement.managerId}</td><td>${reimbursement.reimbursement}</td><td>${reimbursement.reason}</td><td>${reimbursement.approval}</td><td>${reimbursement.managerComment}</td>`;
        console.log(tableRow);
        reimbursementTableBody.appendChild(tableRow);
        console.log(reimbursementTableBody);
    }
}
getAllEmployeeData();


//create a function for the employee to submit an reimbursement...

//create function to show previous reimbursements or pending reimbursements.

//function to have logout scene and restart all data if possible...

//statistics function for all the employee page...


