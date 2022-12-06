import React, { Fragment } from 'react'
import LocationOnIcon from '@mui/icons-material/LocationOn';
import CircularProgress from '@mui/material/CircularProgress';
import axios from 'axios'

import './SearchBar.css'
import { useState } from 'react';
import {Button} from "@mui/material";
const SearchBar = ({ setRestaurants, setLat, setLng }) => {
    const [address, setAddress] = useState("");
    const [term, setTerm] = useState("")
    const [isLocating, setIsLocating] = useState(false);

    const getCurrentLocation = async () => {
        if (navigator.geolocation) {
            setIsLocating(true)
            navigator.geolocation.getCurrentPosition(position => {
                let lat = position.coords.latitude;
                let long = position.coords.longitude;
                setLat(lat);
                setLng(long);
                axios.get(`/location/current?long=${long}&lat=${lat}`
                ).then(res => {
                    setAddress(res.data.results[0].formatted_address)
                    setIsLocating(false)
                }).catch(err => {
                    setIsLocating(false)
                })
            });
        } else {
            console.log('Geo location is not supported in current browser');
        }
    }

    const searchRestaurants = () => {
        axios.get(`/location/geolocation?address=${address}`
        ).then(res => {
            setLng(res.data.results[0].geometry.location.lng);
            setLat(res.data.results[0].geometry.location.lat);
        }).then(
            axios.get(`/restaurants?term=${term}&location=${address.replace(' ', '+')}`
            ).then(res => {
                console.log(res.data);
                setRestaurants(res.data.businesses);
            })
        )
    }

    return (
        <Fragment>
            <div className='search-bar-container'>
                <input type="text"
                    className='search-bar-term-field'
                    placeholder='Search for restaurants...'
                    onChange={e => setTerm(e.target.value)}
                    onKeyUp={e => e.keyCode === 13 && searchRestaurants()} />
                <input type="text" className='search-bar-location-field' placeholder='Location' value={address} onChange={e => setAddress(e.target.value)} />
                <div className='search-bar-location-icon'>
                    {
                        isLocating ? <CircularProgress className='search-bar-location-progress-bar' size={20} /> : <LocationOnIcon onClick={getCurrentLocation} />
                    }
                </div>
                <Button variant="outlined" color="inherit" onClick={searchRestaurants}>
                    Search
                </Button>
            </div>
            <div className='search-bar-bottom-divider'></div>
        </Fragment>

    )
}

export default SearchBar