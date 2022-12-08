# Dinner Table: A Search Engine for Restaurants

## 1. Intro
<p>
After you start frontend and backend server, your <a href="http://localhost:3000/">localhost:3000</a>  should look
like this.
</p>

<img src="preview.png" alt="not found">

<p>
You can enter some category keyword in the first input field, some location
keyword in the second input field (You can also click on the navigation icon
to autofill your current location). After that, you can click the 
search button, then you will find a list of restaurants information and the google map 
will also zoom and center to the location automatically.
</p>


## 2. Tech Stack

### Frontend

<ul>
    <li>React.js</li>
    <li>Material UI</li>
</ul>

### Backend
<ul>
    <li>Flask</li>
    <li> 
    <a href="https://docs.developer.yelp.com/docs/fusion-intro">
        Yelp Fusion API</a> 
    </li>
    <li> 
    <a href="https://developers.google.com/maps/apis-by-platform">
        Google Map API</a> 
    </li>
</ul>

## 3. How to run
<ul>

<li>
    Step 0: Prerequisites: Node.js, Flask
</li>

<li>
    Step 1: Clone this repository to your local
</li>
<li>
    Step 2: Start the backend server by running the following command
</li>

```{shell}
flask run
```

<li>
    Step 3: Start the frontend server by running the following command
</li>

```{shell}
npm install
npm start
```

</ul>
