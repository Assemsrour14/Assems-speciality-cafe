import http.server
import socketserver
import webbrowser
from urllib.parse import parse_qs

# Full HTML with updated features and organized layout
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Assem's Specialty Cafe</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f9;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            color: #333;
        }

        header {
            background-color: #3e2723;
            color: white;
            padding: 20px 0;
            text-transform: uppercase;
            font-size: 36px;
            letter-spacing: 2px;
            position: relative;
            text-align: center;
        }

        .nav-links {
            margin-top: 10px;
        }

        .nav-links a {
            color: white;
            text-decoration: none;
            font-size: 20px;
            margin: 0 15px;
        }

        .nav-links a:hover {
            color: #FF6347;
        }

        #cart-icon {
            position: absolute;
            top: 20px;
            right: 20px;
            font-size: 30px;
            cursor: pointer;
        }

        #cart-count {
            background-color: red;
            color: white;
            padding: 5px 10px;
            border-radius: 50%;
            position: absolute;
            top: -5px;
            right: -5px;
            font-size: 14px;
        }

        main {
            padding: 50px 10%;
        }

        .category {
            font-size: 30px;
            font-weight: bold;
            color: #3e2723;
            margin-top: 40px;
        }

        .menu-item {
            background-color: #fff;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin: 15px;
            text-align: center;
            width: 230px;
            transition: transform 0.3s ease-in-out, box-shadow 0.3s;
            cursor: pointer;
        }

        .menu-item:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 10px rgba(0, 0, 0, 0.2);
        }

        .menu-item img {
            width: 100%;
            height: 150px;
            object-fit: cover;
            border-radius: 10px;
        }

        .menu-item p {
            font-size: 18px;
            color: #3e2723;
            font-weight: bold;
            margin-top: 15px;
        }

        .order-summary {
            background-color: #fff;
            padding: 25px;
            margin-top: 40px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        .order-summary h3 {
            color: #3e2723;
        }

        .order-summary ul {
            list-style-type: none;
            padding: 0;
            font-size: 18px;
            margin-top: 15px;
        }

        .order-summary li {
            margin-bottom: 8px;
        }

        .order-summary p {
            font-size: 20px;
            color: #3e2723;
            font-weight: bold;
        }

        .order-summary button {
            background-color: #3e2723;
            color: white;
            font-size: 18px;
            padding: 12px 25px;
            border: none;
            border-radius: 8px;
            margin-top: 20px;
            cursor: pointer;
        }

        .order-summary button:hover {
            background-color: #FF6347;
        }

        .payment-section {
            margin-top: 40px;
            padding: 20px;
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .payment-section select, .payment-section input {
            padding: 10px;
            margin: 10px 0;
            width: 100%;
            border-radius: 8px;
            border: 1px solid #ddd;
        }

        .payment-section button {
            background-color: #3e2723;
            color: white;
            font-size: 18px;
            padding: 12px 25px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }

        .payment-section button:hover {
            background-color: #FF6347;
        }

        .thank-you-page {
            text-align: center;
            margin-top: 50px;
        }

        .shipment-info {
            margin-top: 20px;
            padding: 20px;
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .shipment-info input {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border-radius: 8px;
            border: 1px solid #ddd;
        }

        .category-menu {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
        }

        .menu-item {
            margin-bottom: 20px;
        }
    </style>
</head>
<body>

<header>
    Assem's Specialty Cafe
    <div class="nav-links">
        <a href="#menu">Menu</a>
        <a href="#order-summary">Order</a>
        <a href="#contact">Contact</a>
    </div>
    <div id="cart-icon" onclick="viewCart()">
        🛒
        <div id="cart-count">0</div>
    </div>
</header>

<main>
    <input type="text" id="search-bar" placeholder="Search for items..." oninput="searchItems()">
    <section id="menu">
        <div class="category">Bakery</div>
        <div class="category-menu">
            <div class="menu-item" onclick="addToOrder('Croissant', 15)">
                <img src="https://via.placeholder.com/300x200?text=Croissant" alt="Croissant">
                <p>Croissant - QAR 15</p>
            </div>
            <div class="menu-item" onclick="addToOrder('Muffin', 18)">
                <img src="https://via.placeholder.com/300x200?text=Muffin" alt="Muffin">
                <p>Muffin - QAR 18</p>
            </div>
            <div class="menu-item" onclick="addToOrder('Apple Turnover', 16)">
                <img src="https://via.placeholder.com/300x200?text=Apple+Turnover" alt="Apple Turnover">
                <p>Apple Turnover - QAR 16</p>
            </div>
            <div class="menu-item" onclick="addToOrder('Cinnamon Roll', 20)">
                <img src="https://via.placeholder.com/300x200?text=Cinnamon+Roll" alt="Cinnamon Roll">
                <p>Cinnamon Roll - QAR 20</p>
            </div>
            <div class="menu-item" onclick="addToOrder('Chocolate Croissant', 22)">
                <img src="https://via.placeholder.com/300x200?text=Chocolate+Croissant" alt="Chocolate Croissant">
                <p>Chocolate Croissant - QAR 22</p>
            </div>
            <div class="menu-item" onclick="addToOrder('Banana Bread', 18)">
                <img src="https://via.placeholder.com/300x200?text=Banana+Bread" alt="Banana Bread">
                <p>Banana Bread - QAR 18</p>
            </div>
        </div>

        <!-- Additional Items -->
        <div class="category">Snacks & Beverages</div>
        <div class="category-menu">
            <div class="menu-item" onclick="addToOrder('Donut', 12)">
                <img src="https://via.placeholder.com/300x200?text=Donut" alt="Donut">
                <p>Donut - QAR 12</p>
            </div>
            <div class="menu-item" onclick="addToOrder('Coffee', 10)">
                <img src="https://via.placeholder.com/300x200?text=Coffee" alt="Coffee">
                <p>Coffee - QAR 10</p>
            </div>
            <div class="menu-item" onclick="addToOrder('Ice Cream', 18)">
                <img src="https://via.placeholder.com/300x200?text=Ice+Cream" alt="Ice Cream">
                <p>Ice Cream - QAR 18</p>
            </div>
            <div class="menu-item" onclick="addToOrder('Snack Box', 25)">
                <img src="https://via.placeholder.com/300x200?text=Snack+Box" alt="Snack Box">
                <p>Snack Box - QAR 25</p>
            </div>
        </div>
    </section>

    <!-- Order Summary -->
    <div id="order-summary">
        <div class="order-summary">
            <h3>Order Summary</h3>
            <ul id="order-list"></ul>
            <p>Total: QAR <span id="total-cost">0</span></p>
            <button onclick="proceedToCheckout()">Proceed to Checkout</button>
        </div>
    </div>

</main>

<script>
    let orderItems = [];
    let totalCost = 0;

    function addToOrder(itemName, itemPrice) {
        orderItems.push({ name: itemName, price: itemPrice });
        totalCost += itemPrice;
        document.getElementById('order-list').innerHTML = orderItems.map(item => `<li>${item.name} - QAR ${item.price}</li>`).join('');
        document.getElementById('total-cost').textContent = totalCost;
        document.getElementById('cart-count').textContent = orderItems.length;
        setTimeout(() => alert(`${itemName} added to cart!`), 200);
    }

    function proceedToCheckout() {
        let checkoutPage = `
            <section class="payment-section">
                <h3>Choose Your Payment Method</h3>
                <select id="payment-method" onchange="toggleCardDetails()">
                    <option value="cash">Cash</option>
                    <option value="card">Card</option>
                </select>
                <div id="card-details" style="display:none;">
                    <label for="card-number">Card Number</label>
                    <input type="text" id="card-number" placeholder="Enter your card number">
                    <label for="card-expiry">Expiration Date</label>
                    <input type="text" id="card-expiry" placeholder="MM/YY">
                    <label for="card-cvv">CVV</label>
                    <input type="text" id="card-cvv" placeholder="Enter CVV">
                </div>
                <div class="shipment-info">
                    <h3>Enter Shipment Information</h3>
                    <label for="zone-number">Zone Number</label>
                    <input type="text" id="zone-number" placeholder="Enter your zone number" required>
                    <label for="street-number">Street Number</label>
                    <input type="text" id="street-number" placeholder="Enter your street number" required>
                    <label for="building-number">Building Number</label>
                    <input type="text" id="building-number" placeholder="Enter your building number" required>
                </div>
                <button onclick="submitOrder()">Submit Order</button>
            </section>
        `;
        document.querySelector('main').innerHTML = checkoutPage;
    }

    function toggleCardDetails() {
        let paymentMethod = document.getElementById('payment-method').value;
        if (paymentMethod === 'card') {
            document.getElementById('card-details').style.display = 'block';
        } else {
            document.getElementById('card-details').style.display = 'none';
        }
    }

    function submitOrder() {
        let paymentMethod = document.getElementById('payment-method').value;
        let cardNumber = document.getElementById('card-number') ? document.getElementById('card-number').value : null;
        let cardExpiry = document.getElementById('card-expiry') ? document.getElementById('card-expiry').value : null;
        let cardCVV = document.getElementById('card-cvv') ? document.getElementById('card-cvv').value : null;
        let zoneNumber = document.getElementById('zone-number').value;
        let streetNumber = document.getElementById('street-number').value;
        let buildingNumber = document.getElementById('building-number').value;

        if (paymentMethod === 'card' && (!cardNumber || !cardExpiry || !cardCVV)) {
            alert('Please fill in your card details.');
        } else if (!zoneNumber || !streetNumber || !buildingNumber) {
            alert('Please fill in your shipping information.');
        } else {
            document.body.innerHTML = `
                <div class="thank-you-page">
                    <h1>Thank You for Your Order!</h1>
                    <p>Your order has been received and is being processed.</p>
                    <p>Total: QAR ${totalCost}</p>
                    <p>You will receive a confirmation email shortly.</p>
                </div>
            `;
        }
    }
</script>

</body>
</html>
'''

# Starting the server
PORT = 8080

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html_content.encode('utf-8'))

# Open the browser immediately
webbrowser.open(f"http://localhost:{PORT}")

# Starting the server
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()

