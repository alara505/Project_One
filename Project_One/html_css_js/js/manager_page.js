const managerTable = document.getElementById("managerTable");
const managerTableBody = document.getElementById("managerBody");
const reimbursementTable = document.getElementById("reimbursementTable");
const reimbursementTableBody = document.getElementById("reimbursementBody");
const reimbursementTablePending = document.getElementById("reimbursementPendingBody");
const username = sessionStorage.getItem("username");
const reimbursementId = 0

const reimbursementRequestsTotal = document.getElementById("reimbursementRequestsTotal");
const reimbursementRequestsPending = document.getElementById("reimbursementRequestsPending");
const reimbursementRequestsApproved = document.getElementById("reimbursementRequestsApproved");
const reimbursementRequestsDenied = document.getElementById("reimbursementRequestsDenied");

function logout(){
    sessionStorage.clear();
    window.location.href = "../html/login.html"
}

async function getAllManagerData(){
    let url = "http://127.0.0.1:5000/manager/" + username.toLowerCase();
    let response = await fetch(url);

    if(response.status === 200){
        let body = await response.json();
        console.log(body);
        populateManagerData(body);
        getAllPastReimbursementData();
        getAllPendingReimbursementData();
    }
    else{
        alert("There was a problem trying to get the manager information: apologies!");
    }

}

//function still needs more work...
async function getAllPendingReimbursementData(){
    let managerID = sessionStorage.getItem("managerId");
    let url = "http://127.0.0.1:5000/manager/pending/reimbursement/" + managerID;
    let response = await fetch(url);

    if(response.status === 200){
        let body = await response.json();
        populatePendingReimbursementData(body);
    }
    else{
        alert("There was a problem trying to get the pending reimbursement information: apologies!");
    }
}
function populatePendingReimbursementData(responseBody){
    for( let reimbursement of responseBody){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${reimbursement.reimbursementId}</td><td>${reimbursement.employeeId}</td><td>${reimbursement.reimbursement}</td><td>${reimbursement.reason}</td><td>${reimbursement.approval}</td><td>${reimbursement.managerComment}</td>`;
        console.log(tableRow);
        reimbursementTablePending.appendChild(tableRow);
        console.log(reimbursementTablePending);
    }
}

async function getAllPastReimbursementData(){
    let managerID = sessionStorage.getItem("managerId");
    let url = "http://127.0.0.1:5000/past/reimbursements/" + managerID;
    let response = await fetch(url);

    if(response.status === 200){
        let body = await response.json();
        populatePastReimbursementData(body);
    }
    else{
        alert("There was a problem trying to get the past reimbursement information: apologies!");
    }
}

function populatePastReimbursementData(responseBody){
    for (let reimbursement of responseBody){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${reimbursement.reimbursementId}</td><td>${reimbursement.employeeId}</td><td>${reimbursement.reimbursement}</td><td>${reimbursement.reason}</td><td>${reimbursement.approval}</td><td>${reimbursement.managerComment}</td>`;
        console.log(tableRow);
        reimbursementTableBody.appendChild(tableRow);
        console.log(reimbursementTableBody);
    }
}

async function updateApproveReimbursementInfo(){
    let reimbursementId = document.getElementById("ReimbursementIdInput").value;
    console.log(reimbursementId);
    let employeeId = document.getElementById("employeeIdInput").value;
    console.log(employeeId);
    let managerId = document.getElementById("managerIdInput").value;
    console.log(managerId);
    let reimbursement = document.getElementById("requestReimbursementInput").value;
    console.log(reimbursement);
    let reason = document.getElementById("reason").value;
    console.log(reason);
    let approval = document.getElementById("approval").value;
    console.log(approval);
    let managerComment = document.getElementById("managerComment").value;
    console.log(managerComment);


    let url = "http://127.0.0.1:5000/reimbursement/approve/" + reimbursementId;
    let response = await fetch(url, {
    method: "PATCH",
    headers:{"Content-Type": 'application/json'},
    body: JSON.stringify({"employeeId":employeeId, "managerId":managerId, "reimbursement":reimbursement, "reason":reason, "approval":approval, "managerComment":managerComment})
    });
    
    
    if(response.status === 200){
        let body = await response.json();
        console.log(body);
        //populateApproveReimbursementData(body);
    }
    else{
        alert("There was a problem trying to update the pending reimbursement informaton: apologies!");
    }
}

