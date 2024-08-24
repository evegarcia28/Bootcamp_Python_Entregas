const clients = [
    { id: '123', name: 'Juan Perez', password: 'pass123', balance: 1000000 },
    { id: '456', name: 'Maria Lopez', password: 'pass456', balance: 2000000 },
    { id: '789', name: 'Carlos Ruiz', password: 'pass789', balance: 1500000 },
];

let currentClient = null;

function login() {
    const id = document.getElementById('id').value;
    const password = document.getElementById('password').value;
    currentClient = clients.find(client => client.id === id && client.password === password);

    if (currentClient) {
        document.getElementById('login').style.display = 'none';
        document.getElementById('menu').style.display = 'block';
        document.getElementById('error').innerText = '';
        alert(`Bienvenido(a) ${currentClient.name}`);
    } else {
        document.getElementById('error').innerText = 'Identificador o Clave incorrecta';
    }
}

function checkBalance() {
    alert(`Su saldo actual es: $${currentClient.balance}`);
}

function retiro() {
    
    const amount = prompt(`Su saldo actual es: $${currentClient.balance}\nIngrese el monto a girar:`);
    const amountNum = parseFloat(amount);

    if (amountNum > currentClient.balance) {
        alert('Fondos insuficientes');
    } else {
        currentClient.balance -= amountNum;
        alert(`Giro realizado. Su nuevo saldo es: $${currentClient.balance}`);
    }
}

function deposito() {
    
    const amount = prompt(`Su saldo actual es: $${currentClient.balance}\nIngrese el monto a depositar:`);
    const amountNum = parseFloat(amount);
    currentClient.balance += amountNum;
    alert(`Depósito realizado. Su nuevo saldo es: $${currentClient.balance}`);
}

function logout() {
    currentClient = null;
    document.getElementById('menu').style.display = 'none';
    document.getElementById('login').style.display = 'block';
    document.getElementById('name').value = '';
    document.getElementById('password').value = '';
    document.getElementById('message').innerText = '';
}