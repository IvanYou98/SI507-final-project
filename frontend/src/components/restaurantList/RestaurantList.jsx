import React from 'react'
import RestaurantItem from '../restaurantItem/RestaurantItem'
import './RestaurantList.css'

const RestaurantList = ({ restaurants }) => {
    return (
        <div className='restaurant-list-container'>
            {restaurants &&
                restaurants.map(restaurant => (
                    <RestaurantItem key={restaurant.id} restaurant={restaurant} />
                ))
            }
        </div >


    )
}

export default RestaurantList