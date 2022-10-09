import GoogleMapReact from 'google-map-react'
import React from 'react'
import { GOOGLE_MAP_API_KEY } from '../../constants';
import Marker from './Marker';

const GoogleMapContainer = ({ lng, lat, places }) => {
    const defaultProps = {
        center: {
            lat: 42.28933,
            lng: -83.7352
        },
        zoom: 13
    };

    return (
        // Important! Always set the container height explicitly
        <div style={{ height: '80vh', width: '50%', marginLeft: '40px' }}>
            <GoogleMapReact
                bootstrapURLKeys={{ key: GOOGLE_MAP_API_KEY }}
                defaultCenter={defaultProps.center}
                defaultZoom={defaultProps.zoom}
                center={{ lat: lat, lng: lng }}
            >
                {
                    places && places.map(place => <Marker lat={place.coordinates.latitude} lng={place.coordinates.longitude} tooltip={place.name} />)
                }
            </GoogleMapReact>
        </div>
    );
}

export default GoogleMapContainer