async function updateDenyReimbursementInfo(){
    let reimbursementId = document.getElementById("ReimbursementIdInput").value;
    console.log(reimbursementId);
    let employeeId = document.getElementById("employeeIdInput").value;
    console.log(employeeId);
    let managerId = document.getElementById("managerIdInput").value;
    console.log(managerId);
    let reimbursement = document.getElementById("requestReimbursementInput").value;
    console.log(reimbursement);
    let reason = document.getElementById("reason").value;
    console.log(reason);
    let approval = document.getElementById("approval").value;
    console.log(approval);
    let managerComment = document.getElementById("managerComment").value;
    console.log(managerComment);


    let url = "http://127.0.0.1:5000/reimbursement/deny/" + reimbursementId;
    let response = await fetch(url, {
    method: "PATCH",
    headers:{"Content-Type": 'application/json'},
    body: JSON.stringify({"employeeId":employeeId, "managerId":managerId, "reimbursement":reimbursement, "reason":reason, "approval":approval, "managerComment":managerComment})
    });


    if (response.status === 200){
        let body = await response.json();
        //populateDenyReimbursementdata(body);
    }
    else{
        alert("There was a problem trying to update the pending reimbursement information: apologies!");
    }
}

function populateDenyReimbursementData(responseBody){
    for(let reimbursement of responseBody){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${reimbursement.reimbursementId}</td><td>${reimbursement.employeeId}</td><td>${reimbursement.reimbursementId}</td><td>${reimbursement.reason}</td><td>${reimbursement.approval}</td><td>${reimbursement.managerComment}</td>`;
        console.log(tableRow);
        reimbursementTablePending.appendChild(tableRow);
        console.log(reimbursementTablePending);
    }
}

function populateApproveReimbursementData(responseBody){
    for (let reimbursement of responseBody){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${reimbursement.reimbursementId}</td><td>${reimbursement.employeeId}</td><td>${reimbursement.reimbursementId}</td><td>${reimbursement.reason}</td><td>${reimbursement.approval}</td><td>${reimbursement.managerComment}</td>`;
        console.log(tableRow);
        reimbursementTablePending.appendChild(tableRow);
        console.log(reimbursementTablePending);
    }
}

function populateManagerData(manager){
    let tableRow = document.createElement("tr");
    // tableRow.innerHTML = ''
    tableRow.innerHTML = `<td>${manager.managerId}</td><td>${manager.firstName}</td><td>${manager.lastName}</td><td>${manager.username}</td>`;
    managerTableBody.appendChild(tableRow);
    sessionStorage.setItem("managerId", manager.managerId);
}

async function getReimbursementRequestsTotal(){
    const response = await fetch(`http://127.0.0.1:5000/manager/total`)
    const totalRequests = await response.json()
    const total = totalRequests.totalRequests
    reimbursementRequestsTotal.innerHTML = total
}

async function getReimbursementRequestsPending(){
    const response = await fetch(`http://127.0.0.1:5000/manager/pending`)
    const pendingRequests = await response.json()
    const pending = pendingRequests.PendingRequests
    reimbursementRequestsPending.innerHTML = pending
}

async function getReimbursementRequestsApproved(){
    const response = await fetch(`http://127.0.0.1:5000/manager/approved`)
    const approvedRequests = await response.json()
    const approved = approvedRequests.ApprovedRequests
    reimbursementRequestsApproved.innerHTML = approved
}
async function getReimbursementRequestsDenied(){
    const response = await fetch(`http://127.0.0.1:5000/manager/denied`)
    const deniedRequests = await response.json()
    const denied = deniedRequests.DeniedRequests
    reimbursementRequestsDenied.innerHTML = denied
}


getAllManagerData();
getReimbursementRequestsTotal();
getReimbursementRequestsPending();
getReimbursementRequestsApproved();
getReimbursementRequestsDenied();

