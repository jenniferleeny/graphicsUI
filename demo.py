<!doctype html>
<html> 
    <head>
        <title>Ubermelon Order Form</title>

    </head>
    <body>
        <h1>Order!</h1>
        <table>
            <tr>
                <th>Melon Name</th>
                <th>Price per lb</th>
            </tr>
            <tr>
                <td>Watermelon</td>
                <td>$1.59</td>
            </tr>
            <tr>
                <td>Honeydew</td>
                <td>$0.99</td>
            </tr>
            <tr>
                <td>Canteloupe</td>
                <td>$1.29</td>
            </tr>
            <tr>
                <td>Crenshaw</td>
                <td>$2.19</td>
            </tr>
            <tr>
                <td>Canary</td>
                <td>$11.99</td>
            </tr>
        </table>
        <p> Place your orders here! You know you want to.</p>
        <form action="https://ubermelon-order-form.herokuapp.com/process" method="GET">
            <label for="firstname">First Name:</label>
            <input type="text" name = "firstname"> <br>
            <label for="lastname">Last Name:&nbsp</label>
            <input type="text" name = "lastname"><br>
            Melon Type:
                <select name="melontype">
                    <option value="watermelon">Watermelon</option>
                    <option value="honeydew">Honeydew</option>
                    <option value="canteloupe">Canteloupe</option>
                    <option value="crenshaw">Crenshaw</option>
                    <option value="canary">Canary</option>
                </select>
                <br>
            <label for="quantity">Quantity:</label>
            <input type="text" name = "quantity"><br>
            <label for="deliverytime">Delivery Time:</label>
            <input type="radio" name="time" value="am">12:00am-12:00pm
            <input type="radio" name="time" value="pm">12:00pm-12:00am
            <input type="radio" name="time" value="wat">Time is an illusion
            <br>

            <label for="returningcustomer">Returning Customer?</label>
            <input type="radio" name="returning" value="yes">Yes
            <input type="radio" name="returning" value="no">No
            <br>

            <label for="statisticalpurposes">For Statistical Purposes:</label>
            <input type="checkbox" name="stats" value="dog">Dog
            <input type="checkbox" name="stats" value="cat">Cat
            <input type="checkbox" name="stats" value="hedgehog">Hedgehog
            <input type="checkbox" name="stats" value="balloonicorn">Balloonicorn
            <input type="checkbox" name="stats" value="yak">Yak
            <br>

            <input type="submit" value="Submit">

        </form>

    </body>
</html>