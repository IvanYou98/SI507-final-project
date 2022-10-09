import { useState } from 'react';
import './App.css';
import Header from './components/header/Header';
import RestaurantList from './components/restaurantList/RestaurantList';
import SearchBar from './components/searchBar/SearchBar';
import GoogleMapContainer from './components/googleMap/GoogleMapContainer';

function App({ google }) {
  const [lat, setLat] = useState(null);
  const [lng, setLng] = useState(null);
  const [restaurants, setRestaurants] = useState(null);
  return (
    <div className="App">
      <Header />
      <SearchBar setRestaurants={setRestaurants} setLat={setLat} setLng={setLng} />
      <div className='body'>
        <RestaurantList restaurants={restaurants} />
        <GoogleMapContainer places={restaurants} lat={lat} lng={lng} />
      </div>
    </div>
  );
}

export default App;